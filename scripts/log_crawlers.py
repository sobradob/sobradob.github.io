#!/usr/bin/env python3
"""
Log AI crawler traffic from Cloudflare Analytics to a CSV file.

Queries the Cloudflare GraphQL Analytics API for the past hour,
filters for known AI bot user agents, and appends results to
data/crawler_log.csv in the repository.

Environment variables required:
    CF_API_TOKEN  - Cloudflare API token with Zone Analytics read permission
    CF_ZONE_ID    - Cloudflare Zone ID
"""

import csv
import json
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

# Known AI bot identifiers (lowercase substrings to match in user agent strings)
AI_BOT_IDENTIFIERS = {
    "meta-externalagent": "Meta AI",
    "chatgpt-user": "ChatGPT",
    "amazonbot": "Amazonbot",
    "bytespider": "Bytespider",
    "bingbot": "Bingbot",
    "claudebot": "ClaudeBot",
    "gptbot": "GPTBot",
    "anthropic-ai": "Anthropic AI",
    "perplexitybot": "PerplexityBot",
}

CF_GRAPHQL_ENDPOINT = "https://api.cloudflare.com/client/v4/graphql"

CSV_PATH = Path(__file__).resolve().parent.parent / "data" / "crawler_log.csv"
CSV_HEADERS = ["timestamp", "bot_name", "request_count", "host"]

GRAPHQL_QUERY = """
query GetAICrawlerTraffic($zoneTag: String!, $start: String!, $end: String!) {
  viewer {
    zones(filter: { zoneTag: $zoneTag }) {
      httpRequestsAdaptiveGroups(
        limit: 5000
        orderBy: [count_DESC]
        filter: {
          datetime_geq: $start
          datetime_lt: $end
        }
      ) {
        count
        dimensions {
          userAgent
          clientRequestHTTPHost
        }
      }
    }
  }
}
"""


def get_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        print(f"ERROR: Missing required environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value


def identify_bot(user_agent: str) -> str | None:
    ua_lower = user_agent.lower()
    for identifier, bot_name in AI_BOT_IDENTIFIERS.items():
        if identifier in ua_lower:
            return bot_name
    return None


def query_cloudflare(api_token: str, zone_id: str, start: str, end: str) -> list[dict]:
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    payload = {
        "query": GRAPHQL_QUERY,
        "variables": {"zoneTag": zone_id, "start": start, "end": end},
    }

    resp = requests.post(CF_GRAPHQL_ENDPOINT, json=payload, headers=headers, timeout=30)
    resp.raise_for_status()

    data = resp.json()

    if data.get("errors"):
        errors = json.dumps(data["errors"], indent=2)
        print(
            f"ERROR: Cloudflare GraphQL API returned errors:\n{errors}", file=sys.stderr
        )
        sys.exit(1)

    zones = data.get("data", {}).get("viewer", {}).get("zones", [])
    if not zones:
        print("ERROR: No zone data returned. Check CF_ZONE_ID.", file=sys.stderr)
        sys.exit(1)

    return zones[0].get("httpRequestsAdaptiveGroups", [])


def aggregate_bot_traffic(groups: list[dict], window_label: str) -> list[list[str]]:
    aggregated: dict[tuple[str, str], int] = {}

    for group in groups:
        ua = group.get("dimensions", {}).get("userAgent", "")
        host = group.get("dimensions", {}).get("clientRequestHTTPHost", "unknown")
        count = group.get("count", 0)

        bot_name = identify_bot(ua)
        if bot_name is None:
            continue

        key = (bot_name, host)
        aggregated[key] = aggregated.get(key, 0) + count

    rows = []
    for (bot_name, host), total_count in sorted(aggregated.items()):
        rows.append([window_label, bot_name, str(total_count), host])

    return rows


def write_to_csv(rows: list[list[str]]) -> None:
    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)

    write_header = not CSV_PATH.exists() or CSV_PATH.stat().st_size == 0

    with open(CSV_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(CSV_HEADERS)
        writer.writerows(rows)

    print(f"Appended {len(rows)} rows to {CSV_PATH}")


def main() -> None:
    cf_api_token = get_env("CF_API_TOKEN")
    cf_zone_id = get_env("CF_ZONE_ID")

    now = datetime.now(timezone.utc)
    end = now.replace(minute=0, second=0, microsecond=0)
    start = end - timedelta(hours=1)

    start_str = start.strftime("%Y-%m-%dT%H:%M:%SZ")
    end_str = end.strftime("%Y-%m-%dT%H:%M:%SZ")
    window_label = f"{start_str} - {end_str}"

    print(f"Querying Cloudflare for window: {window_label}")

    groups = query_cloudflare(cf_api_token, cf_zone_id, start_str, end_str)
    print(f"Received {len(groups)} user-agent/host groups from Cloudflare.")

    rows = aggregate_bot_traffic(groups, window_label)
    print(f"Found {len(rows)} AI bot entries to log.")

    if not rows:
        print("No AI crawler traffic found in the query window. Nothing to append.")
        return

    write_to_csv(rows)
    print("Done.")


if __name__ == "__main__":
    main()

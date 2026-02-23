# AI Crawler Traffic Logger

Automatically logs AI crawler traffic from Cloudflare Analytics to a CSV file in this repository every hour. Cloudflare's free tier only retains 24 hours of analytics data, so this preserves historical bot traffic for long-term analysis.

## How It Works

1. A GitHub Actions cron job runs every hour (at minute :05)
2. A Python script queries the Cloudflare GraphQL Analytics API for the previous hour's traffic
3. It filters for known AI bot user agents and aggregates request counts
4. Results are appended to `data/crawler_log.csv` and committed to the repo

### Tracked Bots

| Identifier | Logged As |
|---|---|
| `meta-externalagent` | Meta AI |
| `chatgpt-user` | ChatGPT |
| `amazonbot` | Amazonbot |
| `bytespider` | Bytespider |
| `bingbot` | Bingbot |
| `claudebot` | ClaudeBot |
| `gptbot` | GPTBot |
| `anthropic-ai` | Anthropic AI |
| `perplexitybot` | PerplexityBot |

### CSV Schema

| Column | Description |
|---|---|
| `timestamp` | Query window, e.g. `2026-02-23T14:00:00Z - 2026-02-23T15:00:00Z` |
| `bot_name` | Cleaned bot name (see table above) |
| `request_count` | Number of requests in the window |
| `host` | The hostname that was requested |

## Setup

### 1. Create a Cloudflare API Token

1. Go to [Cloudflare Dashboard](https://dash.cloudflare.com) > My Profile > API Tokens
2. Click **Create Token**
3. Use the **Custom token** template
4. Set permissions: **Zone > Analytics > Read**
5. Under Zone Resources, select your specific zone (or "All zones")
6. Click **Continue to summary** > **Create Token**
7. Copy the token — you won't be able to see it again

To find your **Zone ID**: go to your domain's Overview page in the Cloudflare dashboard. The Zone ID is shown in the right sidebar under "API".

### 2. Add GitHub Secrets

Go to your repository on GitHub > Settings > Secrets and variables > Actions, then add:

| Secret Name | Value |
|---|---|
| `CF_API_TOKEN` | Your Cloudflare API token |
| `CF_ZONE_ID` | Your Cloudflare Zone ID |

### 3. Test It

Trigger the workflow manually:

1. Go to your repository > Actions > "Log AI Crawler Traffic"
2. Click **Run workflow** > **Run workflow**
3. Check the run logs for output
4. Verify `data/crawler_log.csv` was created with a new commit

## Validation

**Important:** After the first few runs, compare the logged counts against the Cloudflare dashboard to confirm accuracy.

1. Go to Cloudflare Dashboard > Analytics & Logs > Traffic
2. Filter to the same time window as a logged entry
3. Check if bot request counts roughly match

Possible reasons for discrepancies:
- **Sampling**: Cloudflare's free tier analytics may use sampling for high-traffic zones. The GraphQL API returns sampled data on free plans, so counts may not be exact.
- **Time alignment**: The script queries aligned hour boundaries (e.g., 14:00-15:00 UTC). The dashboard may use different boundaries depending on your timezone setting.
- **User agent grouping**: The script aggregates multiple user agent strings containing the same bot identifier (e.g., different versions of GPTBot) into a single count.

## Maintenance

### Adding New Bots

Edit the `AI_BOT_IDENTIFIERS` dictionary in `scripts/log_crawlers.py`:

```python
AI_BOT_IDENTIFIERS = {
    "meta-externalagent": "Meta AI",
    "chatgpt-user": "ChatGPT",
    # Add new bots here:
    "newbot": "NewBot Display Name",
}
```

The key is a lowercase substring to match in user agent strings. The value is the clean name logged to the sheet.

### Monitoring

If the workflow fails, GitHub will show it in the Actions tab. The script exits with a non-zero code if:
- Any required environment variable is missing
- The Cloudflare API returns an error
- The HTTP request itself fails

GitHub Actions will mark the run as failed in all these cases.

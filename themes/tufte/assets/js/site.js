(function () {
  var root = document.documentElement;

  // Theme toggle: auto -> light -> dark. head.html applies the saved choice before paint.
  var btn = document.getElementById("theme-toggle");
  var order = ["auto", "light", "dark"];
  var mode = root.getAttribute("data-theme") || "auto";
  function applyTheme(m) {
    mode = m;
    if (m === "auto") root.removeAttribute("data-theme"); else root.setAttribute("data-theme", m);
    if (btn) btn.textContent = "Theme: " + m;
    try { if (m === "auto") localStorage.removeItem("theme"); else localStorage.setItem("theme", m); } catch (e) {}
  }
  if (btn) {
    btn.textContent = "Theme: " + mode;
    btn.addEventListener("click", function () { applyTheme(order[(order.indexOf(mode) + 1) % 3]); });
  }

  var content = document.querySelector(".post .content, .intro");
  if (content) {
    var paras = Array.prototype.filter.call(content.children, function (el) { return el.tagName === "P"; });

    // An opening paragraph that is only italic text ("Originally published in Forbes", "co-written with")
    // is a credit line, not the start of the piece.
    var first = paras[0];
    if (first && first === content.firstElementChild && first.children.length === 1 &&
        first.firstElementChild.tagName === "EM" && first.textContent.trim() === first.firstElementChild.textContent.trim()) {
      first.classList.add("note");
      paras.shift();
    }

    // Drop cap and small-caps lead-in on the first real paragraph, if it starts with a plain letter.
    var opening = paras[0];
    if (opening && opening.firstChild && opening.firstChild.nodeType === 3) {
      var text = opening.firstChild.nodeValue.replace(/^\s+/, "");
      var m = text.match(/^(\p{L})(\S*(?:\s+\S+){0,2})/u);
      if (m && m[0].length < text.length) {
        opening.firstChild.nodeValue = text.slice(m[0].length);
        var initial = document.createElement("span");
        initial.className = "initial";
        initial.setAttribute("aria-hidden", "true");
        initial.textContent = m[1];
        var lead = document.createElement("span");
        lead.className = "lead";
        var sr = document.createElement("span");
        sr.className = "sr";
        sr.textContent = m[1];
        lead.appendChild(sr);
        lead.appendChild(document.createTextNode(m[2]));
        opening.insertBefore(lead, opening.firstChild);
        opening.insertBefore(initial, lead);
        opening.classList.add("opening");
      }
    }
  }

  // Code: language label and highlighting (highlight.js loads on article pages only).
  document.querySelectorAll(".content pre > code").forEach(function (code) {
    var lang = (code.className.match(/language-(\w+)/) || [])[1];
    if (lang) code.parentElement.setAttribute("data-lang", lang);
    if (window.hljs && lang) {
      try { window.hljs.highlightElement(code); } catch (e) {}
    }
  });

  // Lightbox for article images that are not already links.
  document.querySelectorAll(".post .content img").forEach(function (img) {
    if (img.closest("a")) return;
    img.classList.add("zoomable");
    img.addEventListener("click", function () {
      var overlay = document.createElement("div");
      overlay.className = "lightbox";
      overlay.setAttribute("role", "dialog");
      overlay.setAttribute("aria-label", "Image preview");
      var full = document.createElement("img");
      full.src = img.currentSrc || img.src;
      full.alt = img.alt || "";
      overlay.appendChild(full);
      document.body.appendChild(overlay);
      var prev = document.body.style.overflow;
      document.body.style.overflow = "hidden";
      function close() {
        overlay.remove();
        document.body.style.overflow = prev;
        document.removeEventListener("keydown", onKey);
      }
      function onKey(ev) { if (ev.key === "Escape") close(); }
      overlay.addEventListener("click", close);
      document.addEventListener("keydown", onKey);
    });
  });
})();

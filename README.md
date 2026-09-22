# WeaveStudio Gallery

A free, growing library of ready-made **weave flows** for [WeaveStudio](https://github.com/KasstekSoftware/WeaveStudio).
Open WeaveStudio, choose **Gallery** in the left sidebar, and any flow here downloads
straight onto your canvas — no copy-paste, no cloning this repo.

Every flow is self-contained (HTTP request + decision + report), so it opens and runs
anywhere. Flows marked ⏰ are most useful when run **periodically**, which needs the
WeaveStudio **Pro Scheduler** upgrade.

## How it works

- `manifest.json` at the repo root lists every flow with a stable id and version.
- Flows live under a folder named for their function (`web/`, `api/`, …).
- WeaveStudio reads the manifest, flags anything new since your last visit, and renders
  this README in-app.

## Web

- **Website Health Check** ⏰ — Fetch a site and branch on HTTP 200 to report up or down.
- **Website Change Monitor** ⏰ — Fetch a page and flag whether an expected marker is still present.
- **Broken Link Check** — Request a URL and report whether it responds OK or is broken.
- **RSS Feed Snapshot** — Download an RSS/Atom feed and save the raw XML as a report.

## Api

- **JSON API to Report** — Call a JSON API, branch on a field, and save success or error.
- **API Latency Watch** ⏰ — Time an API call and report when it is slower than a threshold.
- **JSON Webhook Poster** — POST a JSON payload to a webhook and report sent or failed.
- **Public IP Snapshot** ⏰ — Fetch your public IP as JSON and save it — schedule it to spot changes.

---

⏰ = best run on a schedule (WeaveStudio Pro).

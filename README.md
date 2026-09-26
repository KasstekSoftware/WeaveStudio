# WeaveStudio Gallery

A free, growing library of ready-made **weave flows** and **scripts** for [WeaveStudio](https://github.com/KasstekSoftware/WeaveStudio).
Open WeaveStudio, choose **Gallery** in the left sidebar, and any flow here downloads
straight onto your canvas — no copy-paste, no cloning this repo.

Most flows are self-contained (HTTP request + decision + report). Some call the small,
dependency-free **scripts** listed below, which WeaveStudio installs automatically. Flows
marked ⏰ are most useful when run **periodically**, which needs the WeaveStudio
**Pro Scheduler** upgrade.

## How it works

- `manifest.json` at the repo root lists every flow with a stable id and version.
- `scripts/manifest.json` lists every distributable script; WeaveStudio installs new or
  updated scripts at launch (keyed by a stable id) so script-backed flows just work.
- Flows live under a folder named for their function (`web/`, `api/`, `files/`, …).
- WeaveStudio reads the manifests, flags anything new since your last visit, and renders
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

## Files

- **Pretty-Print JSON** — Reformat a JSON blob with sorted keys and 2-space indentation.
- **CSV to JSON** — Convert CSV rows into a JSON array of objects.
- **Extract JSON Field** — Pull a dotted-path value out of a JSON object.

## System

- **Run a Swift Script** — Compile and run a tiny Swift script, then print the result.
- **Say a Message (macOS)** — Run /usr/bin/say with a parameter to speak text, then print a confirmation.
- **Launch TextEdit (macOS)** — Launch the TextEdit app, then print a confirmation. Re-pick the app if macOS asks.

## Scripts

- **Reformat JSON** (`python`) — Pretty-print JSON with sorted keys and 2-space indentation.
- **CSV to JSON** (`python`) — Convert CSV text into a JSON array of objects.
- **JSON to CSV** (`python`) — Convert a JSON array of objects into CSV rows.
- **Extract JSON Field** (`python`) — Pull a dotted-path value out of a JSON object.
- **Count Lines** (`bash`) — Report the line, word, and character counts of the input.
- **To Uppercase** (`bash`) — Convert the input text to uppercase.
- **Greet (Swift)** (`swift`) — A tiny Swift script that prints a greeting for the name passed as an argument.
- **Print Line** (`bash`) — Print (echo) the message passed as the first argument — a simple final Print step.

---

⏰ = best run on a schedule (WeaveStudio Pro).

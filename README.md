# Jetlag Dial

Convert every hour between two cities on a selected date, including daylight saving changes.

Set from_zone and to_zone to IANA names, date to YYYY-MM-DD (or leave empty for the current source-zone date), and start_hour to the first displayed hour. Turn through all hours. Missing spring-forward hours are marked skipped, and both fall-back occurrences get a separate destination reading.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)

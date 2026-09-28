# ClaudeinCloud notes for Claude

- JJ's playground for browser games. Each game lives in its own folder as a single `index.html` (no build step).
- Games use three.js **r128** loaded from `https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js` so they also publish as claude.ai artifacts (the artifact CSP only allows cdnjs, jsdelivr, unpkg; fonts only from Google Fonts).
- Game HTML files are written as artifact bodies: they start with `<title>` and `<style>`, not `<!doctype>`/`<html>`. Keep `[hidden]{display:none!important}` in each file's own CSS.
- JJ plays on his phone a lot: every game needs touch controls (virtual sticks + big buttons) as well as keyboard and gamepad.
- Style family (shared with Road Crew): safety yellow `#f5b800`, survey orange `#ff6b1a`, dark asphalt panels, Big Shoulders Display / IBM Plex Sans Condensed / IBM Plex Mono.
- Show player-facing measurements in feet and inches (US).
- Testing: headless Chromium via Playwright with `--use-gl=swiftshader`. `window.__pool` in Pool Dig exposes state and a `step(dt, input)` hook for scripted tests.

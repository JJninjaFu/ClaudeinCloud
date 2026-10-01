# ClaudeinCloud notes for Claude

- JJ's playground for browser games. Each game lives in its own folder as a single `index.html` (no build step).
- Games use three.js **r128** loaded from `https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js` so they also publish as claude.ai artifacts (the artifact CSP only allows cdnjs, jsdelivr, unpkg; fonts only from Google Fonts).
- Game HTML files are written as artifact bodies: they start with `<title>` and `<style>`, not `<!doctype>`/`<html>`. Keep `[hidden]{display:none!important}` in each file's own CSS.
- JJ plays on his phone a lot: every game needs touch controls (virtual sticks + big buttons) as well as keyboard and gamepad.
- Style family (shared with Road Crew): safety yellow `#f5b800`, survey orange `#ff6b1a`, dark asphalt panels, Big Shoulders Display / IBM Plex Sans Condensed / IBM Plex Mono.
- Show player-facing measurements in feet and inches (US).
- Testing: headless Chromium via Playwright with `--use-gl=swiftshader`. `window.__pool` (Pool Dig) and `window.__crane` (Topping Out) expose state and a `step(dt, input)` hook for scripted tests. When teleporting the crane in a test, zero `cr.prevV` and `cr.aT` or the load will swing wildly.
- Skyscraper Sim is the long-term plan (demo → dig → pour → steel on one lot); see README. Build each phase as its own playable game first.
- Never put one big ground plane under a dig grid: anything dug below it gets hidden. Build the surroundings as a ring of planes outside the grid (fixed in Pool Dig and Dig & Pour).
- Game files start with charset + viewport `<meta>` tags before `<title>` so they scale right on phones when served from GitHub Pages (harmless as artifact bodies). Root `index.html` is the Pages game menu (a full HTML doc); add new games to it.
- Mineral Fork (dirt bike hillclimb): `window.__game` exposes state; `__game.sim(seconds)` runs the autopilot headless (`autoFeather` true = smooth throttle, which should top out both days; false = pinned, which should fail on the scree).
- Topping Out has three modes: gantry (default), tower (swinging load), hand (drag-to-place). `window.__dig` exposes Dig & Pour state (`startRebar()` skips to the pour).

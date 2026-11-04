# Chew Bubblegum

"We came here to chew bubblegum and kick bookkeeping ass with Jeff... and we are all out of bubblegum!!!"

A cartoon office shooter starring Jeff, a CPA with a pump shotgun. One self-contained `index.html` (canvas 2D, WebAudio, no build step, no install).

## Scenes

1. **The office.** Side-scrolling shooter along a long desk of paper stacks (JIBs, revenue statements, 1099s). Blast a stack and it bursts into dozens of sheets that tumble, drift and pile up on the floor. Mugs shatter, staplers fly, filing cabinets spit paper and topple. 30 seconds, or until every stack is gone.
2. **Cutscene.** Jeff sits down, says his piece, smashes the computer with the shotgun butt and rolls over to the backup PC.
3. **Expense Allocation.** JIB slips slide across the desk. Six buckets along the bottom: LOE, IDC, LWE, TDC, LHC, AFE. Shoot a slip when it is right over its bucket and it rockets straight down, or grab it and drag it in. Right bucket +1, wrong bucket -1. 90 seconds, 4 waves, faster each wave.
   - **MOHAWK COMPLETIONS $85,115.85** slides by in slow motion. Shoot it for a ruling.
   - **LATIGO: NETTED, NO CASH** shows up once. Don't book it. Let it pass for +2.
   - End screen: score, accuracy by bucket, rank (Bookkeeper, Staff Accountant, CPA, Jeff), Replay.

## Controls

| | Keyboard + mouse | Touch |
|---|---|---|
| Walk (office) | A / D or arrows | on-screen arrow buttons |
| Aim / fire | mouse / click (one blast per click, infinite ammo) | tap |
| Allocate | click a slip over its bucket, or drag it in | tap or drag |
| Advance dialog | click, Space or any key | tap |
| Skip | Esc (ends the office round or skips the cutscene) | |
| Mute | M | |

## Test hooks

`window.__gum` exposes `S`, `O` (office), `A` (allocation), `C` (cutscene), `step(dt, n)`, `sim(seconds)`, `frame()`, `go(scene)`, `officeShoot(worldX, worldY)` and `click(x, y)` (logical 1280 x 720 coordinates). Set `__gum.paused = true` to stop the real-time loop and `__gum.A.auto = true` to let a bot play the allocation round.

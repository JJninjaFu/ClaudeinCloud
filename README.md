# ClaudeinCloud
Experimenting w Claude in the cloud! Woot!

## Games

| Game | Folder | What it is |
|---|---|---|
| Pool Dig | [`pool-dig/`](pool-dig/index.html) | Excavator sim: dig a 33 × 16 ft backyard pool to grade (3 ft shallow to 6 ft deep), load the dump truck, and don't cut the sprinkler line. |
| Dig & Pour | [`foundation/`](foundation/index.html) | Foundation phase on the same downtown lot: dig a 33 × 33 ft basement 20 ft deep with a big laser-guided excavator (two haul trucks take turns), watch the rebar mat go in, then pump a 3 ft concrete mat. |
| Topping Out | [`topping-out/`](topping-out/index.html) | Steel erection on a downtown lot: fly columns, beams and decks from the laydown yard and build a frame floor by floor. Default gantry crane (no swing, climbs with the building) or a swinging tower crane. Four floors tops out the job. |

Each game is one self-contained HTML file. It runs in any browser, including on a phone with touch sticks, and uses three.js r128 from cdnjs.

### Pool Dig controls
- **Phone:** left stick drives, right stick swings (left/right) and reaches (up/down), **DIG** scoops or dumps, **TRIM** shaves a thin layer.
- **Keyboard:** WASD drive · Q/E swing · R/F reach · Space dig/dump · T trim · H send truck · G grade view · Z/C rotate view · wheel zoom · M sound
- **Controller:** left stick drive · right stick swing/reach · A dig/dump · X trim · Y send truck · LB/RB rotate view

### Dig & Pour controls
- **Phone:** left stick drives (pour: moves the hose), right stick swings/reaches (pour: looks around), **DIG** scoops or dumps, hold **POUR** to pour.
- **Keyboard:** WASD drive · Q/E swing · R/F reach · Space dig (hold to pour) · H send truck · Z/C rotate view · wheel zoom · M sound

### Topping Out controls
- **Phone:** left stick moves the hook (tower crane: swing and trolley), right stick hoists (up/down) and looks around, **HOOK** picks up, sets, or sends a piece back to the laydown yard, **TURN** rotates a beam 90°. **Mode: Hand** skips the crane: pick a piece in the tray and drag across the site to drop pieces into every open spot.
- **Keyboard:** WASD move hook · R/F or ↑/↓ hoist · Space hook · T turn · Z/C look around · wheel zoom · M sound
- **Controller:** left stick move hook · right stick hoist/look · RT/LT hoist · A hook · X turn

## Kerbal Space Program
- [`ksp/Hard Hat Heavy.craft`](ksp/) is a stock KSP 1.12 crew rocket: Mainsail + 4 Kickbacks, launch escape tower, and a Poodle upper stage for Mun/Minmus. See [`ksp/README.md`](ksp/README.md).

## Skyscraper Sim plan
One downtown lot, played start to finish: wrecking-ball demolition → clear rubble → dig a 20 ft basement → pour the foundation → fly the steel with the tower crane. Built one playable phase at a time:
1. ✅ Steel erection (Topping Out), gantry + tower crane. The tower crane's swing physics get reused for the wrecking ball.
2. ✅ Basement dig + foundation pour (Dig & Pour)
3. Wrecking-ball demolition (needs a physics engine for chunks), rubble feeds the dig phase

## Ideas list
- Pool Dig: pour the base and set forms, more yards (tight side access, a tree in the way, rock)
- Moto Track Builder: dirt bike tracks and ruts in the dirt

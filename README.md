# ClaudeinCloud
Experimenting w Claude in the cloud! Woot!

## Games

| Game | Folder | What it is |
|---|---|---|
| Pool Dig | [`pool-dig/`](pool-dig/index.html) | Excavator sim: dig a 33 × 16 ft backyard pool to grade (3 ft shallow to 6 ft deep), load the dump truck, and don't cut the sprinkler line. |
| Topping Out | [`topping-out/`](topping-out/index.html) | Tower crane sim on a downtown lot: fly columns, beams and decks from the laydown yard and build a steel frame floor by floor. Four floors tops out the job. |

Each game is one self-contained HTML file. It runs in any browser, including on a phone with touch sticks, and uses three.js r128 from cdnjs.

### Pool Dig controls
- **Phone:** left stick drives, right stick swings (left/right) and reaches (up/down), **DIG** scoops or dumps, **TRIM** shaves a thin layer.
- **Keyboard:** WASD drive · Q/E swing · R/F reach · Space dig/dump · T trim · H send truck · G grade view · Z/C rotate view · wheel zoom · M sound
- **Controller:** left stick drive · right stick swing/reach · A dig/dump · X trim · Y send truck · LB/RB rotate view

### Topping Out controls
- **Phone:** left stick swings the crane (left/right) and runs the trolley (up/down), right stick hoists (up/down) and looks around, **HOOK** picks up or sets, **TURN** rotates a beam 90°.
- **Keyboard:** A/D swing · W/S trolley · R/F or ↑/↓ hoist · Space hook · T turn · Z/C look around · wheel zoom · M sound
- **Controller:** left stick swing/trolley · right stick hoist/look · RT/LT hoist · A hook · X turn

## Skyscraper Sim plan
One downtown lot, played start to finish: wrecking-ball demolition → clear rubble → dig a 20 ft basement → pour the foundation → fly the steel with the tower crane. Built one playable phase at a time:
1. ✅ Tower crane steel erection (Topping Out)
2. Basement dig + foundation pour (reuse Pool Dig terrain and truck)
3. Wrecking-ball demolition (needs a physics engine for chunks), rubble feeds the dig phase

## Ideas list
- Pool Dig: pour the base and set forms, more yards (tight side access, a tree in the way, rock)
- Moto Track Builder: dirt bike tracks and ruts in the dirt

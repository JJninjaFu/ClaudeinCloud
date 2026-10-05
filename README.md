# ClaudeinCloud
Experimenting w Claude in the cloud! Woot!

## Games

| Game | Folder | What it is |
|---|---|---|
| Skydivin' 2 | [`skydivin2/`](skydivin2/index.html) | 4-way formation skydiving for up to 4 friends (bots fill the rest). Two jumpers off each skid of a helicopter at 13,500 ft, then lean forward and back (like the rider on Mineral Fork) to fly your slot, slide and match fall rate, and hold each formation for 3 seconds: Star, Line, Caterpillar, Diamond, Box, Accordion. Break off at 4,500 ft, track, pull, and see who lands closest to the X. |
| Survivin' Skydivin' | [`survivin-skydivin/`](survivin-skydivin/index.html) | Solo skydiving survival. Exit the plane on the green light, fly through rings in freefall, pull by 3,500 ft, then deal with what opens: line twists (kick out), streamers, pilot chute in tow and lineovers (cut away, pull the reserve). Wind, geese, other jumpers, trees, a pond and power lines. Flare and land on the X. Three jumps: Fun Jump, Cloud Hopper, Sunset Load. |
| Funnin' N Gunnin' | [`funnin-n-gunnin/`](funnin-n-gunnin/index.html) | Isometric army battle in the spirit of Running With Rifles, with Foxhole-style dirt. Red vs Blue, 25 soldiers a side (bots fill in around 1 to 4 players). Hold control points to bleed the other side's tickets. Every explosion leaves a crater, you can dig your own foxhole, and walls crumble block by block. Each side has 2 jeeps, an APC and a tank that bots crew and drive; hop in, take the gun, or steal the enemy's. |
| Mineral Fork | [`mineral-fork/`](mineral-fork/index.html) | Dirt bike hillclimb based on the brothers' Big Cottonwood ride: roll off the tailgate, climb the Trail 1154 switchbacks and the red scree pitch (Day 1), then the Red Face hillclimb (Day 2). Feather the throttle and work your body position or you spin out, slide back or loop out. |
| Pool Dig | [`pool-dig/`](pool-dig/index.html) | Excavator sim: dig a 33 × 16 ft backyard pool to grade (3 ft shallow to 6 ft deep), load the dump truck, and don't cut the sprinkler line. |
| Dig & Pour | [`foundation/`](foundation/index.html) | Foundation phase on the same downtown lot: dig a 33 × 33 ft basement 20 ft deep with a big laser-guided excavator (two haul trucks take turns), watch the rebar mat go in, then pump a 3 ft concrete mat. |
| Topping Out | [`topping-out/`](topping-out/index.html) | Steel erection on a downtown lot: fly columns, beams and decks from the laydown yard and build a frame floor by floor. Default gantry crane (no swing, climbs with the building) or a swinging tower crane. Four floors tops out the job. |

The root `index.html` is a game menu for GitHub Pages. Each game is one self-contained HTML file. It runs in any browser, including on a phone with touch sticks, and uses three.js r128 from cdnjs.

### Skydivin' 2 controls
- **Phone:** left stick leans you forward/back (drive toward or away from your slot) and turns you; right stick slides you sideways (left/right) and sets fall rate (up float, down sink). Big button pulls and flares.
- **Keyboard:** W/S lean · A/D turn · Q/E slide · R float · F sink · Space pull / flare · C camera (chase, top, helmet) · M sound
- **Controller:** left stick lean & turn · right stick slide & fall rate · A pull / flare · B camera
- **How it plays:** your see-through ghost marks your slot. Get in it, face the way it faces and keep the level bar green. When all four are docked, hold 3 seconds for the point. You carry momentum, so lean back early or you'll bump. *Easy docks* adds a gentle pull into the slot; *Pro* is tighter.
- **Jump with friends:** *Jump with friends*, enter your name, *Host a jump* and send the 4-letter code, or type a code and *Join*. Slots 1-2 sit on the left skid, 3-4 on the right. Empty slots are bots. Same PeerJS rooms as Mineral Fork.

### Survivin' Skydivin' controls
- **Phone:** touch anywhere on the left half for the stick. The big yellow button does the next thing: JUMP, PULL, KICK, CUT AWAY, RESERVE, hold to FLARE. Hold DIVE to go head down. CUT and RES buttons appear when you need them.
- **Keyboard:** WASD/arrows · Space big button · Shift dive · X cut away · R reserve · C camera · P pause · M sound
- **Controller:** left stick · A big button · RT dive / flare · LT brakes · X cut away · Y reserve · B camera · Start pause
- **Survival notes:** pull by 3,500 ft (audible altimeter beeps at 5,500 / 4,500 / 3,500 / 2,500). Decision altitude is 1,800 ft. The AAD fires your reserve at 750 ft if you're still in freefall, but it won't save you from a streamer. Land into the wind (windsock points downwind) and flare at about 10 ft; your shadow helps you judge it.

### Funnin' N Gunnin' controls
- **Phone:** left stick moves, right stick aims (push it to the edge to fire, aim assist helps), **NADE** throws where you aim, hold **DIG** to dig a foxhole where you stand, **DUCK** crouches, **SQUAD** grabs up to 4 nearby troops to follow you (tap again to dismiss), **TAKE** appears next to a dropped weapon.
- **Keyboard:** WASD move · mouse aim · click fire · right-click or G grenade · hold F dig · C crouch · E take weapon · Q squad · R reload · wheel zoom · P pause · M sound
- **Controller:** left stick move · right stick aim · RT fire · LB/RB grenade · A dig · B crouch · X take · Y squad · Start pause
- **Vehicles:** walk up and press **E** (phone: **GET IN**). You take the driver seat (a bot driver slides over); **T** or **SEAT** switches seats, so you can let a bot drive while you work the gun. Point the stick or WASD where you want to go and the vehicle steers there (pull back to reverse). The driver also aims and fires the gun when nobody is in the gunner seat. Jeep: fast, mounted MG, crew can be shot. APC: carries 6, heavy MG, drops troops at the point, and works as a mobile spawn once it leaves HQ. Tank: cannon (holding fire switches to the coax MG while it reloads), flattens trees, sandbags and walls. Rockets, grenades and tank shells hurt armor; bullets mostly don't. Run enemies over. Empty enemy vehicles can be stolen. Your squad climbs in with you. Craters and foxholes bog vehicles down. Wrecks burn and respawn at HQ after 30 seconds.
- **Classes:** Rifleman, Gunner (100-round belt, pins people down), Sniper (one-shot rifle, camera pulls out toward where you aim), Rocket (5 rockets that flatten walls, pistol when empty). Grenades and rockets refill while you stand on a point your side holds.
- **Play with friends (up to 4):** *Play with friends*, enter your name, *Host a battle* and send the 4-letter code, or type a code and *Join*. Everyone picks Red or Blue in the lobby (2v2, co-op, anything), bots fill both armies to 25. Friends can join a battle already in progress.

### Mineral Fork controls
- **Phone:** left stick steers (left/right) and shifts your body forward/back (up/down), slide up the **GAS** strip for more throttle, **BRAKE** button.
- **Keyboard:** W gas (hold Shift to feather at half) · S/Space brake · A/D or ←/→ steer · ↑/↓ body forward/back · R pick the bike up · C camera (chase, buddy filming, helmet) · P pause · M sound
- **Controller:** RT gas · LT brake · left stick steer and lean · Y reset · RB camera · Start pause
- **Ride with friends (up to 4):** tap *Ride with friends*, enter your name, and either *Host a race* (you get a 4-letter room code to send the group) or type a code and *Join*. The host picks the day and starts the race; everyone gets the same countdown, sees each other's bikes live (no collisions), and gets a standings board and finish results. Uses PeerJS (loaded only when you open multiplayer); the host's browser relays everyone. Some cell networks block direct connections, so Wi-Fi helps if someone can't join.

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

## Skyscraper Sim plan
One downtown lot, played start to finish: wrecking-ball demolition → clear rubble → dig a 20 ft basement → pour the foundation → fly the steel with the tower crane. Built one playable phase at a time:
1. ✅ Steel erection (Topping Out), gantry + tower crane. The tower crane's swing physics get reused for the wrecking ball.
2. ✅ Basement dig + foundation pour (Dig & Pour)
3. Wrecking-ball demolition (needs a physics engine for chunks), rubble feeds the dig phase

## Ideas list
- Skydivin' 2: bigger ways (8-way with bots), more formations, video judge replay, wingsuit mode
- Pool Dig: pour the base and set forms, more yards (tight side access, a tree in the way, rock)
- Moto Track Builder: dirt bike tracks and ruts in the dirt
- Funnin' N Gunnin' v3: helicopters, artillery and anti-air call-ins unlocked by rank.

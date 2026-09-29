# Hard Hat Heavy (KSP 1.12, all stock)

A 30-part, 3-kerbal crew rocket with six stages of rowdiness. It launches on a Mainsail plus four Kickbacks, has a working launch escape tower, and has about 6.9 km/s of vacuum delta-v. That's enough to reach orbit and then take the Poodle upper stage to the Mun or Minmus and home.

## Install
Copy `Hard Hat Heavy.craft` into `<KSP folder>/Ships/VAB/` (or `<KSP folder>/saves/<your save>/Ships/VAB/` for one save), then load it in the VAB. In career mode you need every part unlocked.

## Stages (in firing order)
| KSP stage | What happens |
|---|---|
| 5 | Liftoff: Mainsail + 4 Kickback SRBs (Kickbacks limited to 80%). Liftoff TWR is about 1.9. |
| 4 | Kickbacks burn out after about 75 s. TT-70 decouplers kick them loose, and 8 Sepratrons fire nose-up to shove their tops outward and slow them down. |
| 3 | Jettison the launch escape tower. It fires and flies itself off. |
| 2 | Drop the core stage and light the Poodle. |
| 1 | Pod separation (before reentry). |
| 0 | 4 radial chutes. |

**Abort (Backspace):** shuts down the Mainsail and Poodle, blows the pod off the stack, and fires the escape tower to yank the crew clear. After that, stage off the tower and the chutes.

## Flying it
- Turn SAS on. Start the gravity turn at 60–80 m/s and aim for about 45° by 10 km.
- The core (Mainsail) has only about 0.8 km/s left after the Kickbacks drop. Stage it as soon as it runs dry, around 30–40 km up.
- The Poodle finishes the climb to orbit and still has about 3.4 km/s. That's enough for a Mun or Minmus orbit and the trip home.
- There's no heat shield, so come home from the Mun with a shallow reentry (periapsis around 30 km). Drop the Poodle stage first.

Rough delta-v: boost about 2,250 m/s, core about 770 m/s, Poodle about 3,850 m/s.

## Regenerating
`tools/gen.py` builds the file from stock part blocks in kRPC's 1.12.5 test craft (see the docstring). `tools/check.py` checks links, symmetry, and full tanks.

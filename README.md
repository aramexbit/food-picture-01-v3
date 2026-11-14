# food-picture-01 v3 — Midnight Tonkotsu Ramen

[![make.fun](https://make.fun/badge.svg)](https://make.fun/c/food-picture-01)

Entry for the [make.fun](https://make.fun) **food-picture-01** bounty
("Make the best-looking food picture", $250, top 100 share the prize).

## The picture

Midnight tonkotsu ramen in near-darkness: a single warm golden light from
the upper left falls on a black ceramic bowl, wooden chopsticks lifting a
tall cascade of glossy steaming noodles high above the bowl, the noodles
catching the light. Creamy tonkotsu broth with glinting chili oil, fanned
chashu slices, a halved jammy egg with its golden yolk, nori and green
onions. Thin steam curls up into the black background. No text in the image.

This is version 3 of the entry. Version 1 ("noodles lifted high with
chopsticks", slate top-down) ranked 1,049 with an 87.1% judge win rate;
version 2 (dramatic close-up, black chopsticks, black speckled bowl, warm
bokeh) ranked 378 with a 91.6% win rate. v3 goes for a darker, more
cinematic frame — one light, deep shadows, a taller noodle cascade — a new
composition, not a copy of v2 or of any other entry.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` beside
it to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), byte for byte,
then verifies the copy's sha256 matches the source, so the judge sees
exactly these bytes. Deterministic: the same input always produces the
same output.

Run it like the grader does:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entrypoint (copies `entry.png` to the output dir, verifies sha256)
- `entry.png` — the picture (683x1024 PNG, 736,290 bytes)
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.

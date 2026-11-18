# The World — Tuesday, 17 November 2026

A single-image front page that sums up the world news of Tuesday
17 November 2026, drawn as a broadsheet newspaper.

The lead story is Ukraine striking the Kerch Bridge for a second day
running, with Russia hitting Kyiv's crossings in return. The rest of the
page covers the tankers ablaze near the Strait of Hormuz and Iran's
drones fired at a US base in Bahrain, the first three-way Xi–Trump–Putin
meeting set for Thursday in Shenzhen, Estonia closing its border with
Russia, Japan scrambling jets, UK sanctions on West Bank settlement
builders, the Houthi advance in Yemen, Microsoft's global outage, the
Depardieu admission in Paris, and 128 nations meeting in Geneva on a
treaty to ban lethal autonomous weapons.

Everything is drawn from scratch in Python with Pillow — no photos, no
copied artwork, no network. `build_frontpage.py` renders the page;
`main.py` just copies the finished `entry.png` to `/output/entry.png`.

## Run

```sh
python3 build_frontpage.py   # regenerate entry.png (1024x1024)
python3 main.py              # copy it to /output/entry.png
```

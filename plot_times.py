from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import json
import sys

import matplotlib.pyplot as plt
plt.style.use("dark_background")

# -----------------------------------------------

json_fname = "board_45291.json"
player_id = "45291"

tz = ZoneInfo("America/Mexico_City")
start_times = {
  5: datetime(2020, 12, 4, 23, 14, tzinfo=tz),
  14: datetime(2020, 12, 13, 23, 28, tzinfo=tz),
  25: datetime(2020, 12, 25, 9, 5, tzinfo=tz)
}

# -----------------------------------------------

with open(json_fname) as f:
  data = json.load(f)
times = data["members"][player_id]["completion_day_level"]

times_stars = []
for day in range(1, 25+1):
  if day in start_times:
    start = start_times[day]
  else:
    start = datetime(2020, 12, day, 23, tzinfo=tz) - timedelta(days=1)
  start_ts = start.timestamp()
  ts = []
  for star in [1, 2]:
    solve_ts = float(times[str(day)][str(star)]["get_star_ts"])
    elapsed = solve_ts - start_ts
    # print(day, star, elapsed)
    ts.append(elapsed/60)
  times_stars.append(ts)

times_star1, times_star2 = zip(*times_stars)

w = 0.3
g = 0.03
xs = range(1, 25+1)
xs1 = [x-w/2-g for x in xs]
xs2 = [x+w/2+g for x in xs]

plt.figure(figsize=(14,4))
plt.bar(xs1, times_star1, width=w, color="#d3e2ec", label="Part 1")
plt.bar(xs2, times_star2, width=w, color="#ffda59", label="Part 2")

plt.xlabel("Day")
plt.ylabel("Minutes")
plt.title("Advent of Code 2020 solve times")

plt.legend(loc="upper left")
plt.xticks(xs)
plt.yticks([0, 30, 60, 90, 120, 150, 180])
plt.xlim(0.25, 25.75)
plt.grid(ls=":", color="0.3")
plt.gca().set_axisbelow(True)
plt.tight_layout()

if "--save" in sys.argv:
  fname = "solve_times.png"
  plt.savefig(fname)
  print("Wrote", fname)
else:
  plt.show()

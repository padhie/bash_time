# timer
Scripts for time issues


# General
## Required Tools
* `Python3` or `docker compose`


# Usage
## Tracking
Run `run.py` at the startup.
Alternative you can push every minute into the tracking file for the current day.

## Statistic
Run `statistic.py` and give the mode as argument(run script without argument to see the available modes),
### Examples
```bash
$ python3 statistic.py week-table 
Week 21
Start: 22.05.2023
End: 28.05.2023

+-----------------------------------------------------+
|    Date    | Tracked Time | Break Time | Total Time |
+-----------------------------------------------------+
| 22.05.2023 |    00h 00m   |     00m    |   00h 00m  |
| 23.05.2023 |    18h 14m   |     60m    |   19h 14m  |
| 24.05.2023 |    18h 56m   |     60m    |   19h 56m  |
| 25.05.2023 |    18h 56m   |     60m    |   19h 56m  |
| 26.05.2023 |    09h 02m   |     60m    |   10h 02m  |
| 27.05.2023 |    00h 00m   |     00m    |   00h 00m  |
| 28.05.2023 |    00h 00m   |     00m    |   00h 00m  |
+-----------------------------------------------------+
|    Total   |    65h 08m   |   04h 00m  |   69h 08m  |
+-----------------------------------------------------+
```

```bash
$ python3 statistic.py month-table        
Month May
Start: 01.05.2023
End: 31.05.2023

+-----------------------------------------------+
| Week | Tracked Time | Break Time | Total Time |
+-----------------------------------------------+
|  18  |    37h 03m   |     60m    |   38h 03m  |
|  19  |    48h 35m   |     60m    |   49h 35m  |
|  20  |    00h 13m   |     00m    |   00h 13m  |
|  21  |    48h 58m   |     60m    |   49h 58m  |
|  22  |    00h 00m   |     00m    |   00h 00m  |
+-----------------------------------------------+
| Total|   134h 49m   |   03h 00m  |  137h 49m  |
+-----------------------------------------------+
```

```bash
$ python3 statistic.py last-weeks-table 4 
Start: 24.04.2023
End: 28.05.2023

+-----------------------------------------------+
| Week | Tracked Time | Break Time | Total Time |
+-----------------------------------------------+
|  17  |    33h 39m   |     60m    |   34h 39m  |
|  18  |    37h 03m   |     60m    |   38h 03m  |
|  19  |    48h 35m   |     60m    |   49h 35m  |
|  20  |    00h 13m   |     00m    |   00h 13m  |
|  21  |    49h 00m   |     60m    |   50h 00m  |
+-----------------------------------------------+
| Total|   168h 30m   |   04h 00m  |  172h 30m  |
+-----------------------------------------------+
```

# Configuration
## break
Define a time (after this time the breaktime will be added) and break (how long is the breaktime).  
Both information are in minutes (e.g. 6h = 6*60 = 360).   
Example: 
```yaml
break:
  -
    time: 360
    break: 30
  -
    time: 480
    break: 60
```
The breaktime will be subtract from the total time. This means: the tool run 10h in total - 30m = 9:30h in the output.   



# Example Configuration
## Conky
```
${font Entopia:bold:size=12}${color 084085}Time Tracking ${hr 2}${font}
${offset 15}${color FFFDE2}System Uptime ${alignr}$color $uptime
${offset 15}${color FFFDE2}First Daily Login ${alignr}$color ${exec python3 /home/patrickzemke/projects/timer/statistic.py daily-login-date}
${offset 15}${color FFFDE2}First Daily Login since ${alignr}$color ${exec python3 /home/patrickzemke/projects/timer/statistic.py daily-login-since}
${offset 15}${color FFFDE2}Week Time ${alignr}$color ${exec python3 /home/patrickzemke/projects/timer/statistic.py week-single}

```

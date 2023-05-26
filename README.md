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

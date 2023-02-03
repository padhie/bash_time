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


# Example Configuration
## Conky
```
${font Entopia:bold:size=12}${color 084085}Time Tracking ${hr 2}${font}
${offset 15}${color FFFDE2}System Uptime ${alignr}$color $uptime
${offset 15}${color FFFDE2}First Daily Login ${alignr}$color ${exec python3 /home/patrickzemke/projects/timer/statistic.py daily-login-date}
${offset 15}${color FFFDE2}First Daily Login since ${alignr}$color ${exec python3 /home/patrickzemke/projects/timer/statistic.py daily-login-since}
${offset 15}${color FFFDE2}Week Time ${alignr}$color ${exec python3 /home/patrickzemke/projects/timer/statistic.py week-single}

```

# bash_time
Scripts for time issues

# General
Tracking Files Format: `{MONTH NUMBER WITH LEADING ZERO}_{DAY OF MONTH WITH LEADING ZERO}.txt`   


# Install

## Tracking
Ad `run.sh` to your startup programms or create a cronjob witch is push every minute into the tracking file for the currect day.  


# Example Configuration
## Conky
```
${font Entopia:bold:size=12}${color 084085}Time Tracking ${hr 2}${font}
${offset 15}${color FFFDE2}System Uptime ${alignr}$color $uptime
${offset 15}${color FFFDE2}First Daily Login ${alignr}$color ${exec /home/root/bash_time/first_daily_login_date.sh}
${offset 15}${color FFFDE2}First Daily Login since ${alignr}$color ${exec /home/root/bash_time/first_daily_login_since.sh}
```

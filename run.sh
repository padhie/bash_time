#!/bin/bash

echo "Press [CTRL+C] to stop..."

CURRENT_MONTH=$(date +%m)
CURRENT_DAY=$(date +%d)

DAY_FILE="${CURRENT_MONTH}_${CURRENT_DAY}.txt"
touch "${DAY_FILE}"

echo $CURRENT_MONTH
echo $CURRENT_DAY
echo $DAY_FILE

while :
do
	date +%s
	echo "$(date +%s)" >> $DAY_FILE
	sleep 1
done

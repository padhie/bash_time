#!/bin/bash


CURRENT_MONTH=$(date +%m)
CURRENT_DAY=$(date +%d)

DAY_FILE="data/${CURRENT_MONTH}_${CURRENT_DAY}.txt"
touch "${DAY_FILE}"

while :
do
	date +%s
	echo "$(date +%s)" >> $DAY_FILE
	sleep 60
done

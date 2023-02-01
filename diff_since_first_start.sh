#!/bin/bash

echo "Press [CTRL+C] to stop..."

CURRENT_MONTH=$(date +%m)
CURRENT_DAY=$(date +%d)
CURRENT_TIMESTAMP=$(date +%s)

DAY_FILE="${CURRENT_MONTH}_${CURRENT_DAY}.txt"
if [ ! -f /path/to/file ]
then
    	touch "${DAY_FILE}"
	echo $CURRENT_TIMESTAMP >> $DAY_FILE
fi

FIRST_TIME=$(head -n 1 $DAY_FILE)
DIFF=$(( $CURRENT_TIMESTAMP - $FIRST_TIME))

echo $DIFF

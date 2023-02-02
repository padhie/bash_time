#!/bin/bash

CURRENT_MONTH=$(date +%m)
CURRENT_DAY=$(date +%d)

DAY_FILE="data/${CURRENT_MONTH}_${CURRENT_DAY}.txt"

if [ ! -f /path/to/file ]
then
        touch "${DAY_FILE}"
        echo $(date +%s) >> $DAY_FILE
fi

echo $DAY_FILE

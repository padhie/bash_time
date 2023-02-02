#!/bin/bash

CURRENT_MONTH=$(date +%m)
CURRENT_DAY=$(date +%d)
CURRENT_TIMESTAMP=$(date +%s)

DAY_FILE="data/${CURRENT_MONTH}_${CURRENT_DAY}.txt"
if [ ! -f /path/to/file ]
then
    	touch "${DAY_FILE}"
	echo $CURRENT_TIMESTAMP >> $DAY_FILE
fi

FIRST_TIME=$(head -n 1 $DAY_FILE)
SECONDS=$(( $CURRENT_TIMESTAMP - $FIRST_TIME))

DAYS=0
HOURS=0
MINUTES=0

#echo $SECONDS

if [ $SECONDS -gt 86400 ];
then
	echo -n " "
	DAYS=$(( $SECONDS / 86400 ))
	SECONDS=$(( $SECONDS-($DAYS*86400) ))
	echo -n "${DAYS}d"
fi;

if [ $SECONDS -gt 3600 ];
then
	echo -n " "
	HOURS=$(( $SECONDS / 3600 ))
	SECONDS=$(( $SECONDS-($HOURS*3600) ))
	if [ $HOURS -lt 10 ];
	then
		echo -n "0"
	fi;
	echo -n "${HOURS}h"
fi;

if [ $SECONDS -gt 60 ];
then
	echo -n " "
	MINUTES=$(( $SECONDS / "60"  ))
	SECONDS=$(( $SECONDS-($MINUTES*60) ))
	if [ $MINUTES -lt 10 ];
	then
		echo -n "0"
	fi;
	echo -n "${MINUTES}m"
fi;

echo -n " "
if [ $SECONDS -lt 10 ];
then
	echo -n "0"
fi;
echo -n "${SECONDS}s"

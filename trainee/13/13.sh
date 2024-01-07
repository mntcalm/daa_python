#!/bin/sh
if [ ! -z "$2" ]
then
  echo "Hello, "$1" "$2"! Nice to see you here!"
else
  echo " Please run this script with 2 arguments like: ./13.sh Name Surname"
fi

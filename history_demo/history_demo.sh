#!/usr/bin/env bash

if [ $# -eq 0 ]
  then
    echo "No arguments supplied, please specify a path for pytest to discover tests as an argument."
    echo "Options:"
    echo "-n - a number of test runs in (optional)."
    echo "-r - a number of retries for failed tests (optional)."
    exit 1
fi

test_runs=2
retries=1

while getopts ":n:r:" opt; do
  case $opt in
    n) test_runs="$OPTARG"
    ;;
    r) retries="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
        exit 1
    ;;
  esac
done

for i in `seq 1 ${test_runs}`; do
   pytest "$1" --alluredir "/tmp/allure-results${i}" --reruns ${retries}
   if [ -d "/tmp/allure-report" ]; then
        cp -r "/tmp/allure-report/history" "/tmp/allure-results${i}"
   fi
   allure generate "/tmp/allure-results${i}" -o "/tmp/allure-report" -c
   rm -r "/tmp/allure-results${i}"
done

allure open "/tmp/allure-report"
#!/usr/bin/env bash

print_usage_and_exit () {
    echo "Usage: sh history_demo.sh *path to discover python tests* -n=2 -r=1"
    echo "Options:"
    echo "-n - a number of test runs to do (optional, default = 2)."
    echo "-r - a number of retries for failed tests (optional, default = 1)."
    exit $1
}

if [ $# -eq 0 ]
  then
    echo "No arguments supplied, please specify a path for pytest to discover tests as an argument."
    print_usage_and_exit 1
fi

test_runs=2
retries=1

while [ "$1" != "" ]; do
    PARAM=`echo $1 | awk -F= '{print $1}'`
    VALUE=`echo $1 | awk -F= '{print $2}'`
    if [[ $1 != -* ]]; then
        shift
        continue
    fi
    case ${PARAM} in
            -h | --help)
                print_usage_and_exit 0
                ;;
            -n )
                test_runs=$VALUE
                ;;
            -r)
                retries=$VALUE
                ;;
            *)
            echo "ERROR: unknown parameter \"$PARAM\""
            print_usage_and_exit 1
                        ;;
    esac
    shift
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
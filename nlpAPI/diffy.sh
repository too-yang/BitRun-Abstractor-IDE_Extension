#!/usr/bin/env bash
echo "Send some traffic to your Diffy instance"
declare -a endpoints=("success" "noise" "regression" "noisy_regression")
declare -a values=("mixpanel" "twitter" "airbnb" "paytm" "baidu")
for i in {1..10}
do
    for k in "${endpoints[@]}"
    do
        for v in "${values[@]}"
        do
            sleep 0.1
            curl -s -i -H "Canonical-Resource : endpoint-$k" http://localhost:8880/$k?value=$v > /dev/null
        done
    done
done

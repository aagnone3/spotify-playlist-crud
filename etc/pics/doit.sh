#!/usr/bin/env bash
set -eou pipefail

i=0
while read fn; do
    echo $i: "$fn"
    i=$((i + 1))
    unzip -d d$i "$fn"
done < files

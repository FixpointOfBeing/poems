#!/bin/bash

if [ $# -eq 0 ]; then
    echo "用法: $0 <filename>"
    exit 1
fi

filename="$1"

datestr=$(date +%Y-%m-%d | sed 's/-0\([1-9]\)/-\1/g')

output="${filename}_${datestr}.txt"

touch "$output"

echo "已生成文件: $output"

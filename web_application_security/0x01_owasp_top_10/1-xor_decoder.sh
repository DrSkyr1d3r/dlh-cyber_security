#!/bin/bash
mask=$(echo "${1#\{xor\}}" | base64 -d)
key=$(printf "%d" "'_")
i=0

while [ "$i" -lt "${#mask}" ]
do
	char="${mask:i:1}"
	ascii=$(printf "%d" "'$char")
	val=$((ascii ^ key))
	octal=$(printf '%03o' "$val")
	printf "\\$octal"
	i=$((i + 1))
done
echo

#!/bin/bash
mask=$(echo "${1#\{xor\}}" | base64 -d)
key=$(printf "%d" "'_")
for ((i=0; i<${#mask}; i++)); do
	char="${mask:i:1}"
	ascii=$(printf "%d" "'$char")
	val=$((ascii^key))
	printf "\\$(printf '%03o' "$val")"
done

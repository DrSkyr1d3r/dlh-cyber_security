#!/bin/bash
mask=$(echo "${1#\{xor\}}" | base64 -d)
key=$(printf "%d" "'_")
i=0

while [ "$i" -lt "${#mask}" ]
do
	char="${mask:i:1}"
	ascii=$(printf "%d" "'$char")
	a="$ascii"
	b="$key"
	val=0
	factor=1
	bit=0

	while [ "$bit" -lt 8 ]
	do
		abit=$((a % 2))
		bbit=$((b % 2))
		xorbit=$((abit + bbit))

		if [ "$xorbit" -eq 1 ]
		then
			val=$((val + factor))
		fi

		a=$((a / 2))
		b=$((b / 2))
		factor=$((factor * 2))
		bit=$((bit + 1))
	done

	octal=$(printf "%03o" "$val")
	printf "%b" "\\$octal"
	i=$((i + 1))
done
echo

#!/bin/bash
hping3 -c 100 -d 1460 -S -p 80 "$1"

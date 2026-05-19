#!/bin/bash
john --wordlist=/usr/share/wordlists/rockyou.txt --format=RAW-MD5 "$1"

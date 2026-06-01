#!/bin/bash
nmap -sn  -PS22,80,44, $1

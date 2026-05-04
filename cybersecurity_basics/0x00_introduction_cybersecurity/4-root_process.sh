#!/bin/bash
ps aux | awk -v user="root" '$1 == user' | grep -v '\[.*\]'

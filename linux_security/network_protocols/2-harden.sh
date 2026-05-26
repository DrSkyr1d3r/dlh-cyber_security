#!/bin/bash
find / -type d -perm -002 -print  -exec chmod go-w {} \; 2>/dev/null

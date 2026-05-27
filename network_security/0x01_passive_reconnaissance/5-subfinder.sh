#!/bin/bash
subfinder -d $1 -oI -ip -nW -silent | awk '{print $1","$2}' > $1.txt

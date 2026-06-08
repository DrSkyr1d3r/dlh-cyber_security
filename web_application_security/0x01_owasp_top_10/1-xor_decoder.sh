#!/bin/bash
echo "${1#\{xor\}}" | base64 -d | perl -pe 's/(.)/chr(ord($1) ^ ord('_'))/ge'

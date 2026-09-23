#!/bin/bash
# Count lines, words, and characters. Input from $1, else stdin, else a sample.
if [ "$#" -gt 0 ]; then
  input="$1"
else
  input="$(cat)"
fi
if [ -z "$input" ]; then
  input=$'first line\nsecond line\nthird line'
fi
printf 'lines: %s\n' "$(printf '%s\n' "$input" | wc -l | tr -d ' ')"
printf 'words: %s\n' "$(printf '%s' "$input" | wc -w | tr -d ' ')"
printf 'chars: %s\n' "$(printf '%s' "$input" | wc -c | tr -d ' ')"
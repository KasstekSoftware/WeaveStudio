#!/bin/bash
# Uppercase the input. Input from $1, else stdin, else a sample.
if [ "$#" -gt 0 ]; then
  input="$1"
else
  input="$(cat)"
fi
if [ -z "$input" ]; then
  input="hello from weave studio"
fi
printf '%s\n' "$input" | tr '[:lower:]' '[:upper:]'
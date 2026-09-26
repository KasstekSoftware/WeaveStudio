#!/bin/bash
# Print the message passed as the first argument, or a default.
if [ "$#" -gt 0 ]; then
  printf '%s\n' "$1"
else
  printf '%s\n' "Weave flow reached the Print step."
fi
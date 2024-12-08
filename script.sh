#!/bin/bash

echo "Introdu un numar:"
read num

# Improved validation and error handling
if [[ ! "$num" =~ ^-?[0-9]+$ ]]; then
    echo "Input invalid! Te rog introdu un numar întreg."
    exit 1
fi

# Use Python inline to check even/odd, with improved error handling
result=$(python3 -c "
try:
    num = int('$num')
    print('par' if num % 2 == 0 else 'nu e par')
except ValueError:
    print('Eroare: Introdu un numar valid')
")

echo "$result"




#!/bin/bash

echo "Script bash - introdu un numar"
read nun
result = $(python - <<EOF
num = int("$nun")
if num % 2 == 0:
	print("e par")
else:
	print("nu e par")
EOF
)

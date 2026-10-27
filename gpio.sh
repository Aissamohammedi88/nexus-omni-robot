#!/bin/bash
# gpio.sh — Simulation GPIO 28 pins (comme Raspberry Pi)
# Usage : ./gpio.sh mode <pin> <in|out>
# ./gpio.sh write <pin> <0|1>
# ./gpio.sh read <pin>
# ./gpio.sh list

BASE="$(dirname "$0")"

case "${1:-}" in
mode)
echo "$3" > "$BASE/pins/gpio$2/direction"
echo "[GPIO] pin $2 → mode $3"
;;
write)
echo "$3" > "$BASE/pins/gpio$2/value"
echo "[GPIO] pin $2 ← valeur $3"
;;
read)
V=$(cat "$BASE/pins/gpio$2/value" 2>/dev/null)
echo "[GPIO] pin $2 = $V"
;;
list)
echo "== GPIO 28 pins =="
for i in $(seq 0 27); do
D=$(cat "$BASE/pins/gpio$i/direction" 2>/dev/null)
V=$(cat "$BASE/pins/gpio$i/value" 2>/dev/null)
echo " gpio$i : $D = $V"
done
;;
*)
echo "Usage : $0 {mode|write|read|list}"
;;
esac

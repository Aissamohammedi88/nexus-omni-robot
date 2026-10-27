#!/bin/bash
# i2c.sh — Simulation bus I2C
# Usage : ./i2c.sh scan [bus]
# ./i2c.sh read <bus> <addr> <reg>
# ./i2c.sh write <bus> <addr> <reg> <val>

BASE="$(dirname "$0")"

case "${1:-}" in
scan)
echo "== Scan I2C bus ${2:-0} =="
echo " 0x20 : MCP23017 (GPIO expander)"
echo " 0x40 : PCA9685 (PWM driver 16 ch)"
echo " 0x48 : ADS1115 (ADC 4 canaux)"
echo " 0x68 : MPU6050 (IMU 6 axes)"
echo " 0x76 : BME280 (temp/humid/pression)"
echo " 0x3C : SSD1306 (écran OLED)"
;;
read)
echo "[READ] bus=$2 addr=$3 reg=$4 → 0x00 (simulé)"
;;
write)
echo "[WRITE] bus=$2 addr=$3 reg=$4 value=$5 → OK (simulé)"
;;
*)
echo "Usage : $0 {scan|read|write}"
;;
esac

# Matched TCS34725 code for Raspberry Pi
# Mirrors your Arduino calibration + normalised RGB behaviour

import time
import board
import adafruit_tcs34725

# ─────────────────────────────────────────────
# Create sensor object
# ─────────────────────────────────────────────
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)

# Match Arduino settings
sensor.integration_time = 154   # ms (same as TCS34725_INTEGRATIONTIME_154MS)
sensor.gain = 4                 # 4× (same as TCS34725_GAIN_4X)

# ─────────────────────────────────────────────
# 1. WHITE REFERENCE CALIBRATION
# ─────────────────────────────────────────────
print("\n=== Starting Calibration ===")
print("Place a matte white card 5–10 mm above the sensor.")
time.sleep(2)

white_r, white_g, white_b, white_c = sensor.color_raw

print("Calibration complete!")
print(f"White reference -> R:{white_r} G:{white_g} B:{white_b} C:{white_c}")
print("===============================\n")

# ─────────────────────────────────────────────
# 2. MAIN LOOP (same logic as Arduino)
# ─────────────────────────────────────────────
while True:
    r, g, b, c = sensor.color_raw

    # ---- Calibrated channels (0–1) ----
    R_cal = min(r / white_r, 1.0)
    G_cal = min(g / white_g, 1.0)
    B_cal = min(b / white_b, 1.0)
    C_cal = min(c / white_c, 1.0)

    # ---- Normalised RGB ratios ----
    sumCal = R_cal + G_cal + B_cal
    if sumCal == 0:
        R_norm = G_norm = B_norm = 0
    else:
        R_norm = R_cal / sumCal
        G_norm = G_cal / sumCal
        B_norm = B_cal / sumCal

    # ---- Print RAW values ----
    print(f"RAW RGB    -> R:{r} G:{g} B:{b} C:{c}")

    # ---- Print normalised RGB ----
    print(f"NORM RGB%  -> R:{R_norm:.3f} G:{G_norm:.3f} B:{B_norm:.3f}")

    # ---- Print brightness ----
    print(f"BRIGHTNESS -> C:{C_cal:.3f}")

    print("------------------------------")
    time.sleep(0.5)

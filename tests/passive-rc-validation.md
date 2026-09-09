# Passive RC Low-Pass Filter Validation

## Circuit

- Resistor: 56 kΩ nominal
- Capacitor: 10 nF nominal (`103`)
- Filter type: first-order passive RC low-pass
- Expected cutoff frequency:

  fc = 1 / (2πRC) ≈ 284 Hz

## Expected Response

- Low-frequency gain: approximately 0 dB
- Gain at cutoff: approximately -3 dB
- Phase at cutoff: approximately -45 degrees
- High-frequency slope: approximately -20 dB/decade

## Baseline Procedure

1. Verify the RC circuit wiring with DAQ power/output disabled.
2. Run the current VI without modifying its block diagram.
3. Record the sample rate, excitation amplitude, frequency range, and sample count.
4. Save the measured magnitude and phase data.
5. Compare the measured cutoff with the expected 284 Hz value.
6. Check the output waveform for clipping or excessive noise.

## Privacy

Only sanitized numerical measurements will be placed in `data/examples`. Device serial numbers, usernames, institutional paths, and private laboratory documents must not be included.

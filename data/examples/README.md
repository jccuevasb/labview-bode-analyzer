# Passive RC Baseline Dataset

This directory contains sanitized loopback and DUT measurements from a first-order passive RC low-pass filter.

## Measurement Configuration

- Resistor: 56 kΩ nominal
- Capacitor: 10 nF nominal
- Theoretical cutoff frequency: 284.21 Hz
- Excitation: 1.00 V sine wave
- Frequency sweep: 1–1000 Hz in 1 Hz increments
- Sample rate: 40,000 samples/s
- Samples per frequency: 8,000
- Acquisition duration per frequency: 0.2 s

## Files

- `passive_rc_loopback.tsv`: Direct output-to-input loopback measurement
- `passive_rc_dut.tsv`: Measurement through the passive RC filter

## Columns

- `Freq`: Excitation frequency in hertz
- `PhiChirp`: Generated-waveform phase in degrees
- `PhiRC`: Acquired-waveform phase in degrees
- `AChirp`: Generated-waveform amplitude in volts
- `ARC`: Acquired-waveform amplitude in volts

The `PhiRC` and `ARC` names are retained from the original VI for compatibility. They represent the acquired signal in both files.

## Baseline Limitations

The loopback and DUT measurements were recorded in separate runs. The fixed 0.2-second acquisition contains fewer than three cycles below 15 Hz, reducing low-frequency phase reliability. An isolated phase outlier is visible at 11 Hz. This dataset is retained as an honest baseline for subsequent improvements.
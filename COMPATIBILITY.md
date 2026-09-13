# LabVIEW 2025 Q3 32-bit Version

This branch contains the compatibility version of the Bode Frequency
Response Analyzer.

## Required environment

- LabVIEW 2025 Q3, 32-bit
- Tested patch: 25.3.2f2
- NI-DAQmx with LabVIEW 2025 32-bit support
- NI USB-6212

## Relationship to the main version

The `main` branch contains the LabVIEW 2026 64-bit development version.

This compatibility branch contains VIs saved and validated for LabVIEW
2025 Q3 32-bit. Functional changes should first be developed and tested
on `main`, then deliberately backported and revalidated on this branch.

## Validated functions

- USB-6212 analog output and synchronized input acquisition
- Passive-filter gain and phase measurement
- One-sample channel-sequencing phase correction
- Phase wrapping into [-180 degrees, 180 degrees)
- Configurable results directory and filename
- Warm-up measurement exclusion
- Real-time gain and phase plots

## Current limitation

Active op-amp filter operation has not yet been validated.

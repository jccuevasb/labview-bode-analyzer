# LabVIEW Bode Frequency Response Analyzer

A LabVIEW and NI-DAQmx application for measuring the magnitude and phase response of analog electronic filters using an NI USB-6212 data-acquisition device.

## Current Status

The current baseline performs frequency-response measurements for a passive low-pass filter using generated excitation, synchronized acquisition, loopback calibration, and tone measurements.

Active-filter support is under development and has not yet been validated.

## Project Goals

- Measure filter input and output signals using synchronized acquisition
- Generate Bode magnitude and phase plots
- Support passive and active filter circuits
- Use logarithmically spaced test frequencies
- Account for settling time and acquisition quality
- Compare experimental measurements with theoretical predictions
- Detect clipping, weak signals, and invalid measurements
- Export sanitized example data for reproducible analysis

## Hardware

- NI USB-6212 multifunction DAQ
- Passive RC filter components
- Active op-amp filter components
- External op-amp power supply when required

## Software

- LabVIEW 2026
- NI-DAQmx
- NI Measurement & Automation Explorer

## Repository Structure

- `src/`: LabVIEW source files
- `analysis/`: Data-analysis and validation scripts
- `data/examples/`: Sanitized example measurements
- `docs/`: Public diagrams and documentation
- `tests/`: Validation procedures and expected results

## Development Roadmap

1. Preserve and validate the existing passive-filter implementation
2. Record a passive-filter baseline
3. Improve frequency selection and settling behavior
4. Add simultaneous input/output acquisition
5. Validate active-filter measurements
6. Add theoretical-response comparison and quality checks
7. Document the final experimental system

## Privacy

This public repository excludes credentials, institutional paths, device serial numbers, private documentation, and unsanitized experimental data.

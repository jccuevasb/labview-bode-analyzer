# NI USB-6212 Phase Correction

## Observed behavior

A direct two-channel loopback measurement showed a phase difference that
increased approximately linearly with frequency. Changing the acquisition
sample rate showed that the apparent delay scaled approximately as one
sample interval.

Tests using the same waveform array as the input to both Tone Measurements
VIs produced approximately 0 dB and 0 degrees. Therefore, the systematic
phase shift originated in the two-channel acquisition and channel-reading
sequence rather than in the Tone Measurements calculations.

## Correction

The application first calculates the raw phase difference as

    dPhi_raw = Phi_DUT - Phi_reference

For the current channel order, the one-sample correction is

    dPhi_corrected = dPhi_raw - 360*f/Fs

where:

- f is the current excitation frequency in Hz.
- Fs is the actual acquisition sample rate in samples per second.
- 1/Fs represents the observed one-sample relative delay.

After applying the correction, the result is wrapped into the interval
[-180 degrees, 180 degrees).

## Validation

The correction was validated with:

1. A direct two-channel loopback.
2. A passive first-order RC low-pass filter.
3. Comparison between the measured -3 dB frequency and the expected
   approximately -45 degree phase at cutoff.

The corrected RC-filter data showed approximately -45 degrees at the
measured -3 dB frequency, demonstrating consistency between the measured
gain and phase.

## Limitations

This is a correction for the current USB-6212 acquisition configuration and
channel order. It is not a correction for the device under test.

The calibration should be repeated if:

- The input-channel order changes.
- The DAQ device changes.
- The acquisition or indexing logic changes.
- A different reference channel is selected.
- The definition of the phase difference is reversed.

Random isolated phase spikes are not corrected by this expression. Those
require settling, measurement-quality checks, or outlier rejection.

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
LOOPBACK_FILE = ROOT / "data" / "examples" / "passive_rc_loopback.tsv"
DUT_FILE = ROOT / "data" / "examples" / "passive_rc_dut.tsv"
PLOT_FILE = ROOT / "docs" / "passive_rc_baseline.png"

RESISTANCE_OHM = 56_000.0
CAPACITANCE_F = 10e-9


def load_measurement(path: Path) -> np.ndarray:
    data = np.loadtxt(path, skiprows=1)

    if data.ndim != 2 or data.shape[1] != 5:
        raise ValueError(f"{path.name} must contain exactly five columns.")

    return data


def interpolate_crossing(
    frequency: np.ndarray,
    response_db: np.ndarray,
    target_db: float,
) -> float:
    crossings = np.flatnonzero(response_db <= target_db)

    if len(crossings) == 0:
        return float("nan")

    index = int(crossings[0])

    if index == 0:
        return float(frequency[0])

    f0, f1 = frequency[index - 1 : index + 1]
    y0, y1 = response_db[index - 1 : index + 1]

    return float(f0 + (target_db - y0) * (f1 - f0) / (y1 - y0))


loopback = load_measurement(LOOPBACK_FILE)
dut = load_measurement(DUT_FILE)

if not np.array_equal(loopback[:, 0], dut[:, 0]):
    raise ValueError("Loopback and DUT frequency columns do not match.")

frequency = dut[:, 0]

loopback_gain = loopback[:, 4] / loopback[:, 3]
dut_gain = dut[:, 4] / dut[:, 3]
measured_gain = dut_gain / loopback_gain
measured_gain_db = 20.0 * np.log10(measured_gain)

loopback_phase = loopback[:, 2] - loopback[:, 1]
dut_phase = dut[:, 2] - dut[:, 1]
measured_phase_deg = np.rad2deg(
    np.unwrap(np.deg2rad(dut_phase - loopback_phase))
)

cutoff_theory_hz = 1.0 / (
    2.0 * np.pi * RESISTANCE_OHM * CAPACITANCE_F
)

frequency_ratio = frequency / cutoff_theory_hz
theory_gain_db = -10.0 * np.log10(1.0 + frequency_ratio**2)
theory_phase_deg = -np.rad2deg(np.arctan(frequency_ratio))

cutoff_measured_hz = interpolate_crossing(
    frequency,
    measured_gain_db,
    -3.0103,
)

magnitude_rmse_db = float(
    np.sqrt(np.mean((measured_gain_db - theory_gain_db) ** 2))
)
phase_rmse_deg = float(
    np.sqrt(np.mean((measured_phase_deg - theory_phase_deg) ** 2))
)

figure, (magnitude_axis, phase_axis) = plt.subplots(
    2,
    1,
    figsize=(8, 7),
    sharex=True,
)

magnitude_axis.semilogx(
    frequency,
    measured_gain_db,
    label="Measured",
    linewidth=1.5,
)
magnitude_axis.semilogx(
    frequency,
    theory_gain_db,
    "--",
    label="Theoretical",
    linewidth=1.5,
)
magnitude_axis.axvline(
    cutoff_theory_hz,
    color="gray",
    linestyle=":",
    label=f"Theoretical cutoff: {cutoff_theory_hz:.1f} Hz",
)
magnitude_axis.set_ylabel("Magnitude (dB)")
magnitude_axis.grid(True, which="both", alpha=0.3)
magnitude_axis.legend()

phase_axis.semilogx(
    frequency,
    measured_phase_deg,
    label="Measured",
    linewidth=1.5,
)
phase_axis.semilogx(
    frequency,
    theory_phase_deg,
    "--",
    label="Theoretical",
    linewidth=1.5,
)
phase_axis.set_xlabel("Frequency (Hz)")
phase_axis.set_ylabel("Phase (degrees)")
phase_axis.grid(True, which="both", alpha=0.3)
phase_axis.legend()

figure.suptitle("Passive RC Low-Pass Filter Baseline")
figure.tight_layout()
figure.savefig(PLOT_FILE, dpi=200, bbox_inches="tight")
plt.close(figure)

print(f"Theoretical cutoff: {cutoff_theory_hz:.2f} Hz")
print(f"Measured -3 dB crossing: {cutoff_measured_hz:.2f} Hz")
print(f"Magnitude RMSE: {magnitude_rmse_db:.3f} dB")
print(f"Phase RMSE: {phase_rmse_deg:.3f} degrees")
print(f"Plot saved to: {PLOT_FILE.relative_to(ROOT)}")
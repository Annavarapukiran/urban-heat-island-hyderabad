# UHI Analysis - Core Python Scripts
# Urban Heat Island Evolution in Hyderabad
# Author: Kiran Annavarapu

import numpy as np
import rasterio
import pandas as pd
import matplotlib.pyplot as plt

# ─────────────────────────────────────────────
# 1. NDVI — Normalized Difference Vegetation Index
# ─────────────────────────────────────────────

def compute_ndvi(band4_path, band5_path):
    """
    Compute NDVI from Landsat Band 4 (Red) and Band 5 (NIR).
    NDVI = (NIR - Red) / (NIR + Red)
    """
    with rasterio.open(band4_path) as red_src:
        red = red_src.read(1).astype(float)
    with rasterio.open(band5_path) as nir_src:
        nir = nir_src.read(1).astype(float)

    ndvi = np.where(
        (nir + red) == 0,
        0,
        (nir - red) / (nir + red)
    )
    return ndvi


# ─────────────────────────────────────────────
# 2. Surface Emissivity
# ─────────────────────────────────────────────

def compute_emissivity(ndvi):
    """
    Compute surface emissivity from NDVI.
    Emissivity = ((NDVI - NDVImin) / (NDVImax - NDVImin))^2
    """
    ndvi_min = np.nanmin(ndvi)
    ndvi_max = np.nanmax(ndvi)
    pv = ((ndvi - ndvi_min) / (ndvi_max - ndvi_min)) ** 2
    emissivity = 0.004 * pv + 0.986
    return emissivity


# ─────────────────────────────────────────────
# 3. LST — Land Surface Temperature
# ─────────────────────────────────────────────

def compute_lst(band10_path, emissivity):
    """
    Compute LST from Landsat Band 10 (Thermal Infrared).
    LST = BT / (1 + (λ·BT/ρ) · ln(ε))
    """
    with rasterio.open(band10_path) as tir_src:
        band10 = tir_src.read(1).astype(float)

    # Convert DN to Top of Atmosphere Radiance
    # (Apply Landsat scaling factors as per USGS metadata)
    radiance = band10 * 0.0003342 + 0.1

    # Convert Radiance to Brightness Temperature (BT) in Kelvin
    K1 = 774.8853  # Landsat 8 Band 10 constant
    K2 = 1321.0789
    bt = K2 / (np.log((K1 / radiance) + 1))

    # Compute LST in Celsius
    wavelength = 10.8e-6  # Band 10 wavelength in meters
    rho = 1.438e-2        # h*c/σ constant
    lst_kelvin = bt / (1 + (wavelength * bt / rho) * np.log(emissivity))
    lst_celsius = lst_kelvin - 273.15

    return lst_celsius


# ─────────────────────────────────────────────
# 4. UTFVI — Urban Thermal Field Variance Index
# ─────────────────────────────────────────────

def compute_utfvi(lst):
    """
    UTFVI = (Ts - Tmean) / Tmean
    """
    t_mean = np.nanmean(lst)
    utfvi = (lst - t_mean) / t_mean
    return utfvi


# ─────────────────────────────────────────────
# 5. IBI — Index-Based Built-Up Index
# ─────────────────────────────────────────────

def compute_ibi(band3, band4, band5, band6):
    """
    IBI = (NDBI - (NDVI + MNDWI)/2) / (NDBI + (NDVI + MNDWI)/2)
    Bands: B3=Green, B4=Red, B5=NIR, B6=SWIR
    """
    ndvi = (band5 - band4) / (band5 + band4 + 1e-10)
    ndbi = (band6 - band5) / (band6 + band5 + 1e-10)
    mndwi = (band3 - band6) / (band3 + band6 + 1e-10)

    numerator = ndbi - (ndvi + mndwi) / 2
    denominator = ndbi + (ndvi + mndwi) / 2
    ibi = np.where(denominator == 0, 0, numerator / denominator)
    return ibi


# ─────────────────────────────────────────────
# 6. Summary Statistics
# ─────────────────────────────────────────────

def summarize_index(index_array, index_name, year):
    """Print summary statistics for a given index."""
    stats = {
        "Index": index_name,
        "Year": year,
        "Mean": round(np.nanmean(index_array), 4),
        "Std Dev": round(np.nanstd(index_array), 4),
        "Min": round(np.nanmin(index_array), 4),
        "Max": round(np.nanmax(index_array), 4),
    }
    print(stats)
    return stats


# ─────────────────────────────────────────────
# 7. Known Results from Study (2017, 2020, 2025)
# ─────────────────────────────────────────────

results = {
    "NDVI": {
        2017: {"mean": 0.2231, "std": 0.1087},
        2020: {"mean": 0.2793, "std": 0.0880},
        2025: {"mean": 0.1126, "std": 0.0545},
    },
    "LST": {
        2017: {"mean": 36.2, "std": 5.1},
        2020: {"mean": 33.4, "std": 4.3},
        2025: {"mean": 38.7, "std": 6.2},
    },
}

# Plot NDVI and LST trends
years = [2017, 2020, 2025]
ndvi_means = [results["NDVI"][y]["mean"] for y in years]
lst_means = [results["LST"][y]["mean"] for y in years]

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].bar(years, ndvi_means, color=["green", "limegreen", "olive"], width=1.5)
axes[0].set_title("Mean NDVI (2017–2025)")
axes[0].set_xlabel("Year")
axes[0].set_ylabel("NDVI Value")
axes[0].set_xticks(years)

axes[1].bar(years, lst_means, color=["orange", "gold", "red"], width=1.5)
axes[1].set_title("Mean LST °C (2017–2025)")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("Temperature (°C)")
axes[1].set_xticks(years)

plt.tight_layout()
plt.savefig("figures/ndvi_lst_trends.png", dpi=150)
plt.show()
print("Plot saved to figures/ndvi_lst_trends.png")

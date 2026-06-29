# 🌡️ Urban Heat Island Evolution in Hyderabad
### Remote Sensing Insights into Surface Temperature and Built-up Expansion

**Author:** Kiran Annavarapu  
**Affiliation:** Department of Computer Science and Engineering, NIAMT Ranchi  
**Collaborator:** Sunil C K, IIIT Dharwad  
**Year:** 2024  

---

## 📌 Overview

This research analyzes the **Urban Heat Island (UHI) effect** in Hyderabad, one of India's fastest-growing metropolitan cities, using multi-temporal satellite remote sensing data from **2017, 2020, and 2025**.

The study computes and analyzes five key environmental indices derived from **Landsat 8 & 9** imagery to assess how rapid urbanization has transformed Hyderabad's thermal landscape over nearly a decade.

---

## 🔑 Key Findings

| Metric | 2017 | 2020 | 2025 |
|--------|------|------|------|
| Mean NDVI | 0.223 | 0.279 | 0.113 |
| Mean LST (°C) | 36.2 | 33.4 | 38.7 |
| Mean Emissivity | 0.9699 | 0.9790 | 0.9521 |
| Mean UTFVI | 0.0056 | 0.0044 | 0.0073 |
| Mean IBI | -0.3076 | -0.3826 | -0.2847 |

- 📉 **NDVI dropped 49%** from 2017 to 2025 — significant vegetation loss
- 🌡️ **LST rose by 2.5°C** between 2017 and 2025
- 🏙️ **COVID-19 lockdown (2020)** caused a temporary cooling effect — LST dropped to 33.4°C
- 🔮 **Forecast models project LST exceeding 40°C** in dense urban zones by 2027

---

## 🛰️ Data Sources

- **Landsat 8 & 9** (USGS) — Operational Land Imager (OLI) + Thermal Infrared Sensor (TIRS)
- Imagery years: **2017, 2020, 2025**
- Study area: **Hyderabad, Telangana, India** (574 km², 17°17'–17°31'N, 78°27'–78°37'E)

---

## 📐 Methodology & Indices

### 1. NDVI — Normalized Difference Vegetation Index
Measures vegetation health and density.
```
NDVI = (NIR - Red) / (NIR + Red)
```
*Bands used: Band 4 (Red), Band 5 (NIR)*

### 2. LST — Land Surface Temperature
Captures actual heat emitted from the land surface.
```
LST = BT / (1 + (λ·BT/ρ) · ln(ε))
```
*Band used: Band 10 (Thermal Infrared)*

### 3. Surface Emissivity
Measures how effectively a surface emits thermal radiation.
```
Emissivity = ((NDVI - NDVImin) / (NDVImax - NDVImin))²
```

### 4. UTFVI — Urban Thermal Field Variance Index
Identifies zones with elevated thermal stress.
```
UTFVI = (Ts - Tmean) / Tmean
```

### 5. IBI — Index-Based Built-Up Index
Identifies urban/built-up areas using spectral signatures.
```
IBI = (NDBI - (NDVI + MNDWI)/2) / (NDBI + (NDVI + MNDWI)/2)
```
*Bands used: Band 3 (Green), Band 4 (Red), Band 5 (NIR), Band 6 (SWIR)*

---

## 🛠️ Tools & Technologies

| Category | Tools Used |
|----------|-----------|
| Satellite Data | Landsat 8 & 9 (USGS) |
| GIS Processing | QGIS |
| Programming | Python 3 |
| Python Libraries | NumPy, Rasterio, Pandas |
| Visualization | Matplotlib |
| ML Forecasting | Scikit-learn (Linear Regression, Random Forest) |

---

## 🔮 LST Forecast for 2027

Two forecasting models were applied to project future thermal conditions:

| Model | Min LST (°C) | Mean LST (°C) | Max LST (°C) |
|-------|-------------|--------------|-------------|
| Linear Regression | 10.00 | 38.70 | 60.00 |
| Random Forest | 46.76 | 46.76 | 46.76 |

Both models indicate **continued intensification of urban heat stress**, especially in densely built-up zones.

---

## 🗂️ Repository Structure

```
urban-heat-island-hyderabad/
│
├── README.md                  # Project overview (this file)
├── paper/
│   └── UHI_Hyderabad.pdf      # Full research paper
├── notebooks/
│   └── uhi_analysis.ipynb     # Python analysis notebook (coming soon)
├── data/
│   └── README.md              # Data access instructions (Landsat via USGS)
└── figures/
    ├── ndvi_maps.png
    ├── lst_maps.png
    ├── emissivity_maps.png
    ├── utfvi_maps.png
    ├── ibi_maps.png
    └── forecast_2027.png
```

---

## 📊 Results Summary

The multiyear analysis reveals:
- Consistent **decline in vegetation cover** across Hyderabad
- **Rising land surface temperatures** with growing spatial heterogeneity by 2025
- The **COVID-19 lockdown** offered a rare natural experiment showing how reduced anthropogenic activity temporarily reversed thermal stress
- **Built-up expansion** continues to be the primary driver of UHI intensification

---

## 🌱 Policy Implications

The findings strongly support:
- Integration of **green infrastructure** (rooftop gardens, tree-lined streets, urban parks)
- **Climate-responsive urban planning** to reduce thermal vulnerability
- Protection of remaining **vegetation and water bodies**
- Targeted interventions in **high-risk thermal zones** identified by UTFVI mapping

---

## 📄 Citation

If you reference this work, please cite:

```
Annavarapu, K., & Sunil C K. (2024). Urban Heat Island Evolution in Hyderabad: 
Remote Sensing Insights into Surface Temperature and Built-up Expansion. 
Department of CSE, NIAMT Ranchi & IIIT Dharwad.
```

---

## 📬 Contact

**Kiran Annavarapu**  
📧 annavarapukiranjune@gmail.com  
🎓 B.Tech Computer Engineering, NIAMT Ranchi (2026)

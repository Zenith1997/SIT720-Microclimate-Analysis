# Microclimate Sensor Data Analysis

Prepare noisy environmental sensor readings for exploratory analysis.

**Python · pandas · matplotlib · data wrangling**

## Project at a glance

Work in progress: the uploaded notebook contains no saved execution outputs. Final sensor rankings and numerical findings are not claimed.

## Technical work

- Missing-value investigation
- PM2.5 and PM10 exploration
- Coordinate parsing and data quality checks
- Min–max scaling and exploratory summaries

## Explore the evidence

- [SIT720_2_1P_Data_Wrangling.ipynb](SIT720_2_1P_Data_Wrangling.ipynb)
- [SIT720_2_1P_Report.pdf](SIT720_2_1P_Report.pdf)

## Run locally

```bash
python -m venv .venv
# Activate the environment, then:
python -m pip install jupyter numpy pandas matplotlib scikit-learn
jupyter notebook
```

Supply microclimate-sensors-data.csv or use the configured City of Melbourne download route in the notebook.

Open the linked notebook and run the cells in order. Package names reflect the source imports; a fresh environment was not tested during this documentation update. Dataset downloads require internet access.

## Limitations and status

Missing-data decisions, sensor coverage and units need checking against the actual input and completed outputs.

The notebook is unexecuted; see the report for the intended analysis.

**Author:** Zenith Anthony Dabarera · SIT720 Machine Learning  
[AI/ML portfolio](https://github.com/Zenith1997)

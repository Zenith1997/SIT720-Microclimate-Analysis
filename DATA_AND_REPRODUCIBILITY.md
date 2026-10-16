# Dataset and reproducibility notes

The notebook reads the **City of Melbourne Open Data** `microclimate-sensors-data` feed. It tries an existing `microclimate-sensors-data.csv` before its configured official City of Melbourne CSV export URLs.

Data availability, column names, year coverage and sensor locations may change. Verify them against the current feed before answering the original 2026 wind/noise questions.

**Status: not executed.** The published notebook has no saved code-cell outputs. The GitHub workflow only checks JSON structure; it does not download the current feed or confirm any 2026 sensor ranking.

## Running the original notebook

```bash
python -m pip install -r requirements.txt
jupyter notebook SIT720_2_1P_Data_Wrangling.ipynb
```

These are version *ranges*, not an exact captured original environment. A fresh run has not been validated by this documentation update.

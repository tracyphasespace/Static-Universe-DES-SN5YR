#!/usr/bin/env bash
# Fetch everything the b=1 transfer pipeline needs.
set -euo pipefail
cd "$(dirname "$0")"
# Raw griz light curves for all 8,293 DES candidates — hosted (gzipped, with
# sha256) in the companion methods repository.
if [ ! -f des_sn5yr_raw_photometry.csv ]; then
  curl -fL --retry 3 -o des_sn5yr_raw_photometry.csv.gz \
    "https://raw.githubusercontent.com/tracyphasespace/Model-Discrimination-DES-SN5YR/master/data/des_sn5yr_raw_photometry.csv.gz"
  gunzip -f des_sn5yr_raw_photometry.csv.gz
fi
# DES-SN5YR v1.2 release files (pinned tag; main has moved to Dovekie)
B="https://raw.githubusercontent.com/des-science/DES-SN5YR/v1.2"
[ -f DES-SN5YR_HD+MetaData.csv ] || curl -fL --retry 3 -o "DES-SN5YR_HD+MetaData.csv" \
  "$B/4_DISTANCES_COVMAT/DES-SN5YR_HD+MetaData.csv"
[ -f DES_noredshift_classification_Moller2024.csv ] || curl -fL --retry 3 \
  -o DES_noredshift_classification_Moller2024.csv \
  "$B/3_CLASSIFICATION/DES_noredshift_classification_Moller2024.csv"
sha256sum *.csv
echo done

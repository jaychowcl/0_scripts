#!/usr/bin/bash

# Check if input file exists
if [ ! -f "$1" ]; then
  echo "Input file not found!"
  exit 1
fi

# Output file
output_file="output.csv"

# Print headers into output file
echo "Postcode sector,Crime rate vs. ENG & WLS rate,Crime rate per 1000 workday people,Total number of crimes" > $output_file

# Process the input file and append to output CSV
awk -F'\t' '{print $1","$2","$3","$4}' "$1" >> $output_file

# Print success message
echo "Conversion complete! Output saved to $output_file"

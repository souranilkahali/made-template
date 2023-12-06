#!/bin/bash
python pipeline.py

database_file="dbsouranil"

# Check if the output file(s) exist
if [ -f "$database_file" ]; then
    echo "Yes! The database file exists."
else
    echo "No database file found!!"
fi
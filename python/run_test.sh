#!/bin/sh
./get_testing_file.sh
python testing.py
find ../Result/ -name "*.tsv" > result_path.txt
python testing-final.py

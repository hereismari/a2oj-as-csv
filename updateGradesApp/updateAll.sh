#!/bin/bash

echo 'updating main sheet...'
python updateLists.py 0  $1 # updates main sheet
echo 'updating late sheet...'
python updateLists.py 1  $1 # updates late sheet
echo 'updating late column from main sheet'
python updateLate.py  $1 # updates late column in main sheet

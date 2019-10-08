#!/usr/bin/env bash
# processinput.sh
# Converts the binary input into a readable file
# Michael Chambers, 2017

god --endian little -d -w20 < challenge.bin > tmp.dat
tr -s ' ' < tmp.dat | cut -d' ' -f 2- | tr ' ' '\t' > tmp2.dat

seq 0 10 30050 > tmp3.dat

paste tmp3.dat tmp2.dat > tmp4.dat

rm -f tmp.dat tmp2.dat tmp3.dat
mv tmp4.dat rawinput.txt

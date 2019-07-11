#!/bin/bash
~/gdown.pl $1 out.xz > /dev/null 2>&1
unxz out.xz > /dev/null 2>&1
tar xf out > /dev/null 2>&1
dir=`tar tf out | head -1 | cut -f1 -d"/"`
cd "$dir"
mpirun -n 7 abinit < tbase*_x.files > log 2> err
echo "Result at: "`pastebinit tbase*_*.out 2> /dev/null`
echo "If there was an error it's here: "`pastebinit err 2> /dev/null`
cd ..
rm -rf "$dir" out out.xz

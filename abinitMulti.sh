#!/bin/bash
scriptDir=`pwd`
dlDir=downloads
cores=4
mkdir $dlDir  > /dev/null 2>&1
cd $dlDir
$scriptDir/gdown.pl $1 out.xz > /dev/null 2>&1
unxz out.xz > /dev/null 2>&1
tar xf out > /dev/null 2>&1     
dir=`tar tf out | head -1 | cut -f1 -d"/"`
rm -rf out out.xz
cd "$dir"
mpirun -n $cores abinit --verbose < tbase*_x.files > log 2> err
if [ "$(wc -l err)" != "0 err" ]
then
	echo Error: `pastebinit -b slexy.org err 2> /dev/null`
fi
echo Results: `pastebinit -b slexy.org tbase*_*.out 2> /dev/null`

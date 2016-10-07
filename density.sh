#!/bin/bash

#echo "running MC simulation..."
#python 3D.py > traj.xyz
#python 3D.py -vmd > mc.xyz
echo "running g(r)..."
python gr.py -mc -f 1000 > a.txt 
python gr.py -f 1000 > b.txt

#superimposing the plots
python comp.py

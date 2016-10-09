#!/bin/bash

rho=() 

for ((i=0; i<${rho[@]}; i++))
do

    echo "running MC simulation..."
    python 3D.py -n $i > traj.xyz
    python 3D.py -vmd > mc.xyz
    echo "running g(r)..."
    python gr.py -mc -n $i -f 1000 > a.txt 
    #python gr.py -n $i -f 1000 > b.txt

#superimposing the plots
python comp.py

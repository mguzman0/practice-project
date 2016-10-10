#!/bin/bash

rho=(0.5 0.55555556 0.61111111 0.66666667 0.72222222 0.77777778  0.83333333  0.88888889  0.94444444 1.) 

for ((i=0; i<${#rho[@]}; i++))
do

    lmp_ubuntu -var seed $RANDOM < ljsim3D.lmp
    echo "running MC simulation..."
    python 3D.py -density ${rho[i]} > traj.xyz
    echo "vmd version"
    python 3D.py -vmd -density ${rho[i]} > mc$i.xyz
    echo "running g(r)..."
    python gr.py -mc -f 1000 > mc_gr$i.txt 
    python gr.py -f 1000 > md_gr$i.txt
    #superimposing the plots
    python comp.py -n $i

done

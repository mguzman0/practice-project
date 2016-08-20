#!/bin/bash

if [ -z ${1+x} ]; then
    echo "Requires argument TEMP or EPSILON to run"
    exit
fi

T=(4 5 6 7 8 9 10 20 30 40 50 55 60 100 200)
E=(0.35 0.4 0.45 0.5 0.55 0.6 0.7 0.9 1.1 1.4 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20) 
ENERGY_DIR=$(pwd)/info/run$2
TEMP_DIR=$(pwd)/info/run$2
DIFFUSION_DIR=$(pwd)/info/run$2

mkdir $ENERGY_DIR
mkdir $ENERGY_DIR/energy
#mkdir $TEMP_DIR
mkdir $TEMP_DIR/temp
#mkdir $DIFFUSION_DIR
mkdir $DIFFUSION_DIR/diffusions
#exit
# ===========================
# TEMP
# ===========================
if [ $1 == "TEMP" ]; then
    
    if [ ! -e $ENERGY_DIR ]; then
        mkdir $ENERGY_DIR
    elif [ -e $ENERGY_DIR/energy_temp.txt ]; then
        rm -r $ENERGY_DIR/*
    fi

    if [ ! -e $TEMP_DIR ]; then 
        mkdir $TEMP_DIR
    elif [ -e $TEMP_DIR/temp_temp.txt ]; then 
        rm -r $TEMP_DIR/*
    fi
    
    if [ ! -e $DIFFUSION_DIR ]; then
        mkdir $DIFFUSION_DIR
    elif [ -e  $DIFFUSION_DIR/coefficients_temp.txt ]; then 
        rm -r $DIFFUSION_DIR/*
    fi

 
    for ((i=0; i<${#T[@]}; i++))
    do
        lammps -var temp ${T[i]} -var ep 1 < ljsim.txt
        rm log.lammps
        #echo "temp: ${T[i]}"
        echo "checking total energy..."
        python emd.py -n $i -save $ENERGY_DIR >> $ENERGY_DIR/energy_temp.txt
        echo "checking temperature..."
        python emd.py -temp -n $i -save $TEMP_DIR >> $TEMP_DIR/temp_temp.txt
        echo "calculating diffusion..."
        python analysis.py -n $i -save $DIFFUSION_DIR >> $DIFFUSION_DIR/coefficients_temp.txt
    done
fi

# ===========================
# EPSILON
# ===========================
if [ $1 == "EPSILON" ]; then
    if [ ! -e $ENERGY_DIR ]; then
        mkdir $ENERGY_DIR
	mkdir $ENERGY_DIR/energy
    elif [ -e $ENERGY_DIR/energy_ep.txt ]; then
        rm -r $ENERGY_DIR/*
    fi

    if [ ! -e $TEMP_DIR ]; then 
        mkdir $TEMP_DIR
        mkdir $TEMP_DIR/temp
    elif [ -e $TEMP_DIR/temp_ep.txt ]; then 
        rm -r $TEMP_DIR/*
    fi
    
    if [ ! -e $DIFFUSION_DIR ]; then
        mkdir $DIFFUSION_DIR
        mkdir $DIFFUSION_DIR/diffusions
    elif [ -e  $DIFFUSION_DIR/coefficients_ep.txt ]; then 
        rm -r $DIFFUSION_DIR/*
    fi
   
    if [ -e epsilon.txt ]; then 
        rm epsilon.txt 
    fi
    
    if [ -e timestep_ep.txt ]; then 
        rm timestep_ep.txt
    fi
 
    echo "calculating timestep..." 
    for ((i=0; i<${#E[@]}; i++))
    do
        python sstime.py -n ${E[i]} >> $DIFFUSION_DIR/timestep_ep.txt
        python printep.py -n ${E[i]} >> $DIFFUSION_DIR/epsilon.txt
    done
    mapfile -t dt < $DIFFUSION_DIR/timestep_ep.txt
    for ((i=0; i<${#E[@]}; i++))
    do
        lammps -var ep ${E[i]} -var dt ${dt[i]} -var seed $RANDOM < ljsim.txt
        mv lj.xyz lj$i.xyz
	mv lj$i.xyz $ENERGY_DIR/diffusions
        echo "checking total energy..."
        python emd.py -n $i -save $ENERGY_DIR/energy >> $ENERGY_DIR/energy/energy_ep.txt
        echo "checking temperature..."
        python emd.py -temp -n $i -save $TEMP_DIR/temp >> $TEMP_DIR/temp/temp_ep.txt
        echo "calculating diffusion..."
        python analysis.py -n $i -save $DIFFUSION_DIR/diffusions >> $DIFFUSION_DIR/diffusions/coefficients_ep.txt
    done
fi

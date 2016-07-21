#!/bin/bash

if [ -z ${1+x} ]; then
    echo "Requires argument TEMP or EPSILON or TIME to run"
    exit
fi

T=(4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34)
E=(1 2)

ENERGY_DIR=$(pwd)/energy
TEMP_DIR=$(pwd)/temp
DIFFUSION_DIR=$(pwd)/diffusions
TIMESTEP_DIR=$(pwd)/timestep

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

 
    for ((i=0; i<31; i++))
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
    elif [ -e $ENERGY_DIR/energy_ep.txt ]; then
        rm -r $ENERGY_DIR/*
    fi

    if [ ! -e $TEMP_DIR ]; then 
        mkdir $TEMP_DIR
    elif [ -e $TEMP_DIR/temp_ep.txt ]; then 
        rm -r $TEMP_DIR/*
    fi

    if [ ! -e $TIMESTEP_DIR ]; then
        mkdir $TIMESTEP_DIR
    elif [ -e $TIMESTEP_DIR/timestep_ep.txt ]; then
        rm -r $TIMESTEP_DIR/*
    fi
    
    echo "calculating timestep..." 
    for ((i=0; i<${#E[@]}; i++))
    do
        python sstime.py -n ${E[i]} >> timestep_ep.txt
    done
    mapfile -t dt < timestep_ep.txt
    exit
    for ((i=0; i<2; i++))
    do
        lammps -var ep ${E[i]} -var temp 4.7 < ljsim.txt
        #echo "temp: ${TEMP[i]}"
        echo "checking total energy..."
        python emd.py -n $i -save $ENERGY_DIR >> $ENERGY_DIR/energy_ep.txt
        echo "checking temperature..."
        python emd.py -temp -n $i -save $TEMP_DIR >> $TEMP_DIR/temp_ep.txt
        echo "calculating diffusion..."
        python analysis.py -n $i -save $DIFFUSION_DIR >> $DIFFUSION_DIR/coefficients_ep.txt
    done
fi

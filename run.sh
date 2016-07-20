#!/bin/sh

if [ -z ${1+x} ]; then
    echo "Requires argument TEMP or EPSILON to run"
    exit
fi

T=(4)
E=(1 2 3 4)

ENERGY_DIR=$(pwd)/energy
TEMP_DIR=$(pwd)/temp
DIFFUSION_DIR=$(pwd)/diffusions

# ===========================
# TEMP
# ===========================
if [ $1 == "TEMP" ]; then
    
    if [ ! -e $ENERGY_DIR ]; then
        mkdir $ENERGY_DIR
    elif [ -e $ENERGY_DIR/energy_temp.txt ]; then
        rm $ENERGY_DIR/*
    fi

    if [ ! -e $TEMP_DIR ]; then 
        mkdir $TEMP_DIR
    elif [ -e $TEMP_DIR/temp_temp.txt ]; then 
        rm $TEMP_DIR/*
    fi

    if [ ! -e $DIFFUSION_DIR ]; then
        mkdir $DIFFUSION_DIR
    elif [ -e $DIFFUSION_DIR/coefficients_temp.txt ]; then 
        rm $DIFFUSION_DIR/*
    fi

 
    for ((i=0; i<1; i++))
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
        rm $ENERGY_DIR/energy_ep.txt
    fi

    if [ ! -e $TEMP_DIR ]; then 
        mkdir $TEMP_DIR
    elif [ -e $TEMP_DIR/temp_ep.txt ]; then 
        rm $TEMP_DIR/temp_ep.txt
    fi

    for ((i=0; i>2; i++))
    do
        lammps -var ep ${E[i]} -var temp 4.7 < ljsim.txt
        #echo "temp: ${TEMP[i]}"
        echo "checking total energy..."
        python emd.py -n $i -save $ENERGY_DIR >> $ENERGY_DIR/energy_ep.txt
        echo "checking temperature..."
        python emd.py -temp -n $i -save $TEMP_DIR >> $TEMP_DIR/temp_ep.txt
        echo "calculating diffusion..."
        python analysis.py >> coefficients.txt
    done
fi

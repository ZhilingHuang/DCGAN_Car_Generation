#!/usr/bin/env bash

# Creates the environment
conda create -n car_gen python=2.7

# Activates the environment
source activate car_gen

# Upgrade pip
pip install --upgrade pip

# pip install into environment
pip install --upgrade -r requirements.txt
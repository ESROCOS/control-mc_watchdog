#!/bin/bash

rm -rf output

mkdir output


#bipc.sh -I . -p InterfaceViewFull -d "Syst()" --gencpp-output output --gencpp-cc-I $PWD/ext-cpp 

bipc.sh -I . -p InterfaceView -d "Syst()" --gencpp-output output --gencpp-cc-I $PWD/ext-cpp --gencpp-no-main

mkdir output/build

cd output/build

cmake ..

make

cd ../..

#output/build/system -l 100 --silent

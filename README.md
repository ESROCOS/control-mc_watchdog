# control-mc_watchdog
This project contains the sources and dependencies for the Watchdog component from the planetary demonstration.

The content is structured as follows.

## Configuration file

config.cfg is a configuration file for the Watchdog component.
It contains the threshold value for the Watchdog timeout against which the scenario needs to be validated.

## BipEngine

The folder contains the reference engine for BIP real-time as library. 
This folder is a dependency for the TasteModel.


## BipModel 

The folder contains the full BIP model of the planetary scenario. It consists of:

- the BIP model types generated in C++ - folder include -,
- the BIP model as C++ static library - folder lib -, and 
- the BIP sources of the model and external code - folder sources.

The include and lib folders are dependencies for the integration of the Watchdog in TasteModel.

## TasteModel

The folder contains the TASTE-SDL model used in for the design and analysis of the Watchdog.
The obtained Watchdog (in C++) is integrated in this model - subfolder watchdog.
The subfolder contains: 

- the implementation of external functions (in C++) used by the BIP model - files ExternInterfaceViewFcns, ExternalPortCmdWatchdog  -, 
- the implementation of wrappers conecting the TASTE template to the BIP-generated FDIR code - files BipWrapper -, and
- the instantiation of the BIP model generated code - file DeployTypes.hpp and Deploy.cc.


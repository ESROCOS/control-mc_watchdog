#ifndef INTERFACEVIEW_PT____INTERFACEVIEW____PORT_HPP_
#define INTERFACEVIEW_PT____INTERFACEVIEW____PORT_HPP_

// /home/taste/Documents/ESROCOS/control-mc_watchdog/BipModel/sources/InterfaceView.bip:54:2
// include package "master" header
#include <InterfaceView.hpp>

#include <Port.hpp>

// User include given in @cpp annotation
#include <ExternInterfaceViewFcns.hpp>
#include <ExternalPortCmdWdog.hpp>

class PT__InterfaceView__Port : public virtual Port{

public:
    PT__InterfaceView__Port(const string &name, const ExportType& type);
    ~PT__InterfaceView__Port();
};
#endif // INTERFACEVIEW_PT____INTERFACEVIEW____PORT_HPP_

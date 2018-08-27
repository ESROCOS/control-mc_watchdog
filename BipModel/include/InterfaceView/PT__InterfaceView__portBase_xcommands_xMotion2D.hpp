#ifndef INTERFACEVIEW_PT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_
#define INTERFACEVIEW_PT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

// /home/taste/Documents/ESROCOS/Planetary/BipModel/sources/InterfaceView.bip:56:2
// include package "master" header
#include <InterfaceView.hpp>

#include <Port.hpp>

// User include given in @cpp annotation
#include <ExternInterfaceViewFcns.hpp>
#include <ExternalPortCmdWdog.hpp>

class PT__InterfaceView__portBase_xcommands_xMotion2D : public virtual Port{

public:
    PT__InterfaceView__portBase_xcommands_xMotion2D(const string &name, const ExportType& type);
    ~PT__InterfaceView__portBase_xcommands_xMotion2D();
};
#endif // INTERFACEVIEW_PT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

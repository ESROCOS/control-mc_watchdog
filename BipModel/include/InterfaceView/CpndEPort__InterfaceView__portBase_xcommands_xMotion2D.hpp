#ifndef INCLUDE_INTERFACEVIEW_CPNDEPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_
#define INCLUDE_INTERFACEVIEW_CPNDEPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

#include <CompoundExportPort.hpp>

#include <InterfaceView/PT__InterfaceView__portBase_xcommands_xMotion2D.hpp>

class CpndEPort__InterfaceView__portBase_xcommands_xMotion2D :
    public virtual Port,
    public CompoundExportPort,
    public PT__InterfaceView__portBase_xcommands_xMotion2D {
public:
    CpndEPort__InterfaceView__portBase_xcommands_xMotion2D(const string &name);
    virtual ~CpndEPort__InterfaceView__portBase_xcommands_xMotion2D();
}; 

#endif // INCLUDE_INTERFACEVIEW_CPNDEPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

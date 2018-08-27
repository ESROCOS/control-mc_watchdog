#ifndef INCLUDE_INTERFACEVIEW_CONNPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_
#define INCLUDE_INTERFACEVIEW_CONNPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

#include <ConnectorExportPort.hpp>

#include <InterfaceView/PT__InterfaceView__portBase_xcommands_xMotion2D.hpp>

class ConnPort__InterfaceView__portBase_xcommands_xMotion2D : public virtual Port,
                public ConnectorExportPort,
                public PT__InterfaceView__portBase_xcommands_xMotion2D {
public:
    ConnPort__InterfaceView__portBase_xcommands_xMotion2D(const string &name);
    virtual ~ConnPort__InterfaceView__portBase_xcommands_xMotion2D();
}; 

#endif // INCLUDE_INTERFACEVIEW_CONNPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

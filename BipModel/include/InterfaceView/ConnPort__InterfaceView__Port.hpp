#ifndef INCLUDE_INTERFACEVIEW_CONNPORT____INTERFACEVIEW____PORT_HPP_
#define INCLUDE_INTERFACEVIEW_CONNPORT____INTERFACEVIEW____PORT_HPP_

#include <ConnectorExportPort.hpp>

#include <InterfaceView/PT__InterfaceView__Port.hpp>

class ConnPort__InterfaceView__Port : public virtual Port,
                public ConnectorExportPort,
                public PT__InterfaceView__Port {
public:
    ConnPort__InterfaceView__Port(const string &name);
    virtual ~ConnPort__InterfaceView__Port();
}; 

#endif // INCLUDE_INTERFACEVIEW_CONNPORT____INTERFACEVIEW____PORT_HPP_

#ifndef INCLUDE_INTERFACEVIEW_CPNDEPORT____INTERFACEVIEW____PORT_HPP_
#define INCLUDE_INTERFACEVIEW_CPNDEPORT____INTERFACEVIEW____PORT_HPP_

#include <CompoundExportPort.hpp>

#include <InterfaceView/PT__InterfaceView__Port.hpp>

class CpndEPort__InterfaceView__Port :
    public virtual Port,
    public CompoundExportPort,
    public PT__InterfaceView__Port {
public:
    CpndEPort__InterfaceView__Port(const string &name);
    virtual ~CpndEPort__InterfaceView__Port();
}; 

#endif // INCLUDE_INTERFACEVIEW_CPNDEPORT____INTERFACEVIEW____PORT_HPP_

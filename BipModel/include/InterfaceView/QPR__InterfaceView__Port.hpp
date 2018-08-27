#ifndef INCLUDE_INTERFACEVIEW_QPR____INTERFACEVIEW____PORT_HPP_
#define INCLUDE_INTERFACEVIEW_QPR____INTERFACEVIEW____PORT_HPP_

#include <QuotedPortReference.hpp>

#include <InterfaceView/PT__InterfaceView__Port.hpp>

class QPR__InterfaceView__Port : public QuotedPortReference {
public:
    QPR__InterfaceView__Port(PT__InterfaceView__Port &port, const bool &trigger);
    virtual ~QPR__InterfaceView__Port();
}; 

#endif // INCLUDE_INTERFACEVIEW_QPR____INTERFACEVIEW____PORT_HPP_

#ifndef INCLUDE_INTERFACEVIEW_ATOMEXTERNALPORT____INTERFACEVIEW____PORT_HPP_
#define INCLUDE_INTERFACEVIEW_ATOMEXTERNALPORT____INTERFACEVIEW____PORT_HPP_

#include <AtomExternalPort.hpp>
#include <TimeValue.hpp>

#include <InterfaceView/PT__InterfaceView__Port.hpp>

class AtomExternalPort__InterfaceView__Port : public AtomExternalPort {
public:
    AtomExternalPort__InterfaceView__Port(const string &name, const EventConsumptionPolicy &policy);
    virtual ~AtomExternalPort__InterfaceView__Port();

    virtual void initialize() { }
    virtual bool hasEvent() const { return false; }
    virtual void popEvent() { }
    virtual void purgeEvents() { }
    virtual TimeValue eventTime() const { return TimeValue::ZERO; }


protected:

private:
};

#endif // INCLUDE_INTERFACEVIEW_ATOMEXTERNALPORT____INTERFACEVIEW____PORT_HPP_

#ifndef INCLUDE_INTERFACEVIEW_ATOMEXTERNALPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_
#define INCLUDE_INTERFACEVIEW_ATOMEXTERNALPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

#include <AtomExternalPort.hpp>
#include <TimeValue.hpp>

#include <InterfaceView/PT__InterfaceView__portBase_xcommands_xMotion2D.hpp>

class AtomExternalPort__InterfaceView__portBase_xcommands_xMotion2D : public AtomExternalPort {
public:
    AtomExternalPort__InterfaceView__portBase_xcommands_xMotion2D(const string &name, const EventConsumptionPolicy &policy);
    virtual ~AtomExternalPort__InterfaceView__portBase_xcommands_xMotion2D();

    virtual void initialize() { }
    virtual bool hasEvent() const { return false; }
    virtual void popEvent() { }
    virtual void purgeEvents() { }
    virtual TimeValue eventTime() const { return TimeValue::ZERO; }

    virtual asn1SccBase_commands_Motion2D &event_get_v() { return m_v; }

protected:
    asn1SccBase_commands_Motion2D m_v;

private:
};

#endif // INCLUDE_INTERFACEVIEW_ATOMEXTERNALPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

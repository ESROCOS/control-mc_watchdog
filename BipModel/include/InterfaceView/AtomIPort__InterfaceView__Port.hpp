#ifndef INCLUDE_INTERFACEVIEW_ATOMIPORT____INTERFACEVIEW____PORT_HPP_
#define INCLUDE_INTERFACEVIEW_ATOMIPORT____INTERFACEVIEW____PORT_HPP_

#include <AtomInternalPort.hpp>

#include <InterfaceView/PT__InterfaceView__Port.hpp>
#include <InterfaceView/PV__InterfaceView__Port.hpp>

class AtomIPort__InterfaceView__Port : public AtomInternalPort {
public:
    AtomIPort__InterfaceView__Port(const string &name, bool hasEarlyUpdate, bool hasUrgency);
    virtual ~AtomIPort__InterfaceView__Port();

    PortValue &portValue() const;
    bool hasPortValue() const;
    void setPortValue(PortValue &portValue);
    void clearPortValue();

    bool isEnabled() const;
    void setIsEnabled(bool b);
    bool isDisabledByPriorities() const;
    void setIsDisabledByPriorities(bool b);

protected:
    PV__InterfaceView__Port *mPortValue;

private:
    bool mIsEnabled;
    bool mIsDisabledByPriorities;
}; 

inline
PortValue &AtomIPort__InterfaceView__Port::portValue() const {
    return *mPortValue;
}

inline
bool AtomIPort__InterfaceView__Port::hasPortValue() const {
    return mPortValue != NULL;
}

inline
void AtomIPort__InterfaceView__Port::setPortValue(PortValue &portValue) {
    assert(dynamic_cast<PV__InterfaceView__Port *>(&portValue) != NULL);
    mPortValue = static_cast<PV__InterfaceView__Port *> (&portValue);
}
inline
void AtomIPort__InterfaceView__Port::clearPortValue() {
    mPortValue = NULL;
}

inline
bool AtomIPort__InterfaceView__Port::isEnabled() const {
    return mIsEnabled;
}

inline
void AtomIPort__InterfaceView__Port::setIsEnabled(bool b) {
    mIsEnabled = b;
}

inline
bool AtomIPort__InterfaceView__Port::isDisabledByPriorities() const {
    return mIsDisabledByPriorities;
}

inline
void AtomIPort__InterfaceView__Port::setIsDisabledByPriorities(bool b) {
    mIsDisabledByPriorities = b;
}

#endif // INCLUDE_INTERFACEVIEW_ATOMIPORT____INTERFACEVIEW____PORT_HPP_

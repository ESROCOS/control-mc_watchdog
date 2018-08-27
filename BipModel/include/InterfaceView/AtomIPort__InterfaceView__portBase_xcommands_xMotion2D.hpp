#ifndef INCLUDE_INTERFACEVIEW_ATOMIPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_
#define INCLUDE_INTERFACEVIEW_ATOMIPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

#include <AtomInternalPort.hpp>

#include <InterfaceView/PT__InterfaceView__portBase_xcommands_xMotion2D.hpp>
#include <InterfaceView/PV__InterfaceView__portBase_xcommands_xMotion2D.hpp>

class AtomIPort__InterfaceView__portBase_xcommands_xMotion2D : public AtomInternalPort {
public:
    AtomIPort__InterfaceView__portBase_xcommands_xMotion2D(const string &name, bool hasEarlyUpdate, bool hasUrgency);
    virtual ~AtomIPort__InterfaceView__portBase_xcommands_xMotion2D();

    PortValue &portValue() const;
    bool hasPortValue() const;
    void setPortValue(PortValue &portValue);
    void clearPortValue();

    bool isEnabled() const;
    void setIsEnabled(bool b);
    bool isDisabledByPriorities() const;
    void setIsDisabledByPriorities(bool b);

protected:
    PV__InterfaceView__portBase_xcommands_xMotion2D *mPortValue;

private:
    bool mIsEnabled;
    bool mIsDisabledByPriorities;
}; 

inline
PortValue &AtomIPort__InterfaceView__portBase_xcommands_xMotion2D::portValue() const {
    return *mPortValue;
}

inline
bool AtomIPort__InterfaceView__portBase_xcommands_xMotion2D::hasPortValue() const {
    return mPortValue != NULL;
}

inline
void AtomIPort__InterfaceView__portBase_xcommands_xMotion2D::setPortValue(PortValue &portValue) {
    assert(dynamic_cast<PV__InterfaceView__portBase_xcommands_xMotion2D *>(&portValue) != NULL);
    mPortValue = static_cast<PV__InterfaceView__portBase_xcommands_xMotion2D *> (&portValue);
}
inline
void AtomIPort__InterfaceView__portBase_xcommands_xMotion2D::clearPortValue() {
    mPortValue = NULL;
}

inline
bool AtomIPort__InterfaceView__portBase_xcommands_xMotion2D::isEnabled() const {
    return mIsEnabled;
}

inline
void AtomIPort__InterfaceView__portBase_xcommands_xMotion2D::setIsEnabled(bool b) {
    mIsEnabled = b;
}

inline
bool AtomIPort__InterfaceView__portBase_xcommands_xMotion2D::isDisabledByPriorities() const {
    return mIsDisabledByPriorities;
}

inline
void AtomIPort__InterfaceView__portBase_xcommands_xMotion2D::setIsDisabledByPriorities(bool b) {
    mIsDisabledByPriorities = b;
}

#endif // INCLUDE_INTERFACEVIEW_ATOMIPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

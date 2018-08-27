#ifndef INCLUDE_INTERFACEVIEW_ATOMEPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_
#define INCLUDE_INTERFACEVIEW_ATOMEPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

#include <AtomExportPort.hpp>
#include <InterfaceView/AtomIPort__InterfaceView__portBase_xcommands_xMotion2D.hpp>

#include <InterfaceView/PT__InterfaceView__portBase_xcommands_xMotion2D.hpp>

class AtomEPort__InterfaceView__portBase_xcommands_xMotion2D :
    public virtual Port,
    public AtomExportPort,
    public PT__InterfaceView__portBase_xcommands_xMotion2D {
public:
    AtomEPort__InterfaceView__portBase_xcommands_xMotion2D(const string &name, bool hasEarlyUpdate, bool hasUrgency);
    virtual ~AtomEPort__InterfaceView__portBase_xcommands_xMotion2D();
    virtual void addInternalPort(AtomIPort__InterfaceView__portBase_xcommands_xMotion2D &p);

    virtual vector<PortValue *> &portValues();
    virtual const vector<PortValue *> &portValues() const;
    virtual bool hasPortValues() const;
    virtual void addPortValue(PortValue &port);
    virtual void clearPortValues();

    virtual bool isReset() const;
    void setIsReset(bool b);

protected:
// Getting messy to store actual type and return more abstract one (thanks to vector template...)
//    vector<PV__InterfaceView__portBase_xcommands_xMotion2D *> mPortValues;
    vector<PortValue *> mPortValues;
    bool mIsReset;
}; 


inline
void AtomEPort__InterfaceView__portBase_xcommands_xMotion2D::addInternalPort(AtomIPort__InterfaceView__portBase_xcommands_xMotion2D &p) {
    AtomExportPort::addInternalPort(p);
}

inline
vector<PortValue *> &AtomEPort__InterfaceView__portBase_xcommands_xMotion2D::portValues() {
    return mPortValues;
}

inline
const vector<PortValue *> &AtomEPort__InterfaceView__portBase_xcommands_xMotion2D::portValues() const {
    return mPortValues;
}

inline
bool AtomEPort__InterfaceView__portBase_xcommands_xMotion2D::hasPortValues() const {
    return !mPortValues.empty();
}

inline
void AtomEPort__InterfaceView__portBase_xcommands_xMotion2D::addPortValue(PortValue &port) {
    mPortValues.push_back(&port);
}

inline
void AtomEPort__InterfaceView__portBase_xcommands_xMotion2D::clearPortValues() {
    mPortValues.clear();
}

inline
bool AtomEPort__InterfaceView__portBase_xcommands_xMotion2D::isReset() const {
    return mIsReset;
}

inline
void AtomEPort__InterfaceView__portBase_xcommands_xMotion2D::setIsReset(bool b) {
    mIsReset = b;
}
#endif // INCLUDE_INTERFACEVIEW_ATOMEPORT____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

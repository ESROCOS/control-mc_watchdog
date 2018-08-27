#ifndef INCLUDE_INTERFACEVIEW_ATOMEPORT____INTERFACEVIEW____PORT_HPP_
#define INCLUDE_INTERFACEVIEW_ATOMEPORT____INTERFACEVIEW____PORT_HPP_

#include <AtomExportPort.hpp>
#include <InterfaceView/AtomIPort__InterfaceView__Port.hpp>

#include <InterfaceView/PT__InterfaceView__Port.hpp>

class AtomEPort__InterfaceView__Port :
    public virtual Port,
    public AtomExportPort,
    public PT__InterfaceView__Port {
public:
    AtomEPort__InterfaceView__Port(const string &name, bool hasEarlyUpdate, bool hasUrgency);
    virtual ~AtomEPort__InterfaceView__Port();
    virtual void addInternalPort(AtomIPort__InterfaceView__Port &p);

    virtual vector<PortValue *> &portValues();
    virtual const vector<PortValue *> &portValues() const;
    virtual bool hasPortValues() const;
    virtual void addPortValue(PortValue &port);
    virtual void clearPortValues();

    virtual bool isReset() const;
    void setIsReset(bool b);

protected:
// Getting messy to store actual type and return more abstract one (thanks to vector template...)
//    vector<PV__InterfaceView__Port *> mPortValues;
    vector<PortValue *> mPortValues;
    bool mIsReset;
}; 


inline
void AtomEPort__InterfaceView__Port::addInternalPort(AtomIPort__InterfaceView__Port &p) {
    AtomExportPort::addInternalPort(p);
}

inline
vector<PortValue *> &AtomEPort__InterfaceView__Port::portValues() {
    return mPortValues;
}

inline
const vector<PortValue *> &AtomEPort__InterfaceView__Port::portValues() const {
    return mPortValues;
}

inline
bool AtomEPort__InterfaceView__Port::hasPortValues() const {
    return !mPortValues.empty();
}

inline
void AtomEPort__InterfaceView__Port::addPortValue(PortValue &port) {
    mPortValues.push_back(&port);
}

inline
void AtomEPort__InterfaceView__Port::clearPortValues() {
    mPortValues.clear();
}

inline
bool AtomEPort__InterfaceView__Port::isReset() const {
    return mIsReset;
}

inline
void AtomEPort__InterfaceView__Port::setIsReset(bool b) {
    mIsReset = b;
}
#endif // INCLUDE_INTERFACEVIEW_ATOMEPORT____INTERFACEVIEW____PORT_HPP_

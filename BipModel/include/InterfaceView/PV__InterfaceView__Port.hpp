#ifndef INCLUDE_INTERFACEVIEW_PV____INTERFACEVIEW____PORT_HPP_
#define INCLUDE_INTERFACEVIEW_PV____INTERFACEVIEW____PORT_HPP_

#include <PortValue.hpp>

#include <InterfaceView/PT__InterfaceView__Port.hpp>

class AtomExportData;
class AtomExportPort;
class AtomInternalPort;
class AtomExternalPort;

class PV__InterfaceView__Port : public PortValue {
public:
    PV__InterfaceView__Port();
    virtual ~PV__InterfaceView__Port();

    virtual string toString() const;

    virtual bool hasUnmodifiedExportData() const { return false; }
    virtual bool hasUnmodifiedExportPorts() const { return false; }
    virtual bool hasUnmodifiedInternalPorts() const { return false; }
    virtual bool hasUnmodifiedExternalPorts() const { return false; }
    virtual const vector<const AtomExportData *> &unmodifiedExportData() const { vector<const AtomExportData *> *ptr = NULL; return *ptr; }
    virtual const vector<const AtomExportPort *> &unmodifiedExportPorts() const { vector<const AtomExportPort *> *ptr = NULL; return *ptr; }
    virtual const vector<const AtomInternalPort *> &unmodifiedInternalPorts() const { vector<const AtomInternalPort *> *ptr = NULL; return *ptr; }
    virtual const vector<const AtomExternalPort *> &unmodifiedExternalPorts() const {  vector<const AtomExternalPort *> *ptr = NULL; return *ptr; }
    virtual bool unmodifiedInvariant() const { return false; }


private:

}; 




#endif // INCLUDE_INTERFACEVIEW_PV____INTERFACEVIEW____PORT_HPP_

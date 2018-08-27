#ifndef INCLUDE_INTERFACEVIEW_PV____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_
#define INCLUDE_INTERFACEVIEW_PV____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

#include <PortValue.hpp>

#include <InterfaceView/PT__InterfaceView__portBase_xcommands_xMotion2D.hpp>

class AtomExportData;
class AtomExportPort;
class AtomInternalPort;
class AtomExternalPort;

class PV__InterfaceView__portBase_xcommands_xMotion2D : public PortValue {
public:
    PV__InterfaceView__portBase_xcommands_xMotion2D(asn1SccBase_commands_Motion2D &_m_v);
    virtual ~PV__InterfaceView__portBase_xcommands_xMotion2D();

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


    // get/set for data.
    const asn1SccBase_commands_Motion2D& get_v() const;
    asn1SccBase_commands_Motion2D& get_v();
    void set_v(const asn1SccBase_commands_Motion2D &_m_v);

private:
    // data fields from Port type.
    asn1SccBase_commands_Motion2D &m_v;

}; 



    // get/set for data.
inline
const asn1SccBase_commands_Motion2D& PV__InterfaceView__portBase_xcommands_xMotion2D::get_v() const {
    return m_v;
}
inline
asn1SccBase_commands_Motion2D& PV__InterfaceView__portBase_xcommands_xMotion2D::get_v() {
    return m_v;
}
inline
void PV__InterfaceView__portBase_xcommands_xMotion2D::set_v(const asn1SccBase_commands_Motion2D &_m_v) {
    m_v = _m_v;
}


#endif // INCLUDE_INTERFACEVIEW_PV____INTERFACEVIEW____PORTBASE__XCOMMANDS__XMOTION2D_HPP_

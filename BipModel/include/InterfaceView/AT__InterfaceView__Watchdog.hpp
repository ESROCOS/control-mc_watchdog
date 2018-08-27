#ifndef INTERFACEVIEW_AT____INTERFACEVIEW____WATCHDOG_HPP_
#define INTERFACEVIEW_AT____INTERFACEVIEW____WATCHDOG_HPP_

// /home/taste/Documents/ESROCOS/Planetary/BipModel/sources/InterfaceView.bip:59:2
// include package "master" header
#include <InterfaceView.hpp>

#include <Atom.hpp>
#include <TimeValue.hpp>
#include <Interval.hpp>
#include <Clock.hpp>

// User include given in @cpp annotation
#include <ExternInterfaceViewFcns.hpp>
#include <ExternalPortCmdWdog.hpp>

#include <InterfaceView/AtomIPort__InterfaceView__Port.hpp>
#include <InterfaceView/AtomIPort__InterfaceView__portBase_xcommands_xMotion2D.hpp>


#include <InterfaceView/AtomEPort__InterfaceView__Port.hpp>
#include <InterfaceView/AtomEPort__InterfaceView__portBase_xcommands_xMotion2D.hpp>

#include <InterfaceView/PV__InterfaceView__portBase_xcommands_xMotion2D.hpp>
#include <InterfaceView/PV__InterfaceView__Port.hpp>



class AT__InterfaceView__Watchdog : public Atom {
private:
   // internal ports & associated port values
    AtomIPort__InterfaceView__Port &_iport_decl__Watchdog_test_cmd_return;
    PV__InterfaceView__Port _iport_decl_pv__Watchdog_test_cmd_return;
    Interval _iport_decl_guard__Watchdog_test_cmd_return;
    Interval _iport_decl_guard_after_prio__Watchdog_test_cmd_return;
    AtomIPort__InterfaceView__portBase_xcommands_xMotion2D &_iport_decl__Watchdog_mot_cmd_out;
    PV__InterfaceView__portBase_xcommands_xMotion2D _iport_decl_pv__Watchdog_mot_cmd_out;
    Interval _iport_decl_guard__Watchdog_mot_cmd_out;
    Interval _iport_decl_guard_after_prio__Watchdog_mot_cmd_out;
    AtomIPort__InterfaceView__Port &_iport_decl__wdog_timeout;
    PV__InterfaceView__Port _iport_decl_pv__wdog_timeout;
    Interval _iport_decl_guard__wdog_timeout;
    Interval _iport_decl_guard_after_prio__wdog_timeout;
   // external ports
    ExternalPortCmdWdog &_iport_decl__Watchdog_test_cmd_in;
    Interval _iport_decl_guard__Watchdog_test_cmd_in;
    Interval _iport_decl_guard_after_prio__Watchdog_test_cmd_in;

    // exported ports
    AtomEPort__InterfaceView__Port &_eport_decl__Watchdog_test_cmd_return;
    AtomEPort__InterfaceView__portBase_xcommands_xMotion2D &_eport_decl__Watchdog_mot_cmd_out;
public:
    AT__InterfaceView__Watchdog(const string &name , AtomIPort__InterfaceView__Port &_iport_decl__Watchdog_test_cmd_return, AtomIPort__InterfaceView__portBase_xcommands_xMotion2D &_iport_decl__Watchdog_mot_cmd_out, AtomIPort__InterfaceView__Port &_iport_decl__wdog_timeout
                             , ExternalPortCmdWdog &_iport_decl__Watchdog_test_cmd_in
                             , AtomEPort__InterfaceView__Port &_eport_decl__Watchdog_test_cmd_return, AtomEPort__InterfaceView__portBase_xcommands_xMotion2D &_eport_decl__Watchdog_mot_cmd_out
                             
                             );
    virtual ~AT__InterfaceView__Watchdog();

    virtual BipError& execute(PortValue &portValue, const TimeValue &t);
    virtual BipError& execute(AtomExternalPort &portValue, const TimeValue &t);
    virtual BipError& initialize();
    virtual string toString() const;
    const Interval &invariant() const { return mInvariant; }
    bool hasInvariant() const { return false; }
    BipError &resume(const TimeValue &time);
    const Interval &resume() const { return mResume; }

protected:
    void setTime(const TimeValue &time);
    TimeValue mTime;
    Interval mResume;
    Interval mInvariant;

    BipError& update();

    BipError& executeInternalTransitions();
    BipError& checkInvariants();

    const static size_t bvector_size = 6/(8*sizeof(int))+((6%(8*sizeof(int))) > 0 ? 1 : 0);
    int __statesbv[ bvector_size ];

    // component data declarations
    double _id__init_timeout;
    double _id__timeout_val;
    double _id__timeout_eps;
    double _id__timeout;
    asn1SccBase_commands_Motion2D _id__Watchdog_test_cmd_cmd_val;
    asn1SccBase_commands_Motion2D _id__Watchdog_mot_cmd_cmd_val;


    // clocks
    Clock _id__t;


    // enabledness of transitions
    bool _transguard__1;
    bool _transguard__2;
    bool _transguard__3;
    bool _transguard__4;
    Interval _transguard__5;
    bool _transguard__6;
    bool _transguard__7;

    Interval generateInterval(const double &speed, const TimeValue &r, bool open) const;


    // index of the latest executed transition
    int __previous;

    bool atWait() const;
    bool toWait();
    bool fromWait();
    bool atl1() const;
    bool tol1();
    bool froml1();
    bool atl2() const;
    bool tol2();
    bool froml2();
    bool atl3() const;
    bool tol3();
    bool froml3();
    bool atl4() const;
    bool tol4();
    bool froml4();
    bool atl5() const;
    bool tol5();
    bool froml5();
};
inline void AT__InterfaceView__Watchdog::setTime(const TimeValue &t) {
    // logical time should not decrease
    assert(this->mTime <= t);

    // set new logical time
    this->mTime = t;
}

inline Interval AT__InterfaceView__Watchdog::generateInterval(const double &speed, const TimeValue &r, bool open) const {
    if (speed == 0.0) {
        return Interval(r == TimeValue::ZERO);
    }
    else if (speed > 0.0) {
        return Interval(r/speed + this->mTime, TimeValue::MAX, open, false);
    }
    else {
        return Interval(TimeValue::MIN, r/speed + this->mTime, false, open);
    }
}

#endif // INTERFACEVIEW_AT____INTERFACEVIEW____WATCHDOG_HPP_

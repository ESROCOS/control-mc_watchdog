// here we should have includes for all used types
// from all packages.
#include "DeployTypes.hpp"

Component* deploy(int argc, char **argv);
bool isSerializeEnabled();
void serialize(char **buf, size_t *len);
void deserialize(const char *buf, size_t len, const TimeValue &time);

namespace staticallocated{

    // data param for Comp__ROOT./
    

    AtomIPort__InterfaceView__Port iport__ROOT__Watchdog__Watchdog_xtest_xcmd_xreturn("Watchdog_test_cmd_return", false, true);

    AtomIPort__InterfaceView__portBase_xcommands_xMotion2D iport__ROOT__Watchdog__Watchdog_xmot_xcmd_xout("Watchdog_mot_cmd_out", false, true);

    AtomIPort__InterfaceView__Port iport__ROOT__Watchdog__wdog_xtimeout("wdog_timeout", false, true);

    ExternalPortCmdWdog eport__ROOT__Watchdog__Watchdog_xtest_xcmd_xin("Watchdog_test_cmd_in", ERROR); // ExternalPortCmdWdog

    AtomEPort__InterfaceView__Port port__ROOT__Watchdog__Watchdog_xtest_xcmd_xreturn("Watchdog_test_cmd_return", false, true);

    AtomEPort__InterfaceView__portBase_xcommands_xMotion2D port__ROOT__Watchdog__Watchdog_xmot_xcmd_xout("Watchdog_mot_cmd_out", false, true);

    // static init for Atom: Comp__ROOT__Watchdog
    

    AT__InterfaceView__Watchdog Comp__ROOT__Watchdog(
     "Watchdog"
     , iport__ROOT__Watchdog__Watchdog_xtest_xcmd_xreturn, iport__ROOT__Watchdog__Watchdog_xmot_xcmd_xout, iport__ROOT__Watchdog__wdog_xtimeout
     , eport__ROOT__Watchdog__Watchdog_xtest_xcmd_xin
     , port__ROOT__Watchdog__Watchdog_xtest_xcmd_xreturn, port__ROOT__Watchdog__Watchdog_xmot_xcmd_xout
     
     
    );


    // static init for Compound: Comp__ROOT

    CT__InterfaceView__Syst Comp__ROOT(
      "ROOT"
     , Comp__ROOT__Watchdog
     
     
     
     
     
     
    );


// End of namespace.
};

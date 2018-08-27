#include "Deploy.hpp"

#include <Launcher.hpp>

/*
 * The "static" includes (the one we use inconditionnaly)
 */


Component* deploy(int argc __attribute__((unused)), char **argv __attribute__((unused))){
    // Top is Comp__ROOT




    staticallocated::eport__ROOT__Watchdog__Watchdog_xtest_xcmd_xin.setHasEarlyUpdate(false);
    staticallocated::eport__ROOT__Watchdog__Watchdog_xtest_xcmd_xin.setHasUrgency(true);

    staticallocated::port__ROOT__Watchdog__Watchdog_xtest_xcmd_xreturn.addInternalPort(staticallocated::iport__ROOT__Watchdog__Watchdog_xtest_xcmd_xreturn);

    staticallocated::port__ROOT__Watchdog__Watchdog_xmot_xcmd_xout.addInternalPort(staticallocated::iport__ROOT__Watchdog__Watchdog_xmot_xcmd_xout);

    // Runtime init for Atom: Comp__ROOT__Watchdog
    // staticallocated::Comp__ROOT__Watchdog


    // Runtime init for Compound: Comp__ROOT
    // staticallocated::Comp__ROOT

    // Finished: Comp__ROOT
    return &(staticallocated::Comp__ROOT);
}

bool isSerializeEnabled() {
    return false;
}

void serialize(char **cbuf __attribute__((unused)), size_t *clen __attribute__((unused))){
    assert(false);
}

void deserialize(const char *buf __attribute__((unused)), size_t len __attribute__((unused)), const TimeValue &time){
    assert(false);
}

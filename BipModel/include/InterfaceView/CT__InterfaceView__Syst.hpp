#ifndef INTERFACEVIEW_CT____INTERFACEVIEW____SYST_HPP_
#define INTERFACEVIEW_CT____INTERFACEVIEW____SYST_HPP_

// /home/taste/Documents/ESROCOS/Planetary/BipModel/sources/InterfaceView.bip:126:2
// include package "master" header
#include <InterfaceView.hpp>

#include <Compound.hpp>

// User include given in @cpp annotation
#include <ExternInterfaceViewFcns.hpp>
#include <ExternalPortCmdWdog.hpp>

// for component types
#include <InterfaceView/AT__InterfaceView__Watchdog.hpp>


class CT__InterfaceView__Syst : public Compound {
public:
    CT__InterfaceView__Syst (const string &name, AT__InterfaceView__Watchdog &_comp_decl__Watchdog
                                  
                                  
                                  
                                  
                                  
    
    );
    virtual ~CT__InterfaceView__Syst();


private:

    // SubComponent decls
    AT__InterfaceView__Watchdog &_comp_decl__Watchdog;
};



#endif // INTERFACEVIEW_CT____INTERFACEVIEW____SYST_HPP_

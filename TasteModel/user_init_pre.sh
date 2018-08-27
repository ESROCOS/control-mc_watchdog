ORCHESTRATOR_OPTIONS+=" --no-retry"
ORCHESTRATOR_OPTIONS+=" -e x86_functional:$PWD/../BipModel/include"
ORCHESTRATOR_OPTIONS+=" -e x86_functional:$PWD/../BipEngine/include/generic"
ORCHESTRATOR_OPTIONS+=" -e x86_functional:$PWD/../BipEngine/include/specific"
ORCHESTRATOR_OPTIONS+=" -l x86_functional:$PWD/../BipModel/lib/libpack__InterfaceView.a"
ORCHESTRATOR_OPTIONS+=" -l x86_functional:$PWD/../BipEngine/lib/libengine.a"

echo "ORCHESTRATOR_OPTIONS=$ORCHESTRATOR_OPTIONS"

-- This file was generated automatically: DO NOT MODIFY IT !

with Base_Types;
use Base_Types;
with TASTE_ExtendedTypes;
use TASTE_ExtendedTypes;
with TASTE_BasicTypes;
use TASTE_BasicTypes;
with UserDefs_Base_Types;
use UserDefs_Base_Types;
with adaasn1rtl;
use adaasn1rtl;



package joystickdriver is
    --  Provided interface "step"
    procedure step;
    pragma Export(C, step, "joystickdriver_step");
    --  Required interface "cmd"
    procedure RI�cmd(cmd_val: access asn1SccBase_commands_Motion2D);
    pragma import(C, RI�cmd, "joystickdriver_RI_cmd");
end joystickdriver;
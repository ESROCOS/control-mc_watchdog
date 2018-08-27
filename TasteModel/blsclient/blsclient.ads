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



package blsclient is
    --  Provided interface "mot_cmd"
    procedure mot_cmd(cmd_val: access asn1SccBase_commands_Motion2D);
    pragma Export(C, mot_cmd, "blsclient_mot_cmd");
end blsclient;
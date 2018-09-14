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



package cmddispatcher is
   --  Provided interface "cmd"
   procedure cmd(cmd_val: access asn1SccBase_commands_Motion2D);
   pragma Export(C, cmd, "cmddispatcher_PI_cmd");
   --  Required interface "log_cmd"
   procedure RIÜlog_cmd(cmd_val: access asn1SccBase_commands_Motion2D);
   pragma import(C, RIÜlog_cmd, "cmddispatcher_RI_log_cmd");
   --  Required interface "test_cmd"
   procedure RIÜtest_cmd(cmd_val: access asn1SccBase_commands_Motion2D);
   pragma import(C, RIÜtest_cmd, "cmddispatcher_RI_test_cmd");
end cmddispatcher;
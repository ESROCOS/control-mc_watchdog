-- This file was generated automatically: DO NOT MODIFY IT !

with System.IO;
use System.IO;

with Ada.Unchecked_Conversion;
with Ada.Numerics.Generic_Elementary_Functions;

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

with Interfaces;
use Interfaces;

package body logger is
   type States is (wait);
   type ctxt_Ty is
      record
      state : States;
      initDone : Boolean := False;
      v : aliased asn1SccBase_commands_Motion2D;
   end record;
   ctxt: aliased ctxt_Ty;
   CS_Only  : constant Integer := 2;
   procedure runTransition(Id: Integer);
   procedure log_cmd(cmd_val: access asn1SccBase_commands_Motion2D) is
      begin
         case ctxt.state is
            when wait =>
               ctxt.v := cmd_val.all;
               runTransition(1);
            when others =>
               runTransition(CS_Only);
         end case;
      end log_cmd;
      

   procedure runTransition(Id: Integer) is
      trId : Integer := Id;
      begin
         while (trId /= -1) loop
            case trId is
               when 0 =>
                  --  NEXT_STATE Wait (11,18) at 320, 60
                  trId := -1;
                  ctxt.state := Wait;
                  goto next_transition;
               when 1 =>
                  --  writeln('Logging', v!translation, v!rotation, v!heading!rad) (17,17)
                  Put("Logging");
                  Put(asn1SccT_Double'Image(ctxt.v.translation));
                  Put(asn1SccT_Double'Image(ctxt.v.rotation));
                  Put(asn1SccT_Double'Image(ctxt.v.heading.rad));
                  New_Line;
                  --  NEXT_STATE Wait (19,22) at 552, 175
                  trId := -1;
                  ctxt.state := Wait;
                  goto next_transition;
               when CS_Only =>
                  trId := -1;
                  goto next_transition;
               when others =>
                  null;
            end case;
            <<next_transition>>
            null;
         end loop;
      end runTransition;
      

   begin
      runTransition(0);
      ctxt.initDone := True;
end logger;
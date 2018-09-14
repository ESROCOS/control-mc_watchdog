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

package body joystickdriver is
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
   procedure step is
      begin
         case ctxt.state is
            when wait =>
               runTransition(1);
            when others =>
               runTransition(CS_Only);
         end case;
      end step;
      

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
                  --  v!translation := 2.0 (17,17)
                  ctxt.v.translation := 2.0;
                  --  v!rotation := 3.0 (18,0)
                  ctxt.v.rotation := 3.0;
                  --  v!heading!rad :=0.5 (19,0)
                  ctxt.v.heading.rad := 0.5;
                  --  cmd(v) (21,19)
                  RIÜcmd(ctxt.v'Access);
                  --  NEXT_STATE Wait (23,22) at 450, 258
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
end joystickdriver;
#############################################################################
##
#W /etc/scscp/gap/server.g                                             Debian
##
#############################################################################

#############################################################################
#
# This is a simple sample SCSCP server configuration file.
#
#############################################################################

#############################################################################
#
# The service provider can start the server just by the command
# $ gap /etc/scscp/gap/server.g
#
#############################################################################

#############################################################################
#
# Load necessary packages and read external files.
# Put here and other commands if needed.
#
#############################################################################

LogTo(); # to close log file if it was opened from .gaprc
LoadPackage("scscp");

#############################################################################
#
# Procedures and functions available for the SCSCP server
# (you can also install procedures contained in other files,
# including standard GAP procedures and functions) by adding
# appropriate calls to InstallSCSCPprocedure below.
#
#############################################################################


#############################################################################
SCSCPadditionService:=function(a,b)
return a+b;
end;

#############################################################################
#
# Installation of procedures to make them available for WS
# (you can also install procedures contained in other files,
# including standard GAP procedures and functions)
#
#############################################################################

# Simple procedures for tests and demos
InstallSCSCPprocedure( "Identity", x -> x, "Identity procedure for tests", 1, 1 );
InstallSCSCPprocedure( "WS_Factorial", Factorial, "See ?Factorial in GAP", 1, 1 );
InstallSCSCPprocedure( "addition", SCSCPadditionService, "to add two integers", 2, 2 );
InstallSCSCPprocedure( "WS_Phi", Phi, "Euler's totient function, see ?Phi in GAP", 1, 1 );
InstallSCSCPprocedure( "Length", Length, 1, 1 );
InstallSCSCPprocedure( "Size", Size, 1, 1 );
InstallSCSCPprocedure( "IsPrimeInt", IsPrimeInt, 1, 1 );
InstallSCSCPprocedure( "NextPrimeInt", NextPrimeInt, 1, 1 );
InstallSCSCPprocedure( "PrevPrimeInt", PrevPrimeInt, 1, 1 );


###########################################################################
# Series of factorisation methods from the GAP package FactInt
if LoadPackage("factint") = true then
  InstallSCSCPprocedure("WS_FactorsTD", FactorsTD,
	  "FactorsTD from FactInt package, see ?FactorsTD in GAP", 1, 2 );
  InstallSCSCPprocedure("WS_FactorsPminus1", FactorsPminus1,
	  "FactorsPminus1 from FactInt package, see ?FactorsPminus1 in GAP", 1, 4 );
  InstallSCSCPprocedure("WS_FactorsPplus1", FactorsPplus1,
	  "FactorsPplus1 from FactInt package, see ?FactorsPplus1 in GAP", 1, 4 );
  InstallSCSCPprocedure("WS_FactorsECM", FactorsECM,
	  "FactorsECM from FactInt package, see ?FactorsECM in GAP", 1, 5 );
  InstallSCSCPprocedure("WS_FactorsCFRAC", FactorsCFRAC,
	  "FactorsCFRAC from FactInt package, see ?FactorsCFRAC in GAP", 1, 1 );
  InstallSCSCPprocedure("WS_FactorsMPQS", FactorsMPQS,
	  "FactorsMPQS from FactInt package, see ?FactorsMPQS in GAP", 1, 1 );
fi;

#############################################################################
#
# Finally, we start the SCSCP server.
#
#############################################################################

RunSCSCPserver( SCSCPserverAddress, SCSCPserverPort );

#############################################################################
##
#E
##

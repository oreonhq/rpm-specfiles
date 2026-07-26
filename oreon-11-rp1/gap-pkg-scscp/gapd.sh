#!/bin/sh
###########################################################################
scriptversion="2.1.4 (Debian @DEB_PKG_VERSION@)"
###########################################################################
##
#W gapd                   The SCSCP package             Alexander Konovalov
#W                                                             Steve Linton
##
## gapd [-h host] [-a] [-l] [-u] [-p port] [-t]
##
## The following options may be used to overwrite the default method to
## specify the hostname to run GAP SCSCP server, stated in scscp/config.g :
##
## 1) if '-h host' is specified, then the server will be started at 'host'.
##    'host' may be given as machine name with or without domain or even as
##    'localhost', though we have -l option for that purpose
##
## 2) if '-a' is specified, then the output of the call to 'hostname' will
##    be used as the SCSCP server address
##
## 3) if '-l' is specified, then the server will be started at localhost
##    and will not accept any incoming connections from the outside
##
## 4) if '-u' is specified, the server will be started in a "universal"
##    mode and will accept all incoming connections
##
## The options 1-4 above are incompatible, so in case several of them will
## be given, only the option with the biggest number will be used
##
## If none of the options 1-4 above is stated, the hostname for the server
## will be taken from the scscp/config.g file
##
## Additionally, you may use the following options:
##
## 5) if '-p port' is specified, this will overwrite the default port for
##    the SCSCP server given in scscp/config.g
##
## 6) if '-t' is specified then the output will be redirected to a
##    temporary file, which name will be displayed on screen during
##    startup. Otherwise, by default it will be redirected to /dev/null
##
###########################################################################
##
##  modified on behalf of Debian by Jerome Benoit <calculus@rezozer.net>
##
###########################################################################
scriptname=${0##*/}
###########################################################################
##
## PART 0. DAEMON VARIABLES
##
###########################################################################
##
CONFDIR=/etc/scscp/gap
LOGDIR=/var/log/gapd
LOGFILE=$LOGDIR/gapd.log
##
###########################################################################

###########################################################################
## USAGE
###########################################################################
##
## usage string formatted with help2man in mind
usage="\
Usage: $scriptname [-h HOST|-a|-l|-u] [-p PORT] [-t [MODE]] \
[--infolevel[-scscp|-master] LEVEL] [--help] [--version]

GAP Daemon - GAP SCSCP server daemon

Options:
   -h HOST\tStart at host HOST: HOST may be given as machine name with or
          \twithout domain or as 'localhost' (see option -l for that purpose).
   -a     \tSet server address to the one given by hostname(1).
   -l     \tStart at localhost: reject incoming any connection from the outside.
   -u     \tStart in \`universal' mode: accept all incoming connections.

   -p PORT\tSet server port to PORT, default port set in \`${CONFDIR}/config.g'.

   -t MODE\tRedirect the server session output according to the following MODEs:
          \tMODE=no sink the output to \`/dev/null' (default behaviour);
          \tMODE=log redirect the output to \`${LOGFILE}';
          \tMODE=yes redirect the output to a temporary file, which name is displayed
          \t(and printed to \`${LOGFILE}' for granted users);
          \tthe implicit mode is MODE=yes for backward compatibility.

   --infolevel-scscp LEVEL  \tSet the GAP InfoLevel for SCSCP to LEVEL.
   --infolevel-master LEVEL \tSet the GAP InfoLevel for MasterWorker to LEVEL.
   --infolevel LEVEL        \tIndiscriminately set the GAP InfoLevel_s to LEVEL.

   --help    \tPrint this help text and exit.
   --version \tOutput version information and exit.

"
##
###########################################################################

###########################################################################
##
## PART 1. MODIFY PATHS IF NEEDED
##
###########################################################################
##
##  Define the local call of GAP and call options, if necessary, for
##  example, memory usage, start with the workspace etc. The path may be
##  relative (to start from this directory) or absolute.
##
CGAP=/usr/bin/gap
GAP="$CGAP -b -r"
##
###########################################################################
##
##  Define the configuration file for the SCSCP server. Note that since GAP
##  reads the configuration file immediately before starting SCSCP server,
##  you may redefine in it all variables that were set to their default
##  values in scscp/config.g and scscp/configpar.g files (explicitly or
##  reading your appropriately modified private copies of that files).
##  The path may be relative (to start from this directory) or absolute.
##
SCSCP_CONFIG=${CONFDIR}/server.g
##
##
###########################################################################

###########################################################################
##
## PART 2. YOU NEED NOT TO MODIFY ANYTHING BELOW
##
###########################################################################
##
##  Parse the arguments.
##
autohost="no"
localhost="no"
unimode="no"
use_temp_file="no"
host=";"
port=";"
infolevel_scscp=0
infolevel_master=0

option="yes"
while [ $option = "yes" ]; do
  option="no"
  case $1 in
    -a) shift; option="yes"; autohost="yes";;
    -h) shift; option="yes"; host=":=\""$1"\";"; shift;;
    -l) shift; option="yes"; localhost="yes";;
    -u) shift; option="yes"; unimode="yes";;
    -p) shift; option="yes"; port=":="$1";"; shift;;
    -t) shift; option="yes";
        if [ 0 -lt $# ]; then
          case "$1" in
            -*) ;;
					  *)
              case "$1" in
                l|lo|log) use_temp_file="log" ;;
                n|no) use_temp_file="no" ;;
                y|ye|yes|*) use_temp_file="yes" ;;
              esac
						  shift
              ;;
          esac
				else
				  use_temp_file="yes"
				fi
				;;
		--infolevel-scscp) shift; option="yes"; infolevel_scscp=$1; shift;;
		--infolevel-master) shift; option="yes"; infolevel_master=$1; shift;;
		--infolevel) shift; option="yes";
				infolevel_scscp=$1; shift; infolevel_master=$infolevel_scscp;;
		--help) echo "$usage"; exit $?;;
		--version) echo "$scriptname $scriptversion"; exit $?;;
  esac
done

if [ -n "${TMPDIR}" -a ! -w "${TMPDIR}" ]; then
	unset TMPDIR
fi

case "$use_temp_file" in
	log)
		OUTFILE=${LOGFILE}
		;;
	yes)
		OUTFILE=$(mktemp --quiet --tmpdir gapd-XXXXXXXXXXX.log)
		if [ -w ${LOGFILE} ]; then
			cat >> ${LOGFILE} <<- EOM
				#############################################################
				#D  log: ${OUTFILE}
				EOM
		fi
		echo "Starting SCSCP server with output to ${OUTFILE}"
		;;
	*)
		OUTFILE="/dev/null"
		;;
esac

if [ $autohost = "yes" ]; then
	host=":=Hostname();"
fi;

if [ $localhost = "yes" ]; then
	host=":=false;"
fi;

if [ $unimode = "yes" ]; then
	host=":=true;"
fi;

if [ $infolevel_scscp -lt 0 ]; then
	infolevel_scscp=0
fi;

if [ $infolevel_master -lt 0 ]; then
	infolevel_master=0
fi;

# Check whether ${OUTFILE} is writable
if [ -e ${OUTFILE} ]; then
	if [ ! -w ${OUTFILE} ]; then
		echo "the GAP daemon gapd can not write to the file ${OUTFILE}" 1>&2
		exit 2
	fi
else
	OUTFOLDER=$(dirname ${OUTFILE})
	if [ ! -w ${OUTFOLDER} ]; then
		echo "the GAP daemon gapd can not write into the folder ${OUTFILE}" 1>&2
		exit 2
	fi
fi

# Check whether the GAP system is available
if [ ! -x $CGAP ]; then
	echo "the GAP command-line interface $CGAP can not be executed" 1>&2
	exit 2
fi

# Check whether the server configuration file is readable
if [ ! -r "${SCSCP_CONFIG}" ]; then
	echo "the GAP SCSCP server configuration file ${SCSCP_CONFIG} can not be read" 1>&2
	exit 2
fi

cat >> ${OUTFILE} <<- EOM
	#############################################################
	#D  script: ${0} (${scriptversion})
	#D  date: $(date -u +%Y%m%dT%H%M%S.%NZ)
	#D  host: $(hostname)
	#D  user: $(id -un)
	#D  infolevel: SCSCP: ${infolevel_scscp}
	#D  infolevel: MasterWorker: ${infolevel_master}
	#D  TMPDIR: ${TMPDIR}
	EOM

exec $GAP -q >> ${OUTFILE} 2>&1 <<-EOGS &
	LoadPackage("scscp");;
	SetInfoLevel(InfoSCSCP,${infolevel_scscp});
	SetInfoLevel(InfoMasterWorker,${infolevel_master});
	SCSCPserverAddress${host};
	SCSCPserverPort${port};
	Read("${SCSCP_CONFIG}");
	if SCSCPserverStatus=fail then
			QUIT_GAP();
	fi;
EOGS

###########################################################################
##
#E
##

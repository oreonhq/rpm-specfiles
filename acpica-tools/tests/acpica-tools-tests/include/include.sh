#!/bin/bash
# /Coreos/acpica-tools/acpica-tools-tests/include/include.sh
# Constants
########################################
# - debug turn off SELinux
#setenforce 0
########################################

# Source the common test script helpers
. /usr/bin/rhts_environment.sh
. /usr/share/beakerlib/beakerlib.sh

# Assume the test will fail.
DeBug=0 # Set to 1 to gather all logs from all tests.
packagename=acpica-tools
RPM_NAME=`rpm -q --queryformat '%{name}\n' $packagename`
RPM_VER=`rpm -q --queryformat '%{version}\n' $packagename`
RPM_REL=`rpm -q --queryformat '%{release}\n' $packagename`
#RPM_ARCH=`rpm -q --queryformat '%{arch}\n' $packagename`
OUTPUTDIR=/mnt/testarea/acpica-tools-tests

# Functions


# Make log and output directories if needed
function mk_test_dirs()
{
if test ! -d $OUTPUTDIR ; then
    echo "Creating $OUTPUTDIR" | tee -a $OUTPUTFILE
    mkdir -p $OUTPUTDIR || rlDie "Can't create directory ${OUTPUTDIR}!"
fi
log_dir=${OUTPUTDIR}/logs/${TESTNAME}-${$}
if test ! -d $log_dir ; then
    echo "Creating $log_dir" | tee -a $OUTPUTFILE 
    mkdir -p $log_dir || rlDie "Can't create directory ${log_dir}!"
fi
RPMBUILDDIR=${OUTPUTDIR}/rpmbuild
if test ! -d $RPMBUILDDIR ; then
    echo "Creating RPM build directorires" | tee -a $OUTPUTFILE
    mkdir -p $RPMBUILDDIR/{BUILD,BUILDROOT,RPMS,SPECS,SOURCES,SRPMS} || rlDie "Can't create RPM build directories"
fi
export OUTPUTDIR log_dir RPMBUILDDIR
}

# Grab src rpm from brew using wget requires package n v r  
function get_srpm_from_koji()
{
    local name=$1
    local version=$2
    local release=$3
    local wget_opts="-Nnv"
    local url2srcfile="http://kojipkgs.fedoraproject.org/packages/${name}/${version}/${release}/src/${name}-${version}-${release}.src.rpm"
    wget $wget_opts $url2srcfile >> $OUTPUTFILE 2>&1
    if [ "$?" -eq "0" ] ; then
        echo "***** Successfully downloaded ${name}-${version}-${release}.src.rpm from brewroot *****" | tee -a $OUTPUTFILE
    fi
}

# Install a src.rpm to a given buildroot
# Requires path to src.rpm and an existing buildroot directory to install to.
function install_srpm()
{
 local srpm=$1
 local buildroot=$2
 if [ -d "$buildroot" ] ; then
   if [ -e $srpm ] ; then
       rpm --define "_topdir $RPMBUILDDIR" -ivh $srpm
       if [ "$?" -eq "0" ] ; then
           echo "***** Successfully installed $srpm *****" | tee -a $OUTPUTFILE
       else
           echo "***** Unable to install $srpm *****" | tee -a $OUTPUTFILE
           return 1
       fi
   else
       echo "***** $srpm file not found *****" | tee -a $OUTPUTFILE
       return 1
   fi
 else 
    echo "***** $buildroot does not exist *****" | tee -a $OUTPUTFILE
       return 1
 fi 
}

# run rpm -bp on extracted acpi-tools src.rpm if needed
function rpmbp_acpica-tools()
{
  rpmbuild --define "_topdir $RPMBUILDDIR" -bp $RPMBUILDDIR/SPECS/acpica-tools.spec > ${log_dir}/rpm-bp-acpica-tools-${$}.log 2>&1
  [ $? -eq 0 ] && return 0 || return 1
}

function acpica-tools_prep()
{
  if [ ! -d ${RPMBUILDDIR}/BUILD/acpica-unix2-${RPM_VER} ] ; then
    rlRun "get_srpm_from_koji $RPM_NAME $RPM_VER $RPM_REL"
    rlRun "install_srpm ${RPM_NAME}-${RPM_VER}-${RPM_REL}.src.rpm $RPMBUILDDIR"
    rlRun rpmbp_acpica-tools
  else 
    rlLog "acpica-tools source tree is already prepared for testing, skipping acpica-tools_prep()"
  fi
}


# wrapper around rlFileSubmit to preserve path names of the log files and submit all files in the log directory
function submit_logs()
{
  for f in $log_dir/*; do
    if [ -f $f ] ; then
      rlFileSubmit $f
    fi
  done
}


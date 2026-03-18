# pegasus_rpm_build_env.sh:
#
# Open Pegasus RPM %build + %install environment setup.
#
# Expects these variables to be set on entry:
#    RPM_ARCH      : rpmbuild architecture identifier
#    RPM_OPT_FLAGS : rpmbuild compile options
#    RPM_BUILD_DIR : rpmbuild source directory
#    RPM_BUILD_ROOT: rpmbuild build destination directory
#    RPM_ARCH_LIB  : %{_lib} : lib or lib64
#    SRCNAME       : name of pegasus source directory
#    
# compile options:
#
export PEGASUS_EXTRA_C_FLAGS="$RPM_OPT_FLAGS -Wno-unused"
export PEGASUS_EXTRA_CXX_FLAGS="$PEGASUS_EXTRA_C_FLAGS"
export PEGASUS_EXTRA_PROGRAM_LINK_FLAGS="-pie -Wl,-z,relro,-z,now,-z,nodlopen,-z,noexecstack"
export SYS_INCLUDES=-I/usr/kerberos/include
#
# build object directories:
#
SRCNAME=${SRCNAME:-pegasus}
export PEGASUS_ROOT=${RPM_BUILD_DIR}/${SRCNAME}
export PEGASUS_HOME=${RPM_BUILD_DIR}/${SRCNAME}/build
#
# build time settings:
export PEGASUS_ARCH_LIB=${RPM_ARCH_LIB:-lib}
export PEGASUS_ENVVAR_FILE=${PEGASUS_ROOT}/env_var_Linux.status
export OPENSSL_HOME=/usr
export OPENSSL_BIN=/usr/bin
export LD_LIBRARY_PATH=${PEGASUS_HOME}/lib
export PATH=${PEGASUS_HOME}/bin:${PATH}
#
# PEGASUS_PLATFORM (hardware platform) setup:
#
if [ -z "$RPM_ARCH" ]; then
    export RPM_ARCH=`/bin/uname -i`;
fi;
case ${RPM_ARCH} in
  ia64)
    export PEGASUS_PLATFORM=LINUX_IA64_GNU;
    ;;
  x86_64)
    export PEGASUS_PLATFORM=LINUX_X86_64_GNU;
    ;;
  ppc)
    export PEGASUS_PLATFORM=LINUX_PPC_GNU;
    ;;
  ppc64|ppc64le|pseries)
    export PEGASUS_PLATFORM=LINUX_PPC64_GNU;
    ;;
  s390)
    export PEGASUS_PLATFORM=LINUX_ZSERIES_GNU;
    export PEGASUS_EXTRA_C_FLAGS="$PEGASUS_EXTRA_C_FLAGS -fsigned-char";
    export PEGASUS_EXTRA_CXX_FLAGS="$PEGASUS_EXTRA_C_FLAGS";
    ;;
  s390x|zseries)
    export PEGASUS_PLATFORM=LINUX_ZSERIES64_GNU;
    export PEGASUS_EXTRA_C_FLAGS="$PEGASUS_EXTRA_C_FLAGS -fsigned-char";
    export PEGASUS_EXTRA_CXX_FLAGS="$PEGASUS_EXTRA_C_FLAGS";
    ;;
  i386)
    export PEGASUS_PLATFORM=LINUX_IX86_GNU
    ;;
  *)
    echo "Architecture unsupported by pegasus: $RPM_ARCH";
    exit 1;
    ;;
esac;

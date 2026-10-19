%global source0_hash 9f2f13a35da218f3cb6e8478246ff7c4d3010560bb4d5de9cbf4272d48e353fb
%global source9_hash c1f4a0e1a5ac470ba543c59c499d2f1691890b9caa6e3c37bd7ee6e43b57650e
%{?!PEGASUS_BUILD_TEST_RPM:     %global PEGASUS_BUILD_TEST_RPM        1}
%global srcname pegasus
%global major_ver 2.14
Name:           tog-pegasus
Version:        %{major_ver}.1
Release:        89%{?dist}
Epoch:          2
Summary:        OpenPegasus WBEM Services for Linux
License:        MIT
URL:            http://www.openpegasus.org
Source0:        https://collaboration.opengroup.org/pegasus/documents/32572/pegasus-%{version}.tar.gz
Source1:        README.RedHat.Security
Source3:        README.RedHat.SSL
Source4:        tog-pegasus.tmpfiles
Source5:        tog-pegasus.service
Source6:        access.conf
Source7:        cimprovagt-wrapper.sh
Source8:        cmpiOSBase_OperatingSystemProvider-cimprovagt.example
Source9:        https://www.dmtf.org/sites/default/files/cim/cim_schema_v2380/cim_schema_2.38.0Experimental-MOFs.zip
Source10:        generate-certs
Source11:        snmptrapd.conf
Source12:        repupgrade.1.gz
Source13:        tog-pegasus.sysusers
Patch1:         pegasus-2.9.0-no-rpath.patch
Patch2:         pegasus-2.7.0-PIE.patch
Patch3:         pegasus-2.9.0-redhat-config.patch
Patch4:         pegasus-2.9.0-cmpi-provider-lib.patch
Patch5:         pegasus-2.9.0-local-or-remote-auth.patch
Patch6:         pegasus-2.5.1-pam-wbem.patch
Patch12:        pegasus-2.7.0-snmp-tests.patch
Patch13:        pegasus-2.9.0-sparc.patch
Patch16:        pegasus-2.9.1-getpagesize.patch
Patch19:        pegasus-2.10.0-dont-strip.patch
Patch20:        pegasus-2.10.0-sparc-posix-lock.patch
Patch22:        pegasus-2.12.0-null_value.patch
Patch24:        pegasus-2.12.0-empty_arrays.patch
Patch25:        pegasus-2.12.0-cimmofl-allow-experimental.patch
Patch26:        pegasus-2.12.0-schema-version-and-includes.patch
Patch29:        pegasus-2.13.0-enable-subscriptions-for-nonprivileged-users.patch
Patch33:        pegasus-2.13.0-gcc5-build.patch
Patch34:        pegasus-2.14.1-build-fixes.patch
Patch35:        pegasus-2.14.1-ssl-include.patch
Patch36:        pegasus-2.14.1-snmpv3-trap.patch
Patch37:        pegasus-2.14.1-fix-setup-sdk.patch
Patch38:        pegasus-2.14.1-cimconfig-man-page-fixes.patch
Patch39:        pegasus-2.14.1-fix-setup-sdk-ppc64le.patch
Patch40:        pegasus-2.14.1-tesid.patch
Patch41:        pegasus-2.14.1-ssl-cert-path.patch
Patch42:        pegasus-2.14.1-openssl-1.1-fix.patch
Patch43:        pegasus-2.14.1-fix-Wreserved-user-defined-literal.patch
Patch44:        pegasus-2.14.1-crypto-policy-compliance.patch
Patch45:        pegasus-2.14.1-add-pegwsmserver-to-ldd-libs.patch
Patch46:        pegasus-2.14.1-build-fixes-2.patch
Patch47:        pegasus-2.14.1-snmp-disable-des.patch
Patch48:        add-riscv64-support.patch
Patch49:        tog-pegasus-2.14.1-bin-sbin-unify.patch
Patch50:        pegasus-2.14.1-ssl-certs-gen-changes.patch
Patch51:        pegasus-2.14.1-post-quantum.patch
Requires:       net-snmp-libs
Requires:       %{name}-libs = %{epoch}:%{version}-%{release}
Requires:       openssl
Requires:       ca-certificates
Provides:       cim-server = 1
Requires(post): /usr/bin/ldconfig
Requires(post): /usr/bin/restorecon
# oreon:deps
BuildRequires:  bash
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  grep
BuildRequires:  libstdc++
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  net-snmp-devel
BuildRequires:  openslp-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  procps
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  systemd-units
# /oreon:deps
%description
OpenPegasus WBEM Services for Linux enables management solutions that deliver
increased control of enterprise resources. WBEM is a platform and resource
independent DMTF standard that defines a common information model and
communication protocol for monitoring and controlling resources from diverse
sources.

%package devel
Summary:        The OpenPegasus Software Development Kit
Requires:       tog-pegasus >= %{epoch}:%{version}-%{release}
%description devel
The OpenPegasus WBEM Services for Linux SDK is the developer's kit for the
OpenPegasus WBEM Services for Linux release. It provides Linux C++ developers
with the WBEM files required to build WBEM Clients and Providers. It also
supports C provider developers via the CMPI interface.

%package libs
Summary:        The OpenPegasus Libraries
Conflicts:      libcmpiCppImpl0
Requires(pre):  /usr/bin/useradd
Requires(pre):  /usr/bin/groupadd
Requires(post): /usr/bin/ldconfig
%description libs
The OpenPegasus libraries.

%if %{PEGASUS_BUILD_TEST_RPM}
%package test
Summary:        The OpenPegasus Tests
Requires:       tog-pegasus >= %{epoch}:%{version}-%{release}, make
Requires:       %{name}-libs = %{epoch}:%{version}-%{release}
%description test
The OpenPegasus WBEM tests for the OpenPegasus %{version} Linux rpm.
%endif

%ifarch ia64
%global PEGASUS_HARDWARE_PLATFORM LINUX_IA64_GNU
%endif
%ifarch x86_64
%global PEGASUS_HARDWARE_PLATFORM LINUX_X86_64_GNU
%endif
%ifarch ppc
%global PEGASUS_HARDWARE_PLATFORM LINUX_PPC_GNU
%endif
%ifarch ppc64
%global PEGASUS_HARDWARE_PLATFORM LINUX_PPC64_GNU
%endif
%ifarch ppc64le
%global PEGASUS_HARDWARE_PLATFORM LINUX_PPC64_GNU
%endif
%ifarch s390
%global PEGASUS_HARDWARE_PLATFORM LINUX_ZSERIES_GNU
%endif
%ifarch s390x
%global PEGASUS_HARDWARE_PLATFORM LINUX_ZSERIES64_GNU
%endif
%ifarch sparcv9
%global PEGASUS_HARDWARE_PLATFORM LINUX_SPARCV9_GNU
%endif
%ifarch sparc64
%global PEGASUS_HARDWARE_PLATFORM LINUX_SPARC64_GNU
%endif
%ifarch %{ix86}
%global PEGASUS_HARDWARE_PLATFORM LINUX_IX86_GNU
%endif
%ifarch %{arm}
%global PEGASUS_HARDWARE_PLATFORM LINUX_XSCALE_GNU
%endif
%ifarch aarch64
%global PEGASUS_HARDWARE_PLATFORM LINUX_AARCH64_GNU
%endif
%ifarch riscv64
%global PEGASUS_HARDWARE_PLATFORM LINUX_RISCV64_GNU
%endif

%global PEGASUS_ARCH_LIB %{_lib}
%global OPENSSL_HOME /usr
%global OPENSSL_BIN /usr/bin
%global PEGASUS_PEM_DIR /etc/pki/Pegasus
%global PEGASUS_SSL_CERT_FILE server.pem
%global PEGASUS_SSL_KEY_FILE file.pem
%global PEGASUS_SSL_TRUSTSTORE client.pem
%global PAM_CONFIG_DIR /etc/pam.d
%global PEGASUS_CONFIG_DIR /etc/Pegasus
%global PEGASUS_VARDATA_DIR /var/lib/Pegasus
%global PEGASUS_VARDATA_CACHE_DIR /var/lib/Pegasus/cache
%global PEGASUS_LOCAL_DOMAIN_SOCKET_PATH  /var/run/tog-pegasus/socket/cimxml.socket
%global PEGASUS_CIMSERVER_START_FILE /var/run/tog-pegasus/cimserver.pid
%global PEGASUS_TRACE_FILE_PATH /var/lib/Pegasus/cache/trace/cimserver.trc
%global PEGASUS_CIMSERVER_START_LOCK_FILE /var/run/tog-pegasus/cimserver_start.lock
%global PEGASUS_REPOSITORY_DIR /var/lib/Pegasus/repository
%global PEGASUS_PREV_REPOSITORY_DIR_NAME prev_repository
%global PEGASUS_REPOSITORY_PARENT_DIR /var/lib/Pegasus
%global PEGASUS_PREV_REPOSITORY_DIR /var/lib/PegasusXXX/prev_repository
%global PEGASUS_DOC_DIR /usr/share/doc/%{name}-%{version}

%global PEGASUS_RPM_ROOT $RPM_BUILD_DIR/%{srcname}
%global PEGASUS_RPM_HOME %PEGASUS_RPM_ROOT/build
%global PEGASUS_INSTALL_LOG /var/lib/Pegasus/log/install.log

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source9_hash}" = "none" || { f="%{SOURCE9}"; test -f "$f" || { echo "oreon: missing Source9 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source9_hash}" || { echo "oreon: Source9 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{srcname}
# convert DMTF schema for Pegasus
export PEGASUS_ROOT=%PEGASUS_RPM_ROOT
yes | mak/CreateDmtfSchema 238 %{SOURCE9} cim_schema_2.38.0
%patch -P1 -p1 -b .no-rpath
%patch -P2 -p1 -b .PIE
%patch -P3 -p1 -b .redhat-config
%patch -P4 -p1 -b .cmpi-provider-lib
%patch -P6 -p1 -b .pam-wbem
%patch -P12 -p1 -b .snmp-tests
%patch -P5 -p1 -b .local-or-remote-auth
%patch -P13 -p1 -b .sparc
%patch -P16 -p1 -b .getpagesize
%patch -P19 -p1 -b .dont-strip
%patch -P20 -p1 -b .sparc-locks
%patch -P22 -p1 -b .null_value
%patch -P24 -p1 -b .empty_arrays
%patch -P25 -p1 -b .cimmofl-allow-experimental
%patch -P26 -p1 -b .schema-version-and-includes
%patch -P29 -p1 -b .enable-subscriptions-for-nonprivileged-users
%patch -P33 -p1 -b .gcc5-build
%patch -P34 -p1 -b .build-fixes
%patch -P35 -p1 -b .ssl-include
%patch -P36 -p1 -b .snmpv3-trap
%patch -P37 -p1 -b .fix-setup-sdk
%patch -P38 -p1 -b .cimconfig-man-page-fixes
%patch -P39 -p1 -b .fix-setup-sdk-ppc64le
%patch -P40 -p1 -b .testid
%patch -P41 -p1 -b .ssl-cert-path
%patch -P42 -p1 -b .openssl-1.1-fix
%patch -P43 -p1 -b .Wreserved-user-defined-literal-fix
%patch -P44 -p1 -b .crypto-policy-compliance
%patch -P45 -p1 -b .add-pegwsmserver-to-ldd-libs
%patch -P46 -p1 -b .build-fixes-2
%patch -P47 -p1 -b .snmp-disable-des
%patch -P48 -p1 -b .add-riscv64-support
%patch -P49 -p1 -b .bin-sbin-unify
%patch -P50 -p1 -b .ssl-certs-gen-changes
%patch -P51 -p1 -b .post-quantum

%build

cp -fp %SOURCE1 doc
cp -fp %SOURCE3 doc
cp -fp %SOURCE6 rpm
cp -fp %SOURCE8 doc
export PEGASUS_ROOT=%PEGASUS_RPM_ROOT
export PEGASUS_HOME=%PEGASUS_RPM_HOME
export PEGASUS_PLATFORM=%PEGASUS_HARDWARE_PLATFORM
export PEGASUS_ARCH_LIB=%PEGASUS_ARCH_LIB
export PEGASUS_ENVVAR_FILE=$PEGASUS_ROOT/env_var_Linux.status
export OPENSSL_HOME=%OPENSSL_HOME
export OPENSSL_BIN=%OPENSSL_BIN
export LD_LIBRARY_PATH=$PEGASUS_HOME/lib
export PATH=$PEGASUS_HOME/bin:$PATH
export PEGASUS_EXTRA_C_FLAGS="$RPM_OPT_FLAGS -fPIC -g -Wall -Wno-unused -fno-strict-aliasing"
export PEGASUS_EXTRA_CXX_FLAGS="$PEGASUS_EXTRA_C_FLAGS -std=c++14"
export PEGASUS_EXTRA_LINK_FLAGS="$RPM_OPT_FLAGS -Wl,-z,now"
export PEGASUS_EXTRA_PROGRAM_LINK_FLAGS="-g -pie -Wl,-z,relro,-z,now,-z,nodlopen,-z,noexecstack"
export SYS_INCLUDES=-I/usr/kerberos/include
%make_build -f ${PEGASUS_ROOT}/Makefile.Release create_ProductVersionFile
%make_build -f ${PEGASUS_ROOT}/Makefile.Release create_CommonProductDirectoriesInclude
%make_build -f ${PEGASUS_ROOT}/Makefile.Release create_ConfigProductDirectoriesInclude
%make_build -f ${PEGASUS_ROOT}/Makefile.Release all
%make_build -f ${PEGASUS_ROOT}/Makefile.Release repository
%install
mkdir -p $RPM_BUILD_ROOT/etc/pki/Pegasus
export PEGASUS_ROOT=%PEGASUS_RPM_ROOT
export PEGASUS_HOME=%PEGASUS_RPM_HOME
export PEGASUS_PLATFORM=%PEGASUS_HARDWARE_PLATFORM
export PEGASUS_ARCH_LIB=%PEGASUS_ARCH_LIB
export PEGASUS_ENVVAR_FILE=$PEGASUS_ROOT/env_var_Linux.status
export OPENSSL_BIN=%OPENSSL_BIN
export LD_LIBRARY_PATH=$PEGASUS_HOME/lib
export PATH=$PEGASUS_HOME/bin:$PATH
export PEGASUS_STAGING_DIR=$RPM_BUILD_ROOT
%if %{PEGASUS_BUILD_TEST_RPM}
make -f $PEGASUS_ROOT/Makefile.Release stage \
    PEGASUS_STAGING_DIR=$PEGASUS_STAGING_DIR \
    PEGASUS_BUILD_TEST_RPM=%{PEGASUS_BUILD_TEST_RPM}
%else
make -f $PEGASUS_ROOT/Makefile.Release stage \
    PEGASUS_STAGING_DIR=$PEGASUS_STAGING_DIR
%endif
mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
install -p -D -m 644 %{SOURCE4} $RPM_BUILD_ROOT/%{_tmpfilesdir}/tog-pegasus.conf
mkdir -p $RPM_BUILD_ROOT/usr/share/Pegasus/scripts
install -p -m 755 %{SOURCE10} $RPM_BUILD_ROOT/usr/share/Pegasus/scripts/generate-certs
rm -f $RPM_BUILD_ROOT/etc/Pegasus/ssl.cnf
mkdir -p $RPM_BUILD_ROOT/etc/pki/Pegasus/crl
rm -f $RPM_BUILD_ROOT/etc/init.d/tog-pegasus
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_unitdir}/tog-pegasus.service
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
mv $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{major_ver}/* $RPM_BUILD_ROOT/%{_docdir}/%{name}
rm -rf $RPM_BUILD_ROOT/usr/share/doc/%{name}-%{major_ver}
pushd $RPM_BUILD_ROOT/usr/%{_lib}
ln -s libcmpiCppImpl.so.1 libcmpiCppImpl.so
ln -s libpeglistener.so.1 libpeglistener.so
popd
mkdir -p $RPM_BUILD_ROOT/%{_libexecdir}/pegasus
mv $RPM_BUILD_ROOT/%{_bindir}/cimprovagt $RPM_BUILD_ROOT/%{_libexecdir}/pegasus
install -p -m 0755 %{SOURCE7} $RPM_BUILD_ROOT/%{_bindir}/cimprovagt
install -m 644 src/Pegasus/Common/Platform_LINUX_XSCALE_GNU.h $RPM_BUILD_ROOT/%{_includedir}/Pegasus/Common
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/Pegasus/Listener
install -m 644 src/Pegasus/Listener/Linkage.h $RPM_BUILD_ROOT/%{_includedir}/Pegasus/Listener
install -m 644 src/Pegasus/Listener/CIMListener.h $RPM_BUILD_ROOT/%{_includedir}/Pegasus/Listener
install -m 644 src/Pegasus/Client/CIMEnumerationContext.h $RPM_BUILD_ROOT/%{_includedir}/Pegasus/Client
install -m 644 src/Pegasus/Common/UintArgs.h $RPM_BUILD_ROOT/%{_includedir}/Pegasus/Common
%if %{PEGASUS_BUILD_TEST_RPM}
install -p %{SOURCE11} $RPM_BUILD_ROOT/usr/share/Pegasus/test/snmptrapd.conf
%endif
install -p Schemas/CIM238/DMTF/Core/CIM_AbstractComponent.mof $RPM_BUILD_ROOT/usr/share/Pegasus/samples/Providers/Load/CIM238/DMTF/Core/
mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man1/
cp %SOURCE12 ${RPM_BUILD_ROOT}/%{_mandir}/man1/
install -p -D -m 0644 %{SOURCE13} %{buildroot}%{_sysusersdir}/tog-pegasus.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export LD_LIBRARY_PATH=$RPM_BUILD_ROOT/usr/%{_lib}
cd $RPM_BUILD_ROOT/usr/share/Pegasus/test
make prestarttests
rm $RPM_BUILD_ROOT/usr/share/Pegasus/test/log.trace.0
rm $RPM_BUILD_ROOT/usr/share/Pegasus/test/testtracer4.trace.0
%pre

if [ $1 -gt 1 ]; then
   if [ -d /var/lib/Pegasus/repository ]; then
        if [ -d /var/lib/Pegasus/prev_repository ]; then
           rm -rf /var/lib/Pegasus/prev_repository
        fi;
        cp -r /var/lib/Pegasus/repository /var/lib/Pegasus/prev_repository;
   fi
fi
:;
%post

install -d -m 1750 -o root -g pegasus /var/run/tog-pegasus
restorecon /var/run/tog-pegasus
/usr/bin/ldconfig;
%systemd_post tog-pegasus.service
if [ $1 -ge 1 ]; then
   echo `date` >>  /var/lib/Pegasus/log/install.log 2>&1 || :;
   if [ $1 -gt 1 ]; then
      if [ -d /var/lib/Pegasus/prev_repository ]; then
         /usr/bin/repupgrade 2>> /var/lib/Pegasus/log/install.log || :;
      fi;
      /bin/systemctl try-restart tog-pegasus.service >/dev/null 2>&1 || :;
   fi;
   (mkdir -p /usr/share/factory/var/lib && cp -a /var/lib/Pegasus /usr/share/factory/var/lib/Pegasus) >/dev/null 2>&1 || :;
fi
:;
%preun

%systemd_preun tog-pegasus.service
if [ $1 -eq 0 ]; then                  
   rm -rf /var/run/tog-pegasus
   rm -rf /usr/share/factory/var/lib/Pegasus
fi
:;
%postun

/usr/bin/ldconfig
%systemd_postun_with_restart tog-pegasus.service
%preun devel

if [ $1 -eq 0 ] ; then
   make --directory /usr/share/Pegasus/samples -s clean >/dev/null 2>&1 || :;
fi
:;
%post libs

if [ $1 -eq 1 ]; then
   ln -sf libpegclient.so.1 /usr/%PEGASUS_ARCH_LIB/libpegclient.so
   ln -sf libpegcommon.so.1 /usr/%PEGASUS_ARCH_LIB/libpegcommon.so
   ln -sf libpegprovider.so.1 /usr/%PEGASUS_ARCH_LIB/libpegprovider.so
   ln -sf libDefaultProviderManager.so.1 /usr/%PEGASUS_ARCH_LIB/libDefaultProviderManager.so
   ln -sf libCIMxmlIndicationHandler.so.1 /usr/%PEGASUS_ARCH_LIB/libCIMxmlIndicationHandler.so
   ln -sf libsnmpIndicationHandler.so.1 /usr/%PEGASUS_ARCH_LIB/libsnmpIndicationHandler.so
   ln -sf libComputerSystemProvider.so.1 /usr/%PEGASUS_ARCH_LIB/Pegasus/providers/libComputerSystemProvider.so
   ln -sf libOSProvider.so.1 /usr/%PEGASUS_ARCH_LIB/Pegasus/providers/libOSProvider.so
   ln -sf libProcessProvider.so.1 /usr/%PEGASUS_ARCH_LIB/Pegasus/providers/libProcessProvider.so
   ln -sf libCMPIProviderManager.so.1 /usr/%PEGASUS_ARCH_LIB/Pegasus/providerManagers/libCMPIProviderManager.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libpegclient.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libpegcommon.so 
   /bin/chgrp -h pegasus /usr/%{_lib}/libpegprovider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libDefaultProviderManager.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libCIMxmlIndicationHandler.so
   /bin/chgrp -h pegasus /usr/%{_lib}/libsnmpIndicationHandler.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providers/libComputerSystemProvider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providers/libOSProvider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providers/libProcessProvider.so
   /bin/chgrp -h pegasus /usr/%{_lib}/Pegasus/providerManagers/libCMPIProviderManager.so
fi
:;
/usr/bin/ldconfig
%postun libs

/usr/bin/ldconfig
%files -f %{oreon_filedir}/main.list
%files -n tog-pegasus-devel -f %{oreon_filedir}/tog-pegasus-devel.list
%files -n tog-pegasus-libs -f %{oreon_filedir}/tog-pegasus-libs.list
%files -n tog-pegasus-test -f %{oreon_filedir}/tog-pegasus-test.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2:2.14.1-89
- Import

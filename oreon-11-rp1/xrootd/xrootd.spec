%global source0_hash 39946509a50e790ab3fcc77ba0f4c9b66abef221262756aa8bb2494f00a0e321

%if %{?fedora}%{!?fedora:0}
%ifarch %{ix86} %{arm}
%global ceph 0
%else
%global ceph 1
%endif
%else
%global ceph 0
%endif

# Needed for EPEL 8
%undefine __cmake_in_source_build

Name:		xrootd
Epoch:		1
Version:	5.9.1
Release:	2%{?dist}
Summary:	Extended ROOT file server
License:	LGPL-3.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND curl AND MIT AND Zlib
URL:		https://xrootd.web.cern.ch
Source0:	%{url}/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-sysusers.conf
#		https://github.com/xrootd/xrootd/pull/2649
Patch0:		0001-Tests-Avoid-test-segfault-on-32-bit-architectures.patch
#		Backport from upstream git
Patch1:		0001-Tests-Ensure-extra-test-fixtures-are-ready-before-se.patch

BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	make
BuildRequires:	pkgconfig
BuildRequires:	fuse-devel
BuildRequires:	krb5-devel
BuildRequires:	libcurl-devel
BuildRequires:	tinyxml-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	perl-generators
BuildRequires:	readline-devel
BuildRequires:	zlib-devel
BuildRequires:	doxygen
BuildRequires:	graphviz
BuildRequires:	selinux-policy-devel
BuildRequires:	systemd-rpm-macros
BuildRequires:	systemd-devel
BuildRequires:	python3-devel
BuildRequires:	python3-pip
BuildRequires:	python3-setuptools
BuildRequires:	python3-wheel
BuildRequires:	python3-sphinx
BuildRequires:	json-c-devel
BuildRequires:	libmacaroons-devel
BuildRequires:	libuuid-devel
BuildRequires:	voms-devel
BuildRequires:	scitokens-cpp-devel
BuildRequires:	davix-devel
BuildRequires:	libxcrypt-devel
%if %{ceph}
BuildRequires:	librados-devel
BuildRequires:	libradosstriper-devel
%endif
%ifnarch %{ix86}
BuildRequires:	isa-l-devel
%endif
BuildRequires:	attr
BuildRequires:	curl
BuildRequires:	davix
BuildRequires:	gtest-devel
BuildRequires:	openssl
BuildRequires:	procps

Requires:	%{name}-server%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-selinux = %{epoch}:%{version}-%{release}

%description
The Extended root file server consists of a file server called xrootd
and a cluster management server called cmsd.

The xrootd server was developed for the root analysis framework to
serve root files. However, the server is agnostic to file types and
provides POSIX-like access to any type of file.

The cmsd server is the next generation version of the olbd server,
originally developed to cluster and load balance Objectivity/DB AMS
database servers. It provides enhanced capability along with lower
latency and increased throughput.

%package server
Summary:	Xrootd server daemons
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-server-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	expect
Requires:	logrotate
%{?sysusers_requires_compat}
%{?systemd_requires}

%description server
This package contains the xrootd servers without the SELinux support.
Unless you are installing on a system without SELinux also install the
xrootd-selinux package.

%package selinux
Summary:	SELinux policy module for the xrootd server
BuildArch:	noarch
Requires:	selinux-policy
Requires(post):		policycoreutils
Requires(postun):	policycoreutils

%description selinux
This package contains SELinux policy module for the xrootd server package.

%package libs
Summary:	Libraries used by xrootd servers and clients

%description libs
This package contains libraries used by the xrootd servers and clients.

%package devel
Summary:	Development files for xrootd
Provides:	%{name}-libs-devel = %{epoch}:%{version}-%{release}
Provides:	%{name}-libs-devel%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-libs-devel < %{epoch}:%{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package contains header files and development libraries for xrootd
development.

%package client-libs
Summary:	Libraries used by xrootd clients
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description client-libs
This package contains libraries used by xrootd clients.

%package client-devel
Summary:	Development files for xrootd clients
Provides:	%{name}-cl-devel = %{epoch}:%{version}-%{release}
Provides:	%{name}-cl-devel%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-cl-devel < %{epoch}:%{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description client-devel
This package contains header files and development libraries for xrootd
client development.

%package server-libs
Summary:	Libraries used by xrootd servers
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description server-libs
This package contains libraries used by xrootd servers.

%package server-devel
Summary:	Development files for xrootd servers
Requires:	%{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-server-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description server-devel
This package contains header files and development libraries for xrootd
server development.

%package private-devel
Summary:	Private xrootd headers
Requires:	%{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-server-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description private-devel
This package contains some private xrootd headers. Backward and forward
compatibility between versions is not guaranteed for these headers.

%package client
Summary:	Xrootd command line client tools
Provides:	%{name}-cl = %{epoch}:%{version}-%{release}
Provides:	%{name}-cl%{?_isa} = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-cl < %{epoch}:%{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description client
This package contains the command line tools used to communicate with
xrootd servers.

%package fuse
Summary:	Xrootd FUSE tool
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	fuse

%description fuse
This package contains the FUSE (file system in user space) xrootd mount
tool.

%package voms
Summary:	VOMS attribute extractor plugin for XRootD
Provides:	vomsxrd = %{epoch}:%{version}-%{release}
Provides:	%{name}-voms-plugin = %{epoch}:%{version}-%{release}
Provides:	xrdhttpvoms = %{epoch}:%{version}-%{release}
Obsoletes:	vomsxrd < 1:0.6.0-4
Obsoletes:	%{name}-voms-plugin < 1:0.6.0-3
Obsoletes:	xrdhttpvoms < 0.2.5-9
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description voms
The VOMS attribute extractor plugin for XRootD.

%package scitokens
Summary:	SciTokens authorization support for XRootD
License:	Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause
Requires:	%{name}-server%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description scitokens
This ACC (authorization) plugin for the XRootD framework utilizes the
SciTokens library to validate and extract authorization claims from a
SciToken passed during a transfer. Configured appropriately, this
allows the XRootD server admin to delegate authorization decisions for
a subset of the namespace to an external issuer.

%package -n xrdcl-http
Summary:	HTTP client plugin for XRootD
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description -n xrdcl-http
xrdcl-http is an XRootD client plugin which allows XRootD to interact
with HTTP repositories.

%if %{ceph}
%package ceph
Summary:	XRootD plugin for interfacing with the Ceph storage platform
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description ceph
The xrootd-ceph is an OSS layer plugin for the XRootD server for
interfacing with the Ceph storage platform.
%endif

%package -n python3-%{name}
Summary:	Python 3 bindings for xrootd
%py_provides	python3-%{name}
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-client-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description -n python3-%{name}
This package contains Python 3 bindings for xrootd.

%package doc
Summary:	Developer documentation for the xrootd libraries
BuildArch:	noarch

%description doc
This package contains the API documentation of the xrootd libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DFORCE_ENABLED:BOOL=ON \
    -DENABLE_TESTS:BOOL=ON \
%if %{ceph}
    -DENABLE_CEPH:BOOL=ON \
%endif
%ifarch %{ix86}
    -DENABLE_XRDEC:BOOL=OFF \
%endif
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 9
    -DPIP_OPTIONS="--no-deps --use-pep517 --no-build-isolation --disable-pip-version-check --verbose" \
%else
    -DPIP_OPTIONS="--no-deps --disable-pip-version-check --verbose" \
%endif
    -DXRD_PYTHON_REQ_VERSION=%{python3_version}
%cmake_build

make -C packaging/common -f /usr/share/selinux/devel/Makefile

doxygen Doxyfile
# Use local image instead of remote
sed 's!src=".*/xrootd-logo.png"!src="xrootd-logo.png"!' \
    -i doxydoc/html/index.html
cp -p docs/images/xrootd-logo.png doxydoc/html

%install
%cmake_install

rm -f %{buildroot}%{_libdir}/libXrdCephPosix.so

rm -f %{buildroot}%{_bindir}/xrdshmap

rm -f %{buildroot}%{python3_sitearch}/xrootd-*.*-info/direct_url.json
rm -f %{buildroot}%{python3_sitearch}/xrootd-*.*-info/RECORD
[ -r %{buildroot}%{python3_sitearch}/xrootd-*.*-info/INSTALLER ] && \
    sed s/pip/rpm/ \
    -i %{buildroot}%{python3_sitearch}/xrootd-*.*-info/INSTALLER

rm -f %{buildroot}%{_libdir}/cmake/XRootD/uninstall.cmake

LD_LIBRARY_PATH=%{buildroot}%{_libdir} \
PYTHONPATH=%{buildroot}%{python3_sitearch} \
PYTHONDONTWRITEBYTECODE=1 \
make -C bindings/python/docs html

# Service unit files
mkdir -p %{buildroot}%{_unitdir}
install -m 644 -p packaging/common/xrootd@.service %{buildroot}%{_unitdir}
install -m 644 -p packaging/common/xrootd@.socket %{buildroot}%{_unitdir}
install -m 644 -p packaging/common/xrdhttp@.socket %{buildroot}%{_unitdir}
install -m 644 -p packaging/common/cmsd@.service %{buildroot}%{_unitdir}
install -m 644 -p packaging/common/frm_xfrd@.service %{buildroot}%{_unitdir}
install -m 644 -p packaging/common/frm_purged@.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 -p packaging/rhel/xrootd.tmpfiles %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 -p %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

# Server config
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
install -m 644 -p packaging/common/%{name}-clustered.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-clustered.cfg
install -m 644 -p packaging/common/%{name}-standalone.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-standalone.cfg
install -m 644 -p packaging/common/%{name}-filecache-clustered.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-filecache-clustered.cfg
install -m 644 -p packaging/common/%{name}-filecache-standalone.cfg \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-filecache-standalone.cfg
sed 's!/usr/lib64/!!' packaging/common/%{name}-http.cfg > \
    %{buildroot}%{_sysconfdir}/%{name}/%{name}-http.cfg

# Client config
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/client.plugins.d
install -m 644 -p packaging/common/client.conf \
    %{buildroot}%{_sysconfdir}/%{name}/client.conf
sed 's!/usr/lib/!!' packaging/common/client-plugin.conf.example > \
    %{buildroot}%{_sysconfdir}/%{name}/client.plugins.d/client-plugin.conf.example
sed -e 's!/usr/lib64/!!' -e 's!-5!!' packaging/common/recorder.conf > \
    %{buildroot}%{_sysconfdir}/%{name}/client.plugins.d/recorder.conf
sed 's!/usr/lib64/!!' packaging/common/http.client.conf.example > \
    %{buildroot}%{_sysconfdir}/%{name}/client.plugins.d/xrdcl-http-plugin.conf

chmod 644 %{buildroot}%{_datadir}/%{name}/utils/XrdCmsNotify.pm

sed 's!/usr/bin/env perl!/usr/bin/perl!' -i \
    %{buildroot}%{_datadir}/%{name}/utils/netchk \
    %{buildroot}%{_datadir}/%{name}/utils/XrdCmsNotify.pm \
    %{buildroot}%{_datadir}/%{name}/utils/XrdOlbMonPerf

sed 's!/usr/bin/env bash!/bin/bash!' -i %{buildroot}%{_bindir}/xrootd-config

mkdir -p %{buildroot}%{_sysconfdir}/%{name}/config.d

mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_localstatedir}/spool/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -m 644 -p packaging/common/%{name}.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

mkdir -p %{buildroot}%{_datadir}/selinux/packages/%{name}
install -m 644 -p packaging/common/%{name}.pp \
    %{buildroot}%{_datadir}/selinux/packages/%{name}

# Documentation
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr doxydoc/html %{buildroot}%{_pkgdocdir}

cp -pr bindings/python/docs/build/html %{buildroot}%{_pkgdocdir}/python
rm %{buildroot}%{_pkgdocdir}/python/.buildinfo

%check
export HOSTNAME=localhost

# Reduce socket path lengths used during tests
# rpm 4.20 uses a longer path to the build directory than earlier versions
# Tests fail with sockets in the build directory with rpm 4.20
adminpath=$(mktemp -d -p /var/tmp)
trap "rm -rf ${adminpath}" EXIT

sed "s!all.adminpath .*!all.adminpath ${adminpath}/XRootD!" \
    -i tests/XRootD/common.cfg

for x in authenticated_cluster badredir cluster TPCTests xcachewithcsi ; do
    sed "s!all.adminpath .*!all.adminpath ${adminpath}/${x}!" \
	-i %{_vpath_builddir}/tests/${x}/common.cfg
done

# The badredir test fails when there is no network - exclude

touch testfile
if ( setfattr -n user.testattr -v testvalue testfile ) ; then
    %ctest -- -E XRootD::badredir
else
    echo "Extended file attributes not supported by file system"
    echo "Don't run tests that require them"
    exclude="\
XrdCl::FileCopyTest|\
XrdCl::FileSystemTest.PlugInTest|\
XrdCl::FileSystemTest.ServerQueryTest|\
XrdCl::FileSystemTest.XAttrTest|\
XrdCl::FileTest.XAttrTest|\
XrdCl::LocalFileHandlerTest.XAttrTest|\
XrdCl::ThreadingTest|\
XrdCl::WorkflowTest.CheckpointTest|\
XrdCl::WorkflowTest.XAttrWorkflowTest|\
XrdEc::XrdEcTests|\
XRootD::authenticated_cluster::test|\
XRootD::badredir|\
XRootD::cluster::test|\
XRootD::http::test|\
XRootD::posix::test|\
XRootD::tpc::test"
    %ctest -- -E $exclude
fi
rm testfile

%pre server
%sysusers_create_compat %{SOURCE1}

%post server
%tmpfiles_create %{name}.conf

if [ $1 -eq 1 ] ; then
    systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun server
if [ $1 -eq 0 ] ; then
    for DAEMON in xrootd cmsd frm_purged frm_xfrd; do
	for INSTANCE in `systemctl | grep $DAEMON@ | awk '{print $1;}'`; do
	    systemctl --no-reload disable $INSTANCE > /dev/null 2>&1 || :
	    systemctl stop $INSTANCE > /dev/null 2>&1 || :
	done
    done
fi

%postun server
if [ $1 -ge 1 ] ; then
    systemctl daemon-reload >/dev/null 2>&1 || :
    for DAEMON in xrootd cmsd frm_purged frm_xfrd; do
	for INSTANCE in `systemctl | grep $DAEMON@ | awk '{print $1;}'`; do
	    systemctl try-restart $INSTANCE >/dev/null 2>&1 || :
	done
    done
fi

%post selinux
/usr/sbin/semodule -i %{_datadir}/selinux/packages/%{name}/%{name}.pp >/dev/null 2>&1 || :

%postun selinux
if [ $1 -eq 0 ] ; then
    /usr/sbin/semodule -r %{name} >/dev/null 2>&1 || :
fi

%files
# Empty

%files server
%{_bindir}/cconfig
%{_bindir}/cmsd
%{_bindir}/frm_admin
%{_bindir}/frm_purged
%{_bindir}/frm_xfragent
%{_bindir}/frm_xfrd
%{_bindir}/mpxstats
%{_bindir}/wait41
%{_bindir}/xrdacctest
%{_bindir}/xrdpfc_print
%{_bindir}/xrdpwdadmin
%{_bindir}/xrdsssadmin
%{_bindir}/xrootd
%{_mandir}/man8/cmsd.8*
%{_mandir}/man8/frm_admin.8*
%{_mandir}/man8/frm_purged.8*
%{_mandir}/man8/frm_xfragent.8*
%{_mandir}/man8/frm_xfrd.8*
%{_mandir}/man8/mpxstats.8*
%{_mandir}/man8/xrdpfc_print.8*
%{_mandir}/man8/xrdpwdadmin.8*
%{_mandir}/man8/xrdsssadmin.8*
%{_mandir}/man8/xrootd.8*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/utils
%{_unitdir}/*
%{_tmpfilesdir}/%{name}.conf
%{_sysusersdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/%{name}/config.d
%attr(-,xrootd,xrootd) %config(noreplace) %{_sysconfdir}/%{name}/*.cfg
%attr(-,xrootd,xrootd) %{_localstatedir}/log/%{name}
%attr(-,xrootd,xrootd) %{_localstatedir}/spool/%{name}
%ghost %attr(-,xrootd,xrootd) %{_rundir}/%{name}

%files selinux
%dir %{_datadir}/selinux/packages/%{name}
%{_datadir}/selinux/packages/%{name}/%{name}.pp

%files libs
%{_libdir}/libXrdAppUtils.so.*
%{_libdir}/libXrdCrypto.so.*
%{_libdir}/libXrdCryptoLite.so.*
%{_libdir}/libXrdUtils.so.*
%{_libdir}/libXrdXml.so.*
# Plugins
%{_libdir}/libXrdCksCalczcrc32-5.so
%{_libdir}/libXrdCryptossl-5.so
%{_libdir}/libXrdSec-5.so
%{_libdir}/libXrdSecProt-5.so
%{_libdir}/libXrdSecgsi-5.so
%{_libdir}/libXrdSecgsiAUTHZVO-5.so
%{_libdir}/libXrdSecgsiGMAPDN-5.so
%{_libdir}/libXrdSeckrb5-5.so
%{_libdir}/libXrdSecpwd-5.so
%{_libdir}/libXrdSecsss-5.so
%{_libdir}/libXrdSecunix-5.so
%{_libdir}/libXrdSecztn-5.so
%license COPYING* LICENSE

%files devel
%{_bindir}/xrootd-config
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/XProtocol
%{_includedir}/%{name}/Xrd
%{_includedir}/%{name}/XrdCks
%{_includedir}/%{name}/XrdNet
%{_includedir}/%{name}/XrdOuc
%{_includedir}/%{name}/XrdSec
%{_includedir}/%{name}/XrdSys
%{_includedir}/%{name}/XrdXml
%{_includedir}/%{name}/XrdVersion.hh
%{_libdir}/libXrdAppUtils.so
%{_libdir}/libXrdCrypto.so
%{_libdir}/libXrdCryptoLite.so
%{_libdir}/libXrdUtils.so
%{_libdir}/libXrdXml.so
%{_libdir}/cmake/XRootD

%files client-libs
%{_libdir}/libXrdCl.so.*
%ifnarch %{ix86}
%{_libdir}/libXrdEc.so.*
%endif
%{_libdir}/libXrdFfs.so.*
%{_libdir}/libXrdPosix.so.*
%{_libdir}/libXrdPosixPreload.so.*
# This lib may be used for LD_PRELOAD so the .so link needs to be included
%{_libdir}/libXrdPosixPreload.so
%{_libdir}/libXrdSsiLib.so.*
%{_libdir}/libXrdSsiShMap.so.*
# Plugins
%{_libdir}/libXrdClProxyPlugin-5.so
%{_libdir}/libXrdClRecorder-5.so
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/client.conf
%dir %{_sysconfdir}/%{name}/client.plugins.d
%config(noreplace) %{_sysconfdir}/%{name}/client.plugins.d/client-plugin.conf.example
%config(noreplace) %{_sysconfdir}/%{name}/client.plugins.d/recorder.conf

%files client-devel
%{_includedir}/%{name}/XrdCl
%{_includedir}/%{name}/XrdPosix
%{_libdir}/libXrdCl.so
%{_libdir}/libXrdFfs.so
%{_libdir}/libXrdPosix.so

%files server-libs
%{_libdir}/libXrdHttpUtils.so.*
%{_libdir}/libXrdServer.so.*
# Plugins
%{_libdir}/libXrdBlacklistDecision-5.so
%{_libdir}/libXrdBwm-5.so
%{_libdir}/libXrdCmsRedirectLocal-5.so
%{_libdir}/libXrdFileCache-5.so
%{_libdir}/libXrdHttp-5.so
%{_libdir}/libXrdHttpCors-5.so
%{_libdir}/libXrdHttpTPC-5.so
%{_libdir}/libXrdMacaroons-5.so
%{_libdir}/libXrdN2No2p-5.so
%{_libdir}/libXrdOfsPrepGPI-5.so
%{_libdir}/libXrdOssCsi-5.so
%{_libdir}/libXrdOssSIgpfsT-5.so
%{_libdir}/libXrdOssStats-5.so
%{_libdir}/libXrdPfc-5.so
%{_libdir}/libXrdPfcPurgeQuota-5.so
%{_libdir}/libXrdPss-5.so
%{_libdir}/libXrdSsi-5.so
%{_libdir}/libXrdSsiLog-5.so
%{_libdir}/libXrdThrottle-5.so
%{_libdir}/libXrdXrootd-5.so

%files server-devel
%{_includedir}/%{name}/XrdAcc
%{_includedir}/%{name}/XrdCms
%{_includedir}/%{name}/XrdHttp
%{_includedir}/%{name}/XrdOfs
%{_includedir}/%{name}/XrdOss
%{_includedir}/%{name}/XrdPfc
%{_includedir}/%{name}/XrdSfs
%{_includedir}/%{name}/XrdXrootd
%{_libdir}/libXrdHttpUtils.so
%{_libdir}/libXrdServer.so

%files private-devel
%{_includedir}/%{name}/private
%ifnarch %{ix86}
%{_libdir}/libXrdEc.so
%endif
%{_libdir}/libXrdSsiLib.so
%{_libdir}/libXrdSsiShMap.so

%files client
%{_bindir}/xrdadler32
%{_bindir}/xrdcks
%{_bindir}/xrdcopy
%{_bindir}/xrdcp
%{_bindir}/xrdcrc32c
%{_bindir}/xrdfs
%{_bindir}/xrdgsiproxy
%{_bindir}/xrdgsitest
%{_bindir}/xrdmapc
%{_bindir}/xrdpinls
%{_bindir}/xrdreplay
%{_mandir}/man1/xrdadler32.1*
%{_mandir}/man1/xrdcopy.1*
%{_mandir}/man1/xrdcp.1*
%{_mandir}/man1/xrdfs.1*
%{_mandir}/man1/xrdgsiproxy.1*
%{_mandir}/man1/xrdgsitest.1*
%{_mandir}/man1/xrdmapc.1*

%files fuse
%{_bindir}/xrootdfs
%{_mandir}/man1/xrootdfs.1*

%files voms
%{_libdir}/libXrdVoms-5.so
%{_libdir}/libXrdHttpVOMS-5.so
%{_libdir}/libXrdSecgsiVOMS-5.so
%doc %{_mandir}/man1/libXrdVoms.1*
%doc %{_mandir}/man1/libXrdSecgsiVOMS.1*
%doc src/XrdVoms/README.md

%files scitokens
%{_libdir}/libXrdAccSciTokens-5.so
%doc src/XrdSciTokens/README.md

%files -n xrdcl-http
%{_libdir}/libXrdClHttp-5.so
%config(noreplace) %{_sysconfdir}/%{name}/client.plugins.d/xrdcl-http-plugin.conf

%if %{ceph}
%files ceph
%{_libdir}/libXrdCeph-5.so
%{_libdir}/libXrdCephXattr-5.so
%{_libdir}/libXrdCephPosix.so.*
%endif

%files -n python3-%{name}
%{python3_sitearch}/xrootd-*.*-info
%{python3_sitearch}/pyxrootd
%{python3_sitearch}/XRootD

%files doc
%doc %{_pkgdocdir}

%changelog
%autochangelog

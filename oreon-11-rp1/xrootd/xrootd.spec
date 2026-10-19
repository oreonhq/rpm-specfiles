%global source0_hash 2853c9fcf476c924f3605b1b1629562badcce631ad156c700735e681a7aa4f04
%global ceph 0
%undefine __cmake_in_source_build
Name:		xrootd
Epoch:		1
Version:	6.1.1
Release:        1%{?dist}
Summary:        Extended ROOT file server
License:	LGPL-3.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND curl AND MIT AND Zlib
URL:		https://xrootd.web.cern.ch
Source0:        https://%{name}.web.cern.ch/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}-sysusers.conf
Patch0:		0001-Tests-Avoid-test-segfault-on-32-bit-architectures.patch
Patch1:		0001-Tests-Ensure-extra-test-fixtures-are-ready-before-se.patch
%ifnarch %{ix86}
%endif
Requires:	%{name}-server%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}-selinux = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  attr
BuildRequires:  cmake
BuildRequires:  curl
BuildRequires:  davix
BuildRequires:  davix-devel
BuildRequires:  doxygen
BuildRequires:  fuse-devel
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  gtest-devel
BuildRequires:  isa-l-devel
BuildRequires:  json-c-devel
BuildRequires:  krb5-devel
BuildRequires:  libcurl-devel
BuildRequires:  libmacaroons-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-wheel
BuildRequires:  readline-devel
BuildRequires:  scitokens-cpp-devel
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tinyxml-devel
BuildRequires:  voms-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
%ifarch %{ix86}
    -DENABLE_XRDEC:BOOL=OFF \
%endif
    -DPIP_OPTIONS="--no-deps --disable-pip-version-check --verbose" \
    -DXRD_PYTHON_REQ_VERSION=%{python3_version}
%cmake_build
make -C packaging/common -f /usr/share/selinux/devel/Makefile
doxygen Doxyfile
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
mkdir -p %{buildroot}%{_pkgdocdir}
cp -pr doxydoc/html %{buildroot}%{_pkgdocdir}
cp -pr bindings/python/docs/build/html %{buildroot}%{_pkgdocdir}/python
rm %{buildroot}%{_pkgdocdir}/python/.buildinfo
%oreon_autofiles xrdcl-http usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export HOSTNAME=localhost
adminpath=$(mktemp -d -p /var/tmp)
trap "rm -rf ${adminpath}" EXIT
sed "s!all.adminpath .*!all.adminpath ${adminpath}/XRootD!" \
    -i tests/XRootD/common.cfg
for x in authenticated_cluster badredir cluster TPCTests xcachewithcsi ; do
    sed "s!all.adminpath .*!all.adminpath ${adminpath}/${x}!" \
	-i %{_vpath_builddir}/tests/${x}/common.cfg
done
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
%files -f %{oreon_filedir}/main.list
%files -n xrootd-server -f %{oreon_filedir}/xrootd-server.list
%files -n xrootd-selinux -f %{oreon_filedir}/xrootd-selinux.list
%files -n xrootd-libs -f %{oreon_filedir}/xrootd-libs.list
%files -n xrootd-devel -f %{oreon_filedir}/xrootd-devel.list
%files -n xrootd-client-libs -f %{oreon_filedir}/xrootd-client-libs.list
%files -n xrootd-client-devel -f %{oreon_filedir}/xrootd-client-devel.list
%files -n xrootd-server-libs -f %{oreon_filedir}/xrootd-server-libs.list
%files -n xrootd-server-devel -f %{oreon_filedir}/xrootd-server-devel.list
%files -n xrootd-private-devel -f %{oreon_filedir}/xrootd-private-devel.list
%files -n xrootd-client -f %{oreon_filedir}/xrootd-client.list
%files -n xrootd-fuse -f %{oreon_filedir}/xrootd-fuse.list
%files -n xrootd-voms -f %{oreon_filedir}/xrootd-voms.list
%files -n xrootd-scitokens -f %{oreon_filedir}/xrootd-scitokens.list
%files -n xrdcl-http -f %{oreon_filedir}/xrdcl-http.list
%files -n python3-xrootd -f %{oreon_filedir}/python3-xrootd.list
%files -n xrootd-doc -f %{oreon_filedir}/xrootd-doc.list

%changelog

%autochangelog

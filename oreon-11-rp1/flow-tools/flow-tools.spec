%global source0_hash 80bbd3791b59198f0d20184761d96ba500386b0a71ea613c214a50aa017a1f67
%bcond_without  openssl
%global username flow-tools
%global homedir %{_localstatedir}/%{name}
%global gecos "Network flow monitoring"
Version: 0.68.5.1
Name: flow-tools
Summary:        Tool set for working with NetFlow data
Release:        1%{?dist}
License: LicenseRef-Callaway-BSD 
URL: http://code.google.com/p/%{name}/
Source0:        http://%{name}.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1: flow-capture.service
Source2: flow-capture.sysconfig
Patch0:  flow-werror-fix.patch
Patch1:  flow-tools-extern.patch
Patch2: flow-tools-c99.patch
%if 0%{with openssl}
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libpq-devel
BuildRequires:  make
BuildRequires:  mariadb-connector-c-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
Flow-tools is library and a collection of programs used to collect, 
send, process, and generate reports from NetFlow data. The tools can be 
used together on a single server or distributed to multiple servers for 
large deployments. The flow-toools library provides an API for development 
of custom applications for NetFlow export versions 1,5,6 and the 14 currently 
defined version 8 subversions. A Perl and Python interface have been 
contributed and are included in the distribution.

%package devel
Summary: Development files for flow-tools
Requires: %{name} = %{version}-%{release}
Requires: zlib-devel
%description devel
Flow-tools is library and a collection of programs used to collect,
send, process, and generate reports from NetFlow data. The tools can be
used together on a single server or distributed to multiple servers for
large deployments. The flow-toools library provides an API for development
of custom applications for NetFlow export versions 1,5,6 and the 14 currently
defined version 8 subversions. A Perl and Python interface have been
contributed and are included in the distribution.

This package contains header files required to build applications that use
libft.

%package rrdtool
Summary: Scripts for flow-tools to build rrd graphs
Requires: %{name} = %{version}-%{release}
Requires: python2-rrdtool
%description rrdtool
Flow-tools is library and a collection of programs used to collect,
send, process, and generate reports from NetFlow data. The tools can be
used together on a single server or distributed to multiple servers for
large deployments. The flow-toools library provides an API for development
of custom applications for NetFlow export versions 1,5,6 and the 14 currently
defined version 8 subversions. A Perl and Python interface have been
contributed and are included in the distribution.

This package contains scripts that use python-rrdtool to create rrds and graphs
from flow data.

%package docs
Summary: HTML and other redundant docs for flow-tools
Requires: %{name} = %{version}-%{release}
%description docs
Flow-tools is library and a collection of programs used to collect,
send, process, and generate reports from NetFlow data. The tools can be
used together on a single server or distributed to multiple servers for
large deployments. The flow-toools library provides an API for development
of custom applications for NetFlow export versions 1,5,6 and the 14 currently
defined version 8 subversions. A Perl and Python interface have been
contributed and are included in the distribution.

This package contains additional documentation, such as man pages in html format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Remove /bin/env deps
sed -i '1s|^#!.*python|#!/usr/bin/python2|' bin/flow*
sed -i '1s|^#!.*perl|#!/usr/bin/perl|' utils/*
# Fix mariadb-connector-c detection
sed -i s/my_init/mysql_init/g configure

# Create a sysusers.d config file
cat >flow-tools.sysusers.conf <<EOF
u flow-tools - '%{gecos}' %{homedir} -
EOF

%build

export CFLAGS="$CFLAGS -std=gnu17"
%configure \
  --localstatedir=%{_localstatedir}/%{name} \
  --sysconfdir=%{_sysconfdir}/%{name} \
  --enable-static=no \
  --with-mysql \
  --with-postgresql \
%if 0%{with openssl}
  --with-openssl
%endif
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/%{name}
install -d $RPM_BUILD_ROOT%{_unitdir}
install -m 0644 %SOURCE1 $RPM_BUILD_ROOT%{_unitdir}/flow-capture.service
install -d $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -m 0644 %SOURCE2 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/flow-capture
install -m0644 -D flow-tools.sysusers.conf %{buildroot}%{_sysusersdir}/flow-tools.conf
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

/sbin/ldconfig
%systemd_post flow-capture.service
%preun

%systemd_preun flow-capture.service
%postun

%systemd_postun flow-capture.service
%files -f %{oreon_filedir}/main.list
%files -n flow-tools-devel -f %{oreon_filedir}/flow-tools-devel.list
%files -n flow-tools-rrdtool -f %{oreon_filedir}/flow-tools-rrdtool.list
%files -n flow-tools-docs -f %{oreon_filedir}/flow-tools-docs.list

%changelog

%autochangelog

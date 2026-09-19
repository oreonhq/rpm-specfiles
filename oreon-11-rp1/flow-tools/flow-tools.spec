%global source0_hash 80bbd3791b59198f0d20184761d96ba500386b0a71ea613c214a50aa017a1f67

# Does not support openssl 1.1
%if 0%{?fedora}
%bcond_with  openssl
%else
%bcond_without  openssl
%endif

%global username flow-tools
%global homedir %{_localstatedir}/%{name}
%global gecos "Network flow monitoring"

Version: 0.68.5.1
Name: flow-tools
Summary: Tool set for working with NetFlow data
Release: 46%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD 
URL: http://code.google.com/p/%{name}/
Source0: http://%{name}.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1: flow-capture.service
Source2: flow-capture.sysconfig
Patch0:  flow-werror-fix.patch
# Fix extern usage
Patch1:  flow-tools-extern.patch
Patch2: flow-tools-c99.patch

BuildRequires: gcc
%if 0%{with openssl}
BuildRequires: openssl-devel
%endif
BuildRequires: mariadb-connector-c-devel
BuildRequires: libpq-devel
BuildRequires: zlib-devel 
BuildRequires: bison
BuildRequires: flex
BuildRequires: doxygen
%if 0%{?fedora} >= 31
BuildRequires: python3.12
%endif
BuildRequires: systemd-rpm-macros
BuildRequires: make

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
%if 0%{?fedora} >= 31
Requires: python3-rrdtool
%else
Requires: python2-rrdtool
%endif

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
%if 0%{?fedora} >= 31
sed -i '1s|^#!.*python|#!/usr/bin/python3|' bin/flow*
python3.12 -m lib2to3 --write --nobackups bin/flow*
%else
sed -i '1s|^#!.*python|#!/usr/bin/python2|' bin/flow*
%endif
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

%post
/sbin/ldconfig
%systemd_post flow-capture.service

%preun
%systemd_preun flow-capture.service

%postun
%systemd_postun flow-capture.service

%files 
%doc README README.fork COPYING ChangeLog
%{_mandir}/man1/flow-capture.1*
%{_mandir}/man1/flow-cat.1*
%{_mandir}/man1/flow-dscan.1*
%{_mandir}/man1/flow-expire.1*
%{_mandir}/man1/flow-export.1*
%{_mandir}/man1/flow-fanout.1*
%{_mandir}/man1/flow-filter.1*
%{_mandir}/man1/flow-gen.1*
%{_mandir}/man1/flow-header.1*
%{_mandir}/man1/flow-import.1*
%{_mandir}/man1/flow-mask.1*
%{_mandir}/man1/flow-merge.1*
%{_mandir}/man1/flow-nfilter.1*
%{_mandir}/man1/flow-print.1*
%{_mandir}/man1/flow-receive.1*
%{_mandir}/man1/flow-report.1*
%{_mandir}/man1/flow-rptfmt.1*
%{_mandir}/man1/flow-send.1*
%{_mandir}/man1/flow-split.1*
%{_mandir}/man1/flow-stat.1*
%{_mandir}/man1/flow-tag.1*
%{_mandir}/man1/flow-tools-examples.1*
%{_mandir}/man1/flow-tools.1*
%{_mandir}/man1/flow-xlate.1*
%{_bindir}/flow-capture
%{_bindir}/flow-cat
%{_bindir}/flow-dscan
%{_bindir}/flow-expire
%{_bindir}/flow-export
%{_bindir}/flow-fanout
%{_bindir}/flow-filter
%{_bindir}/flow-gen
%{_bindir}/flow-header
%{_bindir}/flow-import
%{_bindir}/flow-mask
%{_bindir}/flow-merge
%{_bindir}/flow-nfilter
%{_bindir}/flow-print
%{_bindir}/flow-receive
%{_bindir}/flow-report
%{_bindir}/flow-rptfmt
%{_bindir}/flow-send
%{_bindir}/flow-split
%{_bindir}/flow-stat
%{_bindir}/flow-tag
%{_bindir}/flow-xlate
%{_libdir}/*.so.*
%dir %{_sysconfdir}/%{name}/
%dir %{_sysconfdir}/%{name}/cfg/
%dir %{_sysconfdir}/%{name}/sym/
%config(noreplace) %{_sysconfdir}/%{name}/cfg/*
%config(noreplace) %{_sysconfdir}/%{name}/sym/*
%config(noreplace) %{_sysconfdir}/sysconfig/flow-capture
%{_unitdir}/flow-capture.service
%attr(-,flow-tools,flow-tools) %{_localstatedir}/%{name}/
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_sysusersdir}/flow-tools.conf

%files devel
%{_libdir}/*.so
%{_includedir}/*.h

%files rrdtool
%{_bindir}/flow-rpt2rrd
%{_bindir}/flow-log2rrd
%{_mandir}/man1/flow-rpt2rrd.1*
%{_mandir}/man1/flow-log2rrd.1*

%files docs
%doc docs/*.html ChangeLog.old TODO INSTALL SECURITY

%changelog
%autochangelog

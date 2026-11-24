# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 27d24f279e4b81bd17ecbdcc38e4c42991bb388826c0b200067ce0eb59d3da5b
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           ladspa
Version:        1.17
Release:        1%{?dist}

Summary:        Linux Audio Developer's Simple Plug-in API, examples and tools

License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.ladspa.org/
Source0:        http://www.ladspa.org/download/%{name}_sdk_%{version}.tgz
Patch1:         ladspa-1.17.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  perl-interpreter
BuildRequires:  make
BuildRequires:  pkgconfig(sndfile)

%description
There is a large number of synthesis packages in use or development on
the Linux platform at this time. The Linux Audio Developer's Simple
Plugin API (LADSPA) attempts to give programmers the ability to write
simple `plugin' audio processors in C/C++ and link them dynamically
against a range of host applications.

This package contains the example plug-ins and tools from the LADSPA SDK.

%package        devel
Summary:        Linux Audio Developer's Simple Plug-in API
Requires:       %{name} = %{version}-%{release}

%description    devel
ladspa-devel contains the ladspa.h header file.

Definitive technical documentation on LADSPA plug-ins for both the host
and plug-in is contained within copious comments within the ladspa.h
header file.

%prep
%oreon_sha256
%setup -q -n ladspa_sdk_%{version}
%patch -P1 -p1 -b .0001
perl -pi -e 's/^(CFLAGS.*)-O2(.*)/$1\$\(RPM_OPT_FLAGS\)$2 -DDEFAULT_LADSPA_PATH=\$\(PLUGINDIR\)/' src/Makefile

perl -pi -e 's/-mkdirhier/-mkdir -p/' src/Makefile

perl -pi -e 's/CC(.*)=(.*)cc//' src/makefile
perl -pi -e 's/CPP(.*)=(.*)c\+\+//' src/makefile

cd doc
perl -pi -e "s!HREF=\"ladspa.h.txt\"!href=\"file:///usr/include/ladspa.h\"!" *.html

%build
%set_build_flags
cd src
PLUGINDIR=%{_libdir}/ladspa make targets %{?_smp_mflags} LD="ld --build-id"

%install
cd src
%make_install \
  INSTALL_PLUGINS_DIR=$RPM_BUILD_ROOT%{_libdir}/ladspa \
  INSTALL_INCLUDE_DIR=$RPM_BUILD_ROOT%{_includedir} \
  INSTALL_BINARY_DIR=$RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/ladspa/rdf

%files
%doc doc/COPYING
%dir %{_libdir}/ladspa
%{_libdir}/ladspa/*.so
%{_bindir}/analyseplugin
%{_bindir}/applyplugin
%{_bindir}/listplugins
%{_datadir}/ladspa

%files devel
%doc doc/*.html
%{_includedir}/ladspa.h

%changelog
%autochangelog

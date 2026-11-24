# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 366000427e194d4ce22e272519b608afbebb1fc9915bcf5da924157a8a47fe10
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global __remake_config 0

%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
%ifarch %{ix86}
%global build_type_safety_c 2
%endif
%endif

Name:           libfabric
Version:        2.7.0
Release:        %{autorelease}
Summary:        Open Fabric Interfaces

License:        BSD-2-Clause OR GPL-2.0-only
URL:            https://github.com/ofiwg/libfabric
Source0:        https://github.com/ofiwg/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2

%if %{__remake_config}
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
%endif
BuildRequires:  make
BuildRequires:  libnl3-devel
%ifnarch %{arm}
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
%endif
%ifarch x86_64
%if 0%{?fedora} || 0%{?oreon} || (0%{?rhel} >= 7 && 0%{?rhel} < 10)
BuildRequires:  libpsm2-devel
%endif
BuildRequires:  numactl-devel
%endif

%description
OpenFabrics Interfaces (OFI) is a framework focused on exporting fabric
communication services to applications.  OFI is best described as a collection
of libraries and applications used to export fabric services.  The key
components of OFI are: application interfaces, provider libraries, kernel
services, daemons, and test applications.

Libfabric is a core component of OFI.  It is the library that defines and
exports the user-space API of OFI, and is typically the only software that
applications deal with directly.  It works in conjunction with provider
libraries, which are often integrated directly into libfabric.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -p1 -n %{name}-%{version}

%build
%if %{__remake_config}
./autogen.sh
%endif
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license COPYING
%{_bindir}/fi_info
%{_bindir}/fi_mon_sampler
%{_bindir}/fi_pingpong
%{_bindir}/fi_strerror
%{_libdir}/*.so.1*
%{_mandir}/man1/*.1*

%files devel
%license COPYING
%doc AUTHORS README
%{_includedir}/rdma/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*

%changelog
%autochangelog

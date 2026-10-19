%global source0_hash 8cc99343dc3ea8908cd9710ba1f72a1ddce591bf80bfd7d656dbc4568f560ada
Name:           rtrlib
Version:        0.8.0
Release:        1%{?dist}
Summary:        Small extensible RPKI-RTR-Client C library
Group:          Development/Libraries
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause
URL:            http://rpki.realmv6.org/
Source0:        https://github.com/rtrlib/rtrlib/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Requires:       libssh >= 0.5.0
Patch0: disable-live-tests.patch
# oreon:deps
BuildRequires:  binutils
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libcmocka
BuildRequires:  libssh-devel
BuildRequires:  tar
# /oreon:deps
%description
RTRlib is an open-source C implementation of the  RPKI/Router Protocol
client. The library allows one to fetch and store validated prefix origin
data from a RTR-cache and performs origin verification of prefixes. It
supports different types of transport sessions (e.g., SSH, unprotected TCP)
and is easily extendable.

%package devel
Summary:        Small extensible RPKI-RTR-Client C library. Development files
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libssh-devel >= 0.5.0
%description devel
RTRlib is an open-source C implementation of the  RPKI/Router Protocol
client. The library allows one to fetch and store validated prefix origin
data from a RTR-cache and performs origin verification of prefixes. It
supports different types of transport sessions (e.g., SSH, unprotected TCP)
and is easily extendable.

This package contains development files.

%package doc
Summary:        Small extensible RPKI-RTR-Client C library. Documentation
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
RTRlib is an open-source C implementation of the  RPKI/Router Protocol
client. The library allows one to fetch and store validated prefix origin
data from a RTR-cache and performs origin verification of prefixes. It
supports different types of transport sessions (e.g., SSH, unprotected TCP)
and is easily extendable.
.
This package contains documentation files.

%package -n rtr-tools
Summary:        RPKI-RTR command line tools
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n rtr-tools
Tools for the RTRlib
Rtrclient is command line that connects to an RPKI-RTR server and prints
protocol information and information about the fetched ROAs to the console.
Rpki-rov is a command line tool that connects to an RPKI-RTR server and
allows to validate given IP prefixes and origin ASes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5 .
%cmake_build %{?_smp_mflags}
%install
%cmake_install
%ldconfig_scriptlets
%oreon_autofiles rtr-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%cmake_build --target test
%files -f %{oreon_filedir}/main.list
%files -n rtrlib-devel -f %{oreon_filedir}/rtrlib-devel.list
%files -n rtrlib-doc -f %{oreon_filedir}/rtrlib-doc.list
%files -n rtr-tools -f %{oreon_filedir}/rtr-tools.list

%changelog

%autochangelog

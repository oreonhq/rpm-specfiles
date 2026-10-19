%global source0_hash 5c278793269dbbf98d5f1592c797234581df69088d2838a14154b4af52ebd133
Name:               json-parser
Version:            1.1.0
Release:        1%{?dist}
Summary:        Very low footprint JSON parser written in portable ANSI C
License:            LicenseRef-Callaway-BSD
URL:                https://github.com/udp/json-parser
Source0:        https://github.com/udp/json-parser/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:             0001-improve-pkgconfig-module-close-37.patch
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Very low footprint JSON parser written in portable ANSI C

%package devel
Summary:            Files needed to develop applications with Very low footprint JSON parser
Requires:           %{name}%{?_isa} = %{version}-%{release}
%description devel
Files needed to develop applications with Very low footprint JSON parser

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .pkgconfig

%build

autoreconf -vfi
%configure
make %{?_smp_mflags}
%install
make install-shared DESTDIR=%{buildroot}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n json-parser-devel -f %{oreon_filedir}/json-parser-devel.list

%changelog

%autochangelog

%global source0_hash 9ff90d85ff613e81659a2d661515e01d3c1f3ad1cade58908838b97fdd7ab5d2
Name:		serialdv
Version:	1.1.5
Release:        1%{?dist}
Summary:        C++ minimal interface to encode/decode audio with AMBE3000 based devices
License:	GPL-3.0-only
URL:		https://github.com/f4exb/serialdv
Source0:        https://github.com/f4exb/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
C++ minimal interface to encode and decode audio with AMBE3000 based devices
in packet mode over a serial link.

%package devel
Summary:	Development files for serialdv
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for serialdv.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir serialDV-%{version}
%oreon_prep
%build

%cmake -DCMAKE_SKIP_RPATH=TRUE
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n serialdv-devel -f %{oreon_filedir}/serialdv-devel.list

%changelog

%autochangelog

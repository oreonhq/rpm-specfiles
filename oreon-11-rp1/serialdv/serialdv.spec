%global source0_hash 9ff90d85ff613e81659a2d661515e01d3c1f3ad1cade58908838b97fdd7ab5d2

Name:		serialdv
Version:	1.1.5
Release:	2%{?dist}
Summary:	C++ minimal interface to encode/decode audio with AMBE3000 based devices
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:	GPL-3.0-only
URL:		https://github.com/f4exb/serialdv
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	make

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

%autosetup -n serialDV-%{version} -p1

%build
%cmake -DCMAKE_SKIP_RPATH=TRUE
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc Readme.md
%{_bindir}/dvtest
%{_libdir}/libserialdv.so.1*

%files devel
%{_includedir}/*
%{_libdir}/libserialdv.so

%changelog
%autochangelog

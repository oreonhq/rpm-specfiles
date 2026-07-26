%global source0_hash f77205ff29f240b3f0e9aa3abaa8855e8c247879458d5bc542c3eaaaf22ef053

Name: libtfmxaudiodecoder
Version: 1.0.2
Release: 1%{?dist}

Summary: C wrapper library for TFMX & FC music files
License: GPL-2.0-or-later
URL: https://github.com/mschwendt/libtfmxaudiodecoder
Source0: https://github.com/mschwendt/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: make

%description
This music player backend library provides a C API for TFMX and
Future Composer music files from the Commodore Amiga era of computing.

%package devel
Summary: Files needed for developing with %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the files that are needed when building
software that uses %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md README_BAD.md TFMX.md TFMX_HIP_FC.md
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/tfmxaudiodecoder.h

%changelog
%autochangelog

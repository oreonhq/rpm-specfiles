%global source0_hash 0a6d42cd6c21e925a27fa560dc45ac80057d275f23342102825909c02d3b1249
Name:       libltc
Version:    1.3.2
Release:        1%{?dist}
Summary:        Linear/Longitudinal Time Code (LTC) Library
License:    LGPL-3.0-or-later
URL:        http://x42.github.io/libltc/
Source0:        https://github.com/x42/%{name}/releases/download/v%{version}/libltc-%{version}.tar.gz
Patch0:     libltc-1.3.2-multilib.patch
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Linear (or Longitudinal) Timecode (LTC) is an encoding of time code data as a
Manchester-Biphase encoded audio signal. The audio signal is commonly recorded
on a VTR track or other storage media.

libltc provides functionality to encode and decode LTC from/to time code,
including SMPTE date support.

%package devel
Summary:    Development files for libltc
Requires:   %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
This package contains the libraries and header files needed for
developing with libltc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1 -b .multilib

%build

%configure
make %{?_smp_mflags} all dox
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/libltc.{a,la}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make check
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libltc-devel -f %{oreon_filedir}/libltc-devel.list

%changelog

%autochangelog

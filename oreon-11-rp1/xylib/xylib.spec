%global source0_hash b641cb33fa01732b8203356e0978384f9551bf415cfbae5989b3a233b3cb0ec7
Name: xylib
Summary:        Library for reading x-y data from several file formats
Version: 1.6
Release:        1%{?dist}
License: LGPL-2.1-only
Url: http://xylib.sourceforge.net/
Source0:        https://github.com/wojdyr/xylib/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  bzip2-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  wxGTK-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
C++ library for reading files that contain x-y data from powder diffraction, 
spectroscopy or other experimental methods. The supported formats include:
VAMAS, pdCIF, Bruker UXD and RAW, Philips UDF and RD, Rigaku DAT, 
Sietronics CPI, DBWS/DMPLOT, Koalariet XDD and others.

%package devel
Summary: Development files for xylib
Requires: %{name} = %{version}-%{release}
Requires: boost-devel
%description devel
Files needed for developing apps using xylib.
xylib is a C++ library for reading files that contain x-y data from 
powder diffraction, spectroscopy or other experimental methods.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static --with-wx-config=wx-config-3.2
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n xylib-devel -f %{oreon_filedir}/xylib-devel.list

%changelog

%autochangelog

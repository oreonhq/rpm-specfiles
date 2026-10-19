%global source0_hash 5d66ff1d692e88f905e363ec9bc9daa3692aee330f950c831daf7222342d91e7
Name: milia
Version: 1.0.0
Release:        1%{?dist}
Summary:        C++ cosmology library
License: GPL-3.0-or-later
URL: http://guaix.fis.ucm.es/projects/milia/wiki
Source0:        ftp://astrax.fis.ucm.es/pub/software/%{name}/%{name}-%{version}.tar.xz
Patch0: milia.cxx11.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel
BuildRequires:  make
# /oreon:deps
%description
Milia is a C++ library created to compute cosmological distances and 
ages in the Friedmann-Lemaître-Robertson-Walker metric. 
The luminosity distance is 
computed using elliptical functions (Kantowski, Kao, Thomas 2000). 
The remaining distances are computed from the luminosity distance using 
Hogg 1999. The age is computed following Thomas & Kantowski 2000, using also 
elliptical functions.

%package devel
Summary: Headers for developing programs that will use %{name}
Requires: boost-devel
Requires: %{name} = %{version}-%{release}
%description devel
These are the header files and libraries needed to develop a %{name} 
application.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

%configure --enable-static=no --enable-shared=yes
make %{?_smp_mflags}
%check

make %{?_smp_mflags} check
%install
make %{?_smp_mflags} install DESTDIR=%{buildroot}
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n milia-devel -f %{oreon_filedir}/milia-devel.list

%changelog

%autochangelog

%global source0_hash e675a2476bd407b8d97a33f93c6651ad3ecdfd422916f260bd620f2aec7ca45f
Name:           libspnav
Version:        1.2
Release:        1%{?dist}
Summary:        Open source alternative to 3DConnextion drivers
License:        LicenseRef-Callaway-BSD
URL:            http://spacenav.sourceforge.net/
Source0:        https://github.com/FreeSpacenav/libspnav/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libX11-devel
BuildRequires:  make
# /oreon:deps
%description
The spacenav project provides a free, compatible alternative to the proprietary
3Dconnexion device driver and SDK, for their 3D input devices (called "space
navigator", "space pilot", "space traveller", etc).

This package provides the library needed for applications to connect to the 
user land daemon.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel
%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

sed -i "s/libdir=lib/libdir=%{_lib}/g" configure
%configure 
sed -i "s/CFLAGS =/CFLAGS +=/g" Makefile
%make_build
%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}.a
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libspnav-devel -f %{oreon_filedir}/libspnav-devel.list

%changelog

%autochangelog

%global source0_hash cbe9d2d7c5ba03ad29df8f56ce199e3ebf092827c609fd8177e86536e59997a5
%global with_fips 1
Summary:        Library for accessing ICA hardware crypto on IBM z Systems
Name: libica
Version: 4.4.2
Release:        1%{?dist}
License: CPL-1.0
URL: https://github.com/opencryptoki/
Source0:        https://github.com/opencryptoki/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0: %{name}-4.0.0-annotate.patch
ExclusiveArch: s390 s390x
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
# /oreon:deps
%description
A library of functions and utilities for accessing ICA hardware crypto on
IBM z Systems.

%package devel
Summary: Development tools for programs to access ICA hardware crypto on IBM z Systems
Requires: %{name} = %{version}-%{release}
Requires: openssl-devel
%description devel
The libica-devel package contains the header files and static
libraries necessary for developing programs accessing ICA hardware crypto on
IBM z Systems.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

sh ./bootstrap.sh

%build

CPPFLAGS=-DNO_FIPS_CONFIG_LOAD
export CPPFLAGS
%configure --disable-static \
    --enable-fips
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/libica*.la
rm %{buildroot}%{_pkgdocdir}/{INSTALL,README.md}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

if [ -c /dev/hwrng -o -c /dev/prandom ]; then
    make check
fi
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    make fipsinstall DESTDIR=%{buildroot}
    %{nil}
%files -f %{oreon_filedir}/main.list
%files -n libica-devel -f %{oreon_filedir}/libica-devel.list

%changelog

%autochangelog

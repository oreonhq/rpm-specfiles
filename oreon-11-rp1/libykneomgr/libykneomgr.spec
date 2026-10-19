%global source0_hash 2749ef299a1772818e63c0ff5276f18f1694f9de2137176a087902403e5df889
Name:           libykneomgr
Version:        0.1.8
Release:        1%{?dist}
Summary:        YubiKey NEO CCID Manager C Library
License:        GPL-3.0-or-later
URL:            http://opensource.yubico.com/%{name}/
Source0:        http://opensource.yubico.com/%{name}/releases/%{name}-%{version}.tar.gz
Provides:       bundled(gnulib)
Provides:       ykneomgr = %{version}-%{release}  
# oreon:deps
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  libzip-devel
BuildRequires:  make
BuildRequires:  pcsc-lite
BuildRequires:  pcsc-lite-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description 
C Library and tool to manage CCID-aspects of YubiKey NEO

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the header files needed to develop applications that
use libykneomgr.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-rpath --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
LD_LIBRARY_PATH="$(pwd)/lib/.libs" make %{?_smp_mflags}
%check

LD_LIBRARY_PATH="$(pwd)/lib/.libs" make check
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libykneomgr-devel -f %{oreon_filedir}/libykneomgr-devel.list

%changelog

%autochangelog

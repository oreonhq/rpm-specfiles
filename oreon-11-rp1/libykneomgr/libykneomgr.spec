%global source0_hash 2749ef299a1772818e63c0ff5276f18f1694f9de2137176a087902403e5df889

Name:           libykneomgr
Version:        0.1.8
Release:        25%{?dist}
Summary:        YubiKey NEO CCID Manager C Library

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://opensource.yubico.com/%{name}/
Source0:        http://opensource.yubico.com/%{name}/releases/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libzip-devel pcsc-lite pcsc-lite-devel
BuildRequires:  zlib-devel help2man
BuildRequires: make

# Bundled gnulib https://fedorahosted.org/fpc/ticket/174
Provides:       bundled(gnulib)
Provides:       ykneomgr = %{version}-%{release}  

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

# --disable-rpath doesn't work.
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# We need LD_LIBRARY_PATH so help2man can run ykneomgr.

LD_LIBRARY_PATH="$(pwd)/lib/.libs" make %{?_smp_mflags}

%check
LD_LIBRARY_PATH="$(pwd)/lib/.libs" make check

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%{_bindir}/ykneomgr
%{_libdir}/*.so.*
%{_mandir}/man1/ykneomgr.1.*
%doc %{_datadir}/gtk-doc/html/%{name}

%files devel
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/*

%changelog
%autochangelog

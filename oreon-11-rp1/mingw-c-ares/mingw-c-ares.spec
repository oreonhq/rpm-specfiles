%global source0_hash 4803c844ce20ce510ef0eb83f8ea41fa24ecaae9d280c468c582d2bb25b3913d
%{?mingw_package_header}
Name:           mingw-c-ares
Version:        1.34.8
Release:        1%{?dist}
Summary:        Library that performs asynchronous DNS operations
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND ISC
URL:            http://c-ares.haxx.se/
Source0:        http://c-ares.haxx.se/download/c-ares-%{version}.tar.gz
Patch0:         0001-Use-RPM-compiler-options.patch
Patch1:         mingw-c-ares_libs-in-ldflags.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package -n mingw32-c-ares
Summary:        Library that performs asynchronous DNS operations
%description -n mingw32-c-ares
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

This package is MinGW compiled c-ares library for the Win32 target.

%package -n mingw64-c-ares
Summary:        Library that performs asynchronous DNS operations
%description -n mingw64-c-ares
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

This package is MinGW compiled c-ares library for the Win64 target.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n c-ares-%{version}
%patch -P0 -p1 -b .optflags
%patch -P1 -p1 -b .ldflags

%build

autoreconf -if
%mingw_configure --enable-shared --disable-static \
                 --disable-dependency-tracking
%mingw_make %{?_smp_mflags}
%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT
rm -f ${RPM_BUILD_ROOT}%{mingw32_libdir}/libcares.la
rm -f ${RPM_BUILD_ROOT}%{mingw64_libdir}/libcares.la
rm -rf ${RPM_BUILD_ROOT}%{mingw32_mandir}
rm -rf ${RPM_BUILD_ROOT}%{mingw64_mandir}
%oreon_autofiles mingw32-c-ares usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-c-ares usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-c-ares -f %{oreon_filedir}/mingw32-c-ares.list
%files -n mingw64-c-ares -f %{oreon_filedir}/mingw64-c-ares.list

%changelog

%autochangelog

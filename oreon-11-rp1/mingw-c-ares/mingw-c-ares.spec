%global source0_hash 4803c844ce20ce510ef0eb83f8ea41fa24ecaae9d280c468c582d2bb25b3913d

%{?mingw_package_header}

Name:           mingw-c-ares
Version:        1.17.2
Release:        13%{?dist}
Summary:        Library that performs asynchronous DNS operations

# ares_getopt.c ares_getopt.h are BSD (3 clause)
# bitncmp.c inet_net_pton.c inet_ntop.c are ISC
# rest is MIT
# Automatically converted from old format: MIT and BSD and ISC - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND ISC
URL:            http://c-ares.haxx.se/
Source0:        http://c-ares.haxx.se/download/c-ares-%{version}.tar.gz
Patch0:         0001-Use-RPM-compiler-options.patch
# Don't fail on -lssp in LDFLAGS
# It's probably true that -lxxx belongs to LIBS, but we don't have that in the mingw macros,
# and no-one else seems to care with link libs are added to LDFLAGS
Patch1:         mingw-c-ares_libs-in-ldflags.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

%description
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package -n mingw32-c-ares
Summary:        %{summary}

%description -n mingw32-c-ares
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

This package is MinGW compiled c-ares library for the Win32 target.

%package -n mingw64-c-ares
Summary:        %{summary}

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
# remove libtool files
rm -f ${RPM_BUILD_ROOT}%{mingw32_libdir}/libcares.la
rm -f ${RPM_BUILD_ROOT}%{mingw64_libdir}/libcares.la
# remove documentation (it's in the native version)
rm -rf ${RPM_BUILD_ROOT}%{mingw32_mandir}
rm -rf ${RPM_BUILD_ROOT}%{mingw64_mandir}

%files -n mingw32-c-ares
%license LICENSE.md
%{mingw32_bindir}/*.dll
%{mingw32_includedir}/ares.h
%{mingw32_includedir}/ares_build.h
%{mingw32_includedir}/ares_dns.h
%{mingw32_includedir}/ares_rules.h
%{mingw32_includedir}/ares_version.h
%{mingw32_libdir}/*.dll.a
%{mingw32_libdir}/pkgconfig/libcares.pc

%files -n mingw64-c-ares
%license LICENSE.md
%{mingw64_bindir}/*.dll
%{mingw64_includedir}/ares.h
%{mingw64_includedir}/ares_build.h
%{mingw64_includedir}/ares_dns.h
%{mingw64_includedir}/ares_rules.h
%{mingw64_includedir}/ares_version.h
%{mingw64_libdir}/*.dll.a
%{mingw64_libdir}/pkgconfig/libcares.pc

%changelog
%autochangelog

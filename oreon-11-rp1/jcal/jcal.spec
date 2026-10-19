%global source0_hash e8983ecad029b1007edc98458ad13cd9aa263d4d1cf44a97e0a69ff778900caa
Name:           jcal
Version:        0.4.1
Release:        1%{?dist}
Summary:        Unix cal-like interface to libjalali
License:        GPL-3.0-or-later
URL:            http://nongnu.org/jcal/
Source0:        http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
This package provides two applications: jcal and jdate which use libjalali
for calendar calculation.

jcal is a UNIX cal-like tool to display calendar based on Jalali calendar
system.

jdate is UNIX date-like tool to display date and time based on Jalali 
calendar system.

%package -n libjalali
Summary:        A library providing Jalali calendar functions
%description -n libjalali
Jalali calendar is a small and portable free software library to manipulate
date and time in Jalali calendar system. It's written in C and has absolutely
zero dependencies. It works on top of any POSIX.1-2001 (and later) compatible
libc implementations. Jalali calendar provides an API similar to that of 
libc's timezone, date and time functions.

%package -n libjalali-devel
Summary:        Development files for libjalali
Requires:       libjalali%{?_isa} = %{version}-%{release}
%description -n libjalali-devel
The libjalali-devel package contains libraries and header files for
developing applications that use libjalali.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

%build

./autogen.sh
%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -f %{buildroot}/%{_libdir}/*.la
%ldconfig_scriptlets -n libjalali
%oreon_autofiles libjalali usr/*/lib*.so.*
%oreon_autofiles libjalali-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libjalali -f %{oreon_filedir}/libjalali.list
%files -n libjalali-devel -f %{oreon_filedir}/libjalali-devel.list

%changelog

%autochangelog

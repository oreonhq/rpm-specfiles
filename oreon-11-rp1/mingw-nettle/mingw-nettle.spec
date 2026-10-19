%global source1_hash b617851da180b7a7ee8cdb34e4a9269eaa9ba3c3cfc69a64d0cbcfd0ae42a4d5
%global source0_hash 3addbc00da01846b232fb3bc453538ea5468da43033f21bb345cb1e9073f5094
%{?mingw_package_header}
Name:           mingw-nettle
Version:        4.0
Release:        1%{?dist}
Summary:        MinGW package for nettle cryptographic library
License: LGPL-3.0-or-later OR GPL-2.0-or-later
URL:    http://www.lysator.liu.se/~nisse/nettle/
Source0:        http://www.lysator.liu.se/~nisse/archive/nettle-%{version}.tar.gz
Source1: http://www.lysator.liu.se/~nisse/archive/nettle-%{version}.tar.gz.sig
Source2: nettle-release-keyring.gpg
Patch1:  nettle-3.10-hobble-to-configure.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gmp
BuildRequires:  mingw32-openssl
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gmp
BuildRequires:  mingw64-openssl
# /oreon:deps
%description
Nettle is a cryptographic library that is designed to fit easily in
more or less any context: In crypto toolkits for object-oriented
languages (C++, Python, Pike, ...), in applications like LSH or GNUPG,
or even in kernel space.

# Mingw32
%package -n mingw32-nettle
Summary: MinGW package for nettle cryptographic library
%description -n mingw32-nettle
Nettle is a cryptographic library that is designed to fit easily in
more or less any context: In crypto toolkits for object-oriented
languages (C++, Python, Pike, ...), in applications like LSH or GNUPG,
or even in kernel space.

# Mingw64
%package -n mingw64-nettle
Summary: MinGW package for nettle cryptographic library
%description -n mingw64-nettle
Nettle is a cryptographic library that is designed to fit easily in
more or less any context: In crypto toolkits for object-oriented
languages (C++, Python, Pike, ...), in applications like LSH or GNUPG,
or even in kernel space.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -Tb 0 -p1 -n nettle-%{version}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%build

autoreconf -ifv
%mingw_configure --enable-shared --enable-fat \
  --disable-sm3 --disable-sm4 --disable-ecc-secp192r1 --disable-ecc-secp224r1
%mingw_make %{?_smp_mflags}
%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libnettle.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libnettle.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libhogweed.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libhogweed.a
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir}/
rm -rf $RPM_BUILD_ROOT%{mingw64_infodir}/
%oreon_autofiles mingw32-nettle usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-nettle usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-nettle -f %{oreon_filedir}/mingw32-nettle.list
%files -n mingw64-nettle -f %{oreon_filedir}/mingw64-nettle.list

%changelog

%autochangelog

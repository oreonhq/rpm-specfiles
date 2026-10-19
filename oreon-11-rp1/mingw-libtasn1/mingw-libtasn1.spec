%global source1_hash a81037649b953c9ecb2e8f8fa24cb5c79456fd9af31499d6b753fa6569656807
%global source0_hash 1d8a444a223cc5464240777346e125de51d8e6abf0b8bac742ac84609167dc87
%{?mingw_package_header}
Name:           mingw-libtasn1
Version:        4.21.0
Release:        1%{?dist}
Summary:        MinGW Windows libtasn1 library
License:        LGPL-2.1-or-later
URL:            http://www.gnu.org/software/libtasn1/
Source0:        http://ftp.gnu.org/gnu/libtasn1/libtasn1-%{version}.tar.gz
Source1:        http://ftp.gnu.org/gnu/libtasn1/libtasn1-%{version}.tar.gz.sig
BuildArch:      noarch
# oreon:deps
BuildRequires:  bison
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
libtasn1 is the ASN.1 library used in GNUTLS.

This package contains the MinGW Windows cross compiled libtasn1 library.

%package -n mingw32-libtasn1
Summary:        MinGW Windows libtasn1 library
Requires:       pkgconfig
%description -n mingw32-libtasn1
A library that provides Abstract Syntax Notation One (ASN.1, as specified
by the X.680 ITU-T recommendation) parsing and structures management, and
Distinguished Encoding Rules (DER, as per X.690) encoding and decoding functions.

This package contains the MinGW Windows cross compiled libtasn1 library.

%package -n mingw64-libtasn1
Summary:        MinGW Windows libtasn1 library
Requires:       pkgconfig
%description -n mingw64-libtasn1
A library that provides Abstract Syntax Notation One (ASN.1, as specified
by the X.680 ITU-T recommendation) parsing and structures management, and
Distinguished Encoding Rules (DER, as per X.690) encoding and decoding functions.

This package contains the MinGW Windows cross compiled libtasn1 library.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libtasn1-%{version}

%build

%mingw_configure --disable-static --disable-gcc-warnings
%mingw_make_build
%install
%mingw_make_install
rm -rf %{buildroot}%{mingw32_datadir}/info/
rm -rf %{buildroot}%{mingw64_datadir}/info/
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -f %{buildroot}%{mingw32_libdir}/{*.la,*.def}
rm -f %{buildroot}%{mingw64_libdir}/{*.la,*.def}
rm -f %{buildroot}%{mingw32_bindir}/*.exe
rm -f %{buildroot}%{mingw64_bindir}/*.exe
%oreon_autofiles mingw32-libtasn1 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libtasn1 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libtasn1 -f %{oreon_filedir}/mingw32-libtasn1.list
%files -n mingw64-libtasn1 -f %{oreon_filedir}/mingw64-libtasn1.list

%changelog

%autochangelog

%global source0_hash fe9ff51cb1f2abb5e65a6b8c10a92da0ab5ab6eaf26e7fc2b675c45f1fb519b5

%{?mingw_package_header}

Name:           mingw-nettle
Version:        3.10.2
Release:        2%{?dist}

Summary: MinGW package for nettle cryptographic library
# Automatically converted from old format: LGPLv3+ or GPLv2+ - review is highly recommended.
License: LGPL-3.0-or-later OR GPL-2.0-or-later
URL:    http://www.lysator.liu.se/~nisse/nettle/

Source0: http://www.lysator.liu.se/~nisse/archive/nettle-%{version}.tar.gz
Source1: http://www.lysator.liu.se/~nisse/archive/nettle-%{version}.tar.gz.sig
Source2: nettle-release-keyring.gpg
# MinGW does not support explicit_bzero()
#Patch0:  nettle-3.8-zeroize-stack.patch
Patch1:  nettle-3.10-hobble-to-configure.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-gmp
BuildRequires:  mingw64-gmp
BuildRequires:  mingw32-openssl
BuildRequires:  mingw64-openssl

BuildRequires:  autoconf, automake
BuildRequires:  gcc
BuildRequires:  m4

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

# Clean out files that should not be part of the rpm.
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libnettle.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libnettle.a
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libhogweed.a
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libhogweed.a
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir}/
rm -rf $RPM_BUILD_ROOT%{mingw64_infodir}/

# Win32
%files -n mingw32-nettle
%doc README
%license COPYINGv2 COPYING.LESSERv3
%{mingw32_bindir}/nettle-hash.exe
%{mingw32_bindir}/nettle-lfib-stream.exe
%{mingw32_bindir}/nettle-pbkdf2.exe
%{mingw32_bindir}/pkcs1-conv.exe
%{mingw32_bindir}/sexp-conv.exe
%{mingw32_bindir}/libnettle-8.dll
%{mingw32_bindir}/libhogweed-6.dll
%{mingw32_libdir}/libnettle.dll.a
%{mingw32_libdir}/libhogweed.dll.a
%{mingw32_libdir}/pkgconfig/nettle.pc
%{mingw32_libdir}/pkgconfig/hogweed.pc
%dir %{mingw32_includedir}/nettle
%{mingw32_includedir}/nettle/*.h

# Win64
%files -n mingw64-nettle
%doc README
%license COPYINGv2 COPYING.LESSERv3
%{mingw64_bindir}/nettle-hash.exe
%{mingw64_bindir}/nettle-lfib-stream.exe
%{mingw64_bindir}/nettle-pbkdf2.exe
%{mingw64_bindir}/pkcs1-conv.exe
%{mingw64_bindir}/sexp-conv.exe
%{mingw64_bindir}/libnettle-8.dll
%{mingw64_bindir}/libhogweed-6.dll
%{mingw64_libdir}/libnettle.dll.a
%{mingw64_libdir}/libhogweed.dll.a
%{mingw64_libdir}/pkgconfig/nettle.pc
%{mingw64_libdir}/pkgconfig/hogweed.pc
%dir %{mingw64_includedir}/nettle
%{mingw64_includedir}/nettle/*.h

%changelog
%autochangelog

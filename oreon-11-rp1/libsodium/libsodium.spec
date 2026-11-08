# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash adbdd8f16149e81ac6078a03aca6fc03b592b89ef7b5ed83841c086191be3349
%global source1_hash c0186d6cf8c9c2ec5c6dbb6d4ff4f701e5592376490e8ad97a4ceeecabbff0f3

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global libname libsodium
%global soname  26
# Uncomment to update to final version
#global versuf  -stable

%bcond_without  mingw


Name:           libsodium
Version:        1.0.22
Release:        1%{?dist}
Summary:        The Sodium crypto library
# Most source code is ISC, except:
# BSD-2-Clause:
#   src/libsodium/crypto_hash/sha256/cp/hash_sha256_cp.c
#   src/libsodium/crypto_hash/sha512/cp/hash_sha512_cp.c
#   src/libsodium/crypto_pwhash/scryptsalsa208sha256/crypto_scrypt.h
#   src/libsodium/crypto_pwhash/scryptsalsa208sha256/nosse/pwhash_scryptsalsa208sha256_nosse.c
#   src/libsodium/crypto_pwhash/scryptsalsa208sha256/pbkdf2-sha256.c
#   src/libsodium/crypto_pwhash/scryptsalsa208sha256/pbkdf2-sha256.h
#   src/libsodium/crypto_pwhash/scryptsalsa208sha256/sse/pwhash_scryptsalsa208sha256_sse.c
# CC0-1.0:
#   src/libsodium/crypto_pwhash/argon2/argon2-encoding.c
License:        ISC AND BSD-2-Clause AND CC0-1.0
URL:            https://libsodium.org/

Source0:        https://download.libsodium.org/libsodium/releases/libsodium-%{version}.tar.gz
Source1:        https://download.libsodium.org/libsodium/releases/libsodium-%{version}.tar.gz.minisig

BuildRequires: minisign
BuildRequires: gcc
BuildRequires: make

%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc

BuildRequires: mingw64-gcc
BuildRequires: mingw64-filesystem
BuildRequires:  oreon-rpm-macros
%endif

# manage update from 3rd party repository
Obsoletes:      %{libname}%{soname} <= %{version}


%description
Sodium is a new, easy-to-use software library for encryption, decryption, 
signatures, password hashing and more. It is a portable, cross-compilable, 
installable, packageable fork of NaCl, with a compatible API, and an extended 
API to improve usability even further. Its goal is to provide all of the core 
operations needed to build higher-level cryptographic tools. The design 
choices emphasize security, and "magic constants" have clear rationales.

The same cannot be said of NIST curves, where the specific origins of certain 
constants are not described by the standards. And despite the emphasis on 
higher security, primitives are faster across-the-board than most 
implementations of the NIST standards.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{libname}%{soname}-devel <= %{version}

%description    devel
This package contains libraries and header files for
developing applications that use %{name} libraries.

%package        static
Summary:        Static library for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Obsoletes:      %{libname}%{soname}-static <= %{version}

%description    static
This package contains the static library for statically
linking applications to use %{name}.

%if %{with mingw}
%package -n     mingw32-%{name}
Summary:        MinGW compiled %{name} library for Win32 target
BuildArch:      noarch

%description -n mingw32-%{name}
This package contains the MinGW compiled library of %{name}
for Win32 target.

%package -n     mingw64-%{name}
Summary:        MinGW compiled %{name} library for Win64 target
BuildArch:      noarch

%description -n mingw64-%{name}
This package contains the MinGW compiled library of %{name}
for Win64 target.

%{?mingw_debug_package}
%endif


%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -

# https://doc.libsodium.org/installation#integrity-checking
minisign -VP RWQf6LRCGA9i53mlYecO4IzT51TGPpvWucNSCh1CBM0QTaLn73Y7GFO3 -m %{SOURCE0}


%setup -q -n %{name}%{?versuf}%{!?versuf:-%{version}}


%build
# This package has a configure test which uses ASMs, but does not link the
# resultant .o files.  As such the ASM test is always successful, even on
# architectures were the ASM is not valid when compiling with LTO.
#
# -ffat-lto-objects is sufficient to address this issue.  It is the default
# for F33, but is expected to only be enabled for packages that need it in
# F34, so we use it here explicitly
%define _lto_cflags -flto=auto -ffat-lto-objects

mkdir build_native
pushd build_native
%global _configure ../configure
%configure \
  --disable-silent-rules \
  --disable-opt

%make_build
popd

%if %{with mingw}
%mingw_configure \
  --disable-silent-rules \
  --disable-opt

%mingw_make_build
%endif


%install
%make_install -C build_native

rm %{buildroot}%{_libdir}/%{libname}.la

%if %{with mingw}
%mingw_make_install
rm %{buildroot}%{mingw32_libdir}/libsodium.a
rm %{buildroot}%{mingw64_libdir}/libsodium.a
%mingw_debug_install_post
%endif


%check
make -C build_native check


%files
%license LICENSE
%{_libdir}/%{libname}.so.%{soname}*

%files devel
%doc AUTHORS ChangeLog README.markdown THANKS
%doc test/default/*.{c,exp,h}
%doc test/quirks/quirks.h
%{_includedir}/sodium.h
%{_includedir}/sodium/
%{_libdir}/%{libname}.so
%{_libdir}/pkgconfig/%{libname}.pc

%files static
%{_libdir}/libsodium.a

%if %{with mingw}
%files -n mingw32-%{name}
%license LICENSE
%{mingw32_bindir}/*.{dll,def}
%{mingw32_includedir}/sodium.h
%{mingw32_includedir}/sodium/
%{mingw32_libdir}/pkgconfig/libsodium.pc
%{mingw32_libdir}/libsodium.dll.a

%files -n mingw64-%{name}
%license LICENSE
%{mingw64_bindir}/*.{dll,def}
%{mingw64_includedir}/sodium.h
%{mingw64_includedir}/sodium/
%{mingw64_libdir}/pkgconfig/libsodium.pc
%{mingw64_libdir}/libsodium.dll.a
%endif



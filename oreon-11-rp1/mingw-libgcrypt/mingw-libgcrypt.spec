%global source0_hash 8b0870897ac5ac67ded568dcfadf45969cfa8a6beb0fd60af2a9eadc2a3272aa

%?mingw_package_header

%global run_tests 0

Name:           mingw-libgcrypt
Version:        1.10.3
Release:        6%{?dist}
Summary:        MinGW Windows gcrypt encryption library

# Automatically converted from old format: LGPLv2+ and GPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later

URL:            ftp://ftp.gnupg.org/gcrypt/libgcrypt/
Source0: https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2
Source1: https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2.sig
Source2: wk@g10code.com

# Pass the annobin flags to the libgcrypt.so (#2016349)
Patch1: libgcrypt-1.10.1-annobin.patch

# MinGW-specific patches

# Workaround a bug in libtool:
# libgcrypt-use-correct-def-file.patch
Patch1000:      libgcrypt-use-correct-def-file.patch

BuildArch:      noarch

BuildRequires:  autoconf, automake, libtool
BuildRequires:  make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-libgpg-error

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-libgpg-error

BuildRequires:  gcc
#BuildRequires:  autoconf automake libtool

%if %run_tests
BuildRequires:  wine
%endif

%description
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.

This is a Windows cross-compiled version of the library.

# Win32
%package -n mingw32-libgcrypt
Summary:        MinGW Windows gcrypt encryption library

%description -n mingw32-libgcrypt
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.

This is a Windows cross-compiled version of the library.

%package -n mingw32-libgcrypt-static
Summary:        Static library for mingw32-libgcrypt development
Requires:       mingw32-libgcrypt = %{version}-%{release}
Requires:       mingw32-libgpg-error-static

%description -n mingw32-libgcrypt-static
Static library for mingw32-libgcrypt development.

# Win64
%package -n mingw64-libgcrypt
Summary:        MinGW Windows gcrypt encryption library

%description -n mingw64-libgcrypt
Libgcrypt is a general purpose crypto library based on the code used
in GNU Privacy Guard.

This is a Windows cross-compiled version of the library.

%package -n mingw64-libgcrypt-static
Summary:        Static library for mingw64-libgcrypt development
Requires:       mingw64-libgcrypt = %{version}-%{release}
Requires:       mingw64-libgpg-error-static

%description -n mingw64-libgcrypt-static
Static library for mingw64-libgcrypt development.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libgcrypt-%{version}
%patch -P1 -p1

%patch -P1000 -p0 -b .def

autoreconf -i --force

%build
MINGW64_CONFIGURE_ARGS="ac_cv_sys_symbol_underscore=no --disable-padlock-support"
%mingw_configure --enable-shared --enable-static --enable-pubkey-ciphers='dsa elgamal rsa ecc'
%mingw_make %{?_smp_mflags}

%check
%if %run_tests
# Stupid Wine doesn't load DLLs from the PATH any
# more, so libtool scripts don't work.  As a result
# we need to use the following Big Hack.
make -C build_win32/tests check ||:
pushd build_win32/src/.libs
for t in $(pwd)/../../tests/*.exe; do
  wine $t
done
popd
%endif

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT

# Remove info pages which duplicate what is in Fedora natively.
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir}
rm -rf $RPM_BUILD_ROOT%{mingw64_infodir}

rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

rm $RPM_BUILD_ROOT%{mingw32_libdir}/libgcrypt.def
rm $RPM_BUILD_ROOT%{mingw64_libdir}/libgcrypt.def

rm $RPM_BUILD_ROOT%{mingw32_libdir}/libgcrypt.la
rm $RPM_BUILD_ROOT%{mingw64_libdir}/libgcrypt.la

%files -n mingw32-libgcrypt
%doc COPYING COPYING.LIB
%{mingw32_bindir}/dumpsexp.exe
%{mingw32_bindir}/hmac256.exe
%{mingw32_bindir}/mpicalc.exe
%{mingw32_bindir}/libgcrypt-20.dll
%{mingw32_bindir}/libgcrypt-config
%{mingw32_libdir}/libgcrypt.dll.a
%{mingw32_libdir}/pkgconfig/libgcrypt.pc
%{mingw32_includedir}/gcrypt.h
%{mingw32_datadir}/aclocal/libgcrypt.m4

%files -n mingw32-libgcrypt-static
%{mingw32_libdir}/libgcrypt.a

%files -n mingw64-libgcrypt
%doc COPYING COPYING.LIB
%{mingw64_bindir}/dumpsexp.exe
%{mingw64_bindir}/hmac256.exe
%{mingw64_bindir}/mpicalc.exe
%{mingw64_bindir}/libgcrypt-20.dll
%{mingw64_bindir}/libgcrypt-config
%{mingw64_libdir}/libgcrypt.dll.a
%{mingw64_libdir}/pkgconfig/libgcrypt.pc
%{mingw64_includedir}/gcrypt.h
%{mingw64_datadir}/aclocal/libgcrypt.m4

%files -n mingw64-libgcrypt-static
%{mingw64_libdir}/libgcrypt.a

%changelog
%autochangelog

%global source1_hash 8be53f19f43ffa0297aceb520be717de539d1bdad45b5538a57fd95610b1e2db
%global source0_hash d77f68f48879510e79a2f65977ccc68981781ea0923e5bdffac2a193ea3d660e
%?mingw_package_header
%global run_tests 0
Name:           mingw-libgcrypt
Version:        1.12.4
Release:        1%{?dist}
Summary:        MinGW Windows gcrypt encryption library
License:        LicenseRef-Callaway-LGPLv2+ AND GPL-2.0-or-later
URL:            ftp://ftp.gnupg.org/gcrypt/libgcrypt/
Source0:        https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2
Source1: https://www.gnupg.org/ftp/gcrypt/libgcrypt/libgcrypt-%{version}.tar.bz2.sig
Source2: wk@g10code.com
Patch1: libgcrypt-1.10.1-annobin.patch
Patch1000:      libgcrypt-use-correct-def-file.patch
BuildArch:      noarch
%if %run_tests
%endif
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-dlfcn
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libgpg-error
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-dlfcn
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libgpg-error
# /oreon:deps
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
make -C build_win32/tests check ||:
pushd build_win32/src/.libs
for t in $(pwd)/../../tests/*.exe; do
  wine $t
done
popd
%endif
%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir}
rm -rf $RPM_BUILD_ROOT%{mingw64_infodir}
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}
rm $RPM_BUILD_ROOT%{mingw32_libdir}/libgcrypt.def
rm $RPM_BUILD_ROOT%{mingw64_libdir}/libgcrypt.def
rm $RPM_BUILD_ROOT%{mingw32_libdir}/libgcrypt.la
rm $RPM_BUILD_ROOT%{mingw64_libdir}/libgcrypt.la
%oreon_autofiles mingw32-libgcrypt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libgcrypt-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgcrypt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgcrypt-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libgcrypt -f %{oreon_filedir}/mingw32-libgcrypt.list
%files -n mingw32-libgcrypt-static -f %{oreon_filedir}/mingw32-libgcrypt-static.list
%files -n mingw64-libgcrypt -f %{oreon_filedir}/mingw64-libgcrypt.list
%files -n mingw64-libgcrypt-static -f %{oreon_filedir}/mingw64-libgcrypt-static.list

%changelog

%autochangelog

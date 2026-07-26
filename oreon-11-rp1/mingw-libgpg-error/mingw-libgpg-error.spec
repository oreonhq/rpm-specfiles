%global source0_hash 95b178148863f07d45df0cea67e880a79b9ef71f5d230baddc0071128516ef78

%?mingw_package_header

Name:           mingw-libgpg-error
Version:        1.55
Release:        2%{?dist}
Summary:        MinGW Windows GnuPGP error library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            ftp://ftp.gnupg.org/gcrypt/libgpg-error/
Source0:        ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2
Source1:        ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2.sig
BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-gettext

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-gettext

BuildRequires:  gettext

# See comment in %%prep for details
BuildRequires:  libtool autoconf automake gettext-devel

%description
MinGW Windows GnuPGP error library.

%package -n mingw32-libgpg-error
Summary:        MinGW Windows libgpg-error compression library for the win32 target

%description -n mingw32-libgpg-error
MinGW Windows GnuPGP error library.

%package -n mingw32-libgpg-error-static
Summary:        Static library for mingw32-libgpg-error development
Requires:       mingw32-libgpg-error = %{version}-%{release}

%description -n mingw32-libgpg-error-static
Static library for mingw32-libgpg-error development.

%package -n mingw64-libgpg-error
Summary:        MinGW Windows libgpg-error compression library for the win64 target

%description -n mingw64-libgpg-error
MinGW Windows GnuPGP error library.

%package -n mingw64-libgpg-error-static
Summary:        Static library for mingw64-libgpg-error development
Requires:       mingw64-libgpg-error = %{version}-%{release}

%description -n mingw64-libgpg-error-static
Static library for mingw64-libgpg-error development.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libgpg-error-%{version}

# Upstream has applied a libtool hack in libgpg-error 1.12
# which automatically gives the libgpg-error library a
# different filename for the win64 target so that
# the libgpg-error DLL's for both the win32 and win64
# targets can be installed in the same folder.
#
# As installing both win32 and win64 libraries in the same
# folder is bad practice and breaks earlier behavior undo
# this libtool hack here by re-running libtoolize
autoreconf -i --force

%build
%mingw_configure --enable-shared --enable-static
%mingw_make %{?_smp_mflags}

%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Drop info and man pages as they're already provided by the native package
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir} $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_infodir} $RPM_BUILD_ROOT%{mingw64_mandir}

%mingw_find_lang libgpg-error

%files -n mingw32-libgpg-error -f mingw32-libgpg-error.lang
%{mingw32_bindir}/gpgrt-config
%{mingw32_bindir}/gpg-error.exe
%{mingw32_bindir}/yat2m.exe
%{mingw32_bindir}/libgpg-error-0.dll
%{mingw32_libdir}/libgpg-error.dll.a
%{mingw32_libdir}/pkgconfig/gpg-error.pc
%{mingw32_includedir}/gpg-error.h
%{mingw32_includedir}/gpgrt.h
%{mingw32_datadir}/aclocal/gpg-error.m4
%{mingw32_datadir}/aclocal/gpgrt.m4
%{mingw32_datadir}/common-lisp/source/gpg-error/*
%{mingw32_datadir}/libgpg-error

%files -n mingw32-libgpg-error-static
%{mingw32_libdir}/libgpg-error.a

%files -n mingw64-libgpg-error -f mingw64-libgpg-error.lang
%{mingw64_bindir}/gpgrt-config
%{mingw64_bindir}/gpg-error.exe
%{mingw64_bindir}/yat2m.exe
%{mingw64_bindir}/libgpg-error-0.dll
%{mingw64_libdir}/libgpg-error.dll.a
%{mingw64_libdir}/pkgconfig/gpg-error.pc
%{mingw64_includedir}/gpg-error.h
%{mingw64_includedir}/gpgrt.h
%{mingw64_datadir}/aclocal/gpg-error.m4
%{mingw64_datadir}/aclocal/gpgrt.m4
%{mingw64_datadir}/common-lisp/source/gpg-error/*
%{mingw64_datadir}/libgpg-error

%files -n mingw64-libgpg-error-static
%{mingw64_libdir}/libgpg-error.a

%changelog
%autochangelog

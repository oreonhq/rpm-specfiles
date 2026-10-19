%global source1_hash 9b20f1e6046aaa3fe16fcd65587fd0fa5e34ceb4830f8eadc856c3e80ad57ad3
%global source0_hash 7a85413f2bc354f4f8aa832b718af122e48965e9e0eb9012ee659c13c6385c93
%?mingw_package_header
Name:           mingw-libgpg-error
Version:        1.61
Release:        1%{?dist}
Summary:        MinGW Windows GnuPGP error library
License:        LicenseRef-Callaway-LGPLv2+
URL:            ftp://ftp.gnupg.org/gcrypt/libgpg-error/
Source0:        https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2
Source1:        https://gnupg.org/ftp/gcrypt/libgpg-error/libgpg-error-%{version}.tar.bz2.sig
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
# /oreon:deps
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
find $RPM_BUILD_ROOT -name "*.la" -delete
rm -rf $RPM_BUILD_ROOT%{mingw32_infodir} $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_infodir} $RPM_BUILD_ROOT%{mingw64_mandir}
%mingw_find_lang libgpg-error
%oreon_autofiles mingw32-libgpg-error usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libgpg-error-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgpg-error usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgpg-error-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libgpg-error -f %{oreon_filedir}/mingw32-libgpg-error.list
%files -n mingw32-libgpg-error-static -f %{oreon_filedir}/mingw32-libgpg-error-static.list
%files -n mingw64-libgpg-error -f %{oreon_filedir}/mingw64-libgpg-error.list
%files -n mingw64-libgpg-error-static -f %{oreon_filedir}/mingw64-libgpg-error-static.list

%changelog

%autochangelog

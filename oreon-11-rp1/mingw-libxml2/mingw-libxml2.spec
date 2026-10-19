%global source0_hash 98087fd181d9070724f3fbc65c7377db03038eb92bd882374daff44940138821
%{?mingw_package_header}
Name:           mingw-libxml2
Version:        2.15.4
Release:        1%{?dist}
Summary:        MinGW Windows libxml2 XML processing library
License:        MIT
URL:            http://xmlsoft.org/
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Source0:        https://download.gnome.org/sources/libxml2/%{release_version}/libxml2-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
MinGW Windows libxml2 XML processing library.

# Win32
%package -n mingw32-libxml2
Summary:        MinGW Windows libxml2 XML processing library
Requires:       pkgconfig
%description -n mingw32-libxml2
MinGW Windows libxml2 XML processing library.

%package -n mingw32-libxml2-static
Summary:        Static version of the MinGW Windows XML processing library
Requires:       mingw32-libxml2 = %{version}-%{release}
%description -n mingw32-libxml2-static
Static version of the MinGW Windows XML processing library.

# Win64
%package -n mingw64-libxml2
Summary:        MinGW Windows libxml2 XML processing library
Requires:       pkgconfig
%description -n mingw64-libxml2
MinGW Windows libxml2 XML processing library.

%package -n mingw64-libxml2-static
Summary:        Static version of the MinGW Windows XML processing library
Requires:       mingw64-libxml2 = %{version}-%{release}
%description -n mingw64-libxml2-static
Static version of the MinGW Windows XML processing library.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libxml2-%{version}
%oreon_prep
%build

NOCONFIGURE=1 ./autogen.sh
MINGW32_CPPFLAGS="-DLIBXML_STATIC_FOR_DLL" \
MINGW64_CPPFLAGS="-DLIBXML_STATIC_FOR_DLL" \
MINGW_BUILDDIR_SUFFIX=static %mingw_configure --without-python --with-modules --enable-static --disable-shared --with-threads=win32
MINGW_BUILDDIR_SUFFIX=shared %mingw_configure --without-python --with-modules --disable-static --enable-shared --with-threads=win32
MINGW_BUILDDIR_SUFFIX=static %mingw_make_build
MINGW_BUILDDIR_SUFFIX=shared %mingw_make_build
%install
MINGW_BUILDDIR_SUFFIX=static %mingw_make_install
MINGW_BUILDDIR_SUFFIX=shared %mingw_make_install
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc/
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc/
find %{buildroot} -name "*.la" -delete
%oreon_autofiles mingw32-libxml2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libxml2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libxml2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libxml2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libxml2 -f %{oreon_filedir}/mingw32-libxml2.list
%files -n mingw32-libxml2-static -f %{oreon_filedir}/mingw32-libxml2-static.list
%files -n mingw64-libxml2 -f %{oreon_filedir}/mingw64-libxml2.list
%files -n mingw64-libxml2-static -f %{oreon_filedir}/mingw64-libxml2-static.list

%changelog

%autochangelog

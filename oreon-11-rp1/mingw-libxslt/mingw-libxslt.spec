%global source0_hash 8e00aa4e1749ee7244d08683ce2bb6fec7fd99baa6ef5d5f091274b318e6925e
%{?mingw_package_header}
Name:           mingw-libxslt
Version:        1.1.45
Release:        1%{?dist}
Summary:        MinGW Windows Library providing the Gnome XSLT engine
License:        MIT
URL:            https://gitlab.gnome.org/GNOME/libxslt
Source0:        https://gitlab.gnome.org/GNOME/libxslt/-/archive/v%{version}/libxslt-v%{version}.tar.bz2
Patch0:         gnome-libxslt-bug-139-apple-fix.patch
Patch1:         https://gitlab.gnome.org/GNOME/libxslt/-/commit/fe508f201efb9ea37bfbe95413b8b28251497de3.patch
Patch2:         https://gitlab.gnome.org/GNOME/libxslt/-/merge_requests/77.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libgcrypt
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libgcrypt
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-win-iconv
BuildRequires:  pkgconfig
# /oreon:deps
%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

# Win32
%package -n mingw32-libxslt
Summary:        MinGW Windows Library providing the Gnome XSLT engine
Requires:       mingw32-libxml2 >= 2.7.2-3
Requires:       pkgconfig
%description -n mingw32-libxslt
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package -n mingw32-libxslt-static
Summary:        Static version of the MinGW Windows LibXSLT library
Requires:       mingw32-libxslt = %{version}-%{release}
%description -n mingw32-libxslt-static
Static version of the MinGW Windows LibXSLT library.

# Win64
%package -n mingw64-libxslt
Summary:        MinGW Windows Library providing the Gnome XSLT engine
Requires:       mingw64-libxml2 >= 2.7.2-3
Requires:       pkgconfig
%description -n mingw64-libxslt
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package -n mingw64-libxslt-static
Summary:        Static version of the MinGW Windows LibXSLT library
Requires:       mingw64-libxslt = %{version}-%{release}
%description -n mingw64-libxslt-static
Static version of the MinGW Windows LibXSLT library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n libxslt-v%{version} -p1
NOCONFIGURE=1 ./autogen.sh

%build

%mingw_configure --without-python --enable-shared --enable-static
%mingw_make_build
%install
%mingw_make_install
rm -r %{buildroot}%{mingw32_datadir}/gtk-doc
rm -r %{buildroot}%{mingw32_docdir}
rm -r %{buildroot}%{mingw32_mandir}
rm -r %{buildroot}%{mingw64_datadir}/gtk-doc
rm -r %{buildroot}%{mingw64_docdir}
rm -r %{buildroot}%{mingw64_mandir}
find %{buildroot} -name "*.la" -delete
%oreon_autofiles mingw32-libxslt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libxslt-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libxslt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libxslt-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libxslt -f %{oreon_filedir}/mingw32-libxslt.list
%files -n mingw32-libxslt-static -f %{oreon_filedir}/mingw32-libxslt-static.list
%files -n mingw64-libxslt -f %{oreon_filedir}/mingw64-libxslt.list
%files -n mingw64-libxslt-static -f %{oreon_filedir}/mingw64-libxslt-static.list

%changelog

%autochangelog

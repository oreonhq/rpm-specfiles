%global source0_hash f138f964a8390c8aecc6c79dc18756989cc2d4db624b12f94a01a92ec57111ff
%{?mingw_package_header}
Name:           mingw-pango
Version:        1.90.0
Release:        1%{?dist}
Summary:        MinGW Windows Pango library
License:        LGPL-2.0-or-later
URL:            http://www.pango.org
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Source0:        http://download.gnome.org/sources/pango/%{release_version}/pango-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-fontconfig
BuildRequires:  mingw32-freetype
BuildRequires:  mingw32-fribidi
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-harfbuzz
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-pixman
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-fontconfig
BuildRequires:  mingw64-freetype
BuildRequires:  mingw64-fribidi
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-harfbuzz
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-win-iconv
BuildRequires:  pkgconfig
# /oreon:deps
%description
MinGW Windows Pango library.

# Win32
%package -n mingw32-pango
Summary:        MinGW Windows Pango library
Requires:       pkgconfig
%description -n mingw32-pango
MinGW Windows Pango library.

%package -n mingw32-pango-static
Summary:        Static version of the MinGW Windows Pango library
Requires:       mingw32-pango = %{version}-%{release}
%description -n mingw32-pango-static
Static version of the MinGW Windows Pango library.

# Win64
%package -n mingw64-pango
Summary:        MinGW Windows Pango library
Requires:       pkgconfig
%description -n mingw64-pango
MinGW Windows Pango library.

%package -n mingw64-pango-static
Summary:        Static version of the MinGW Windows Pango library
Requires:       mingw64-pango = %{version}-%{release}
%description -n mingw64-pango-static
Static version of the MinGW Windows Pango library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pango-%{version}
%oreon_prep
%build

%mingw_meson --default-library=both -Dintrospection=disabled -Dgtk_doc=false -Dfontconfig=enabled
%mingw_ninja
%install
%mingw_ninja_install
mkdir -p %{buildroot}%{mingw32_sysconfdir}/pango/
mkdir -p %{buildroot}%{mingw64_sysconfdir}/pango/
%oreon_autofiles mingw32-pango usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-pango-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-pango usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-pango-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-pango -f %{oreon_filedir}/mingw32-pango.list
%files -n mingw32-pango-static -f %{oreon_filedir}/mingw32-pango-static.list
%files -n mingw64-pango -f %{oreon_filedir}/mingw64-pango.list
%files -n mingw64-pango-static -f %{oreon_filedir}/mingw64-pango-static.list

%changelog

%autochangelog

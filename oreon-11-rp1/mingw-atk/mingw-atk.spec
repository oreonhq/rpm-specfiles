%global source0_hash ac4de2a4ef4bd5665052952fe169657e65e895c5057dffb3c2a810f6191a0c36
%{?mingw_package_header}
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-atk
Version:        2.38.0
Release:        1%{?dist}
Summary:        MinGW Windows Atk library
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://projects.gnome.org/accessibility/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/atk/%{release_version}/atk-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-win-iconv
BuildRequires:  pkgconfig
# /oreon:deps
%description
MinGW Windows Atk library.

# Win32
%package -n mingw32-atk
Summary:        MinGW Windows Atk library
Requires:       pkgconfig
%description -n mingw32-atk
MinGW Windows Atk library.

%package -n mingw32-atk-static
Summary:        Static version of the MinGW Windows Atk library
Requires:       mingw32-atk = %{version}-%{release}
%description -n mingw32-atk-static
Static version of the MinGW Windows Atk library.

# Win64
%package -n mingw64-atk
Summary:        MinGW Windows Atk library
Requires:       pkgconfig
%description -n mingw64-atk
MinGW Windows Atk library.

%package -n mingw64-atk-static
Summary:        Static version of the MinGW Windows Atk library
Requires:       mingw64-atk = %{version}-%{release}
%description -n mingw64-atk-static
Static version of the MinGW Windows Atk library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir atk-%{version}
%oreon_prep
%build

%mingw_meson --default-library=both -Dintrospection=false
%mingw_ninja
%install
%mingw_ninja_install
%mingw_find_lang atk10
%oreon_autofiles mingw32-atk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-atk-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-atk usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-atk-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-atk -f %{oreon_filedir}/mingw32-atk.list
%files -n mingw32-atk-static -f %{oreon_filedir}/mingw32-atk-static.list
%files -n mingw64-atk -f %{oreon_filedir}/mingw64-atk.list
%files -n mingw64-atk-static -f %{oreon_filedir}/mingw64-atk-static.list

%changelog

%autochangelog

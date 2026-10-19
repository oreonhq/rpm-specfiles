%global source0_hash 17d15cac2af80a33271127408e0abc2748eb297c595c2a26409e81e14e7d1b8f
%{?mingw_package_header}
Name:           mingw-glib2
Version:        2.90.0
Release:        1%{?dist}
Summary:        MinGW Windows GLib2 library
License:        LGPL-2.0-or-later
URL:            http://www.gtk.org
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Source0:        https://download.gnome.org/sources/glib/%{release_version}/glib-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gettext
BuildRequires:  mingw32-libffi
BuildRequires:  mingw32-pcre2
BuildRequires:  mingw32-win-iconv
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gettext
BuildRequires:  mingw64-libffi
BuildRequires:  mingw64-pcre2
BuildRequires:  mingw64-win-iconv
BuildRequires:  mingw64-zlib
BuildRequires:  python3-devel
# /oreon:deps
%description
MinGW Windows Glib2 library.

# Win32
%package -n mingw32-glib2
Summary:        MinGW Windows Glib2 library for the win32 target
Requires:       python3
%description -n mingw32-glib2
MinGW Windows Glib2 library.

%package -n mingw32-glib2-static
Summary:        Static version of the MinGW Windows GLib2 library
Requires:       mingw32-glib2 = %{version}-%{release}
Requires:       mingw32-gettext-static
%description -n mingw32-glib2-static
Static version of the MinGW Windows GLib2 library.

# Win64
%package -n mingw64-glib2
Summary:        MinGW Windows Glib2 library for the win64 target
Requires:       python3
%description -n mingw64-glib2
MinGW Windows Glib2 library.

%package -n mingw64-glib2-static
Summary:        Static version of the MinGW Windows GLib2 library
Requires:       mingw64-glib2 = %{version}-%{release}
Requires:       mingw64-gettext-static
%description -n mingw64-glib2-static
Static version of the MinGW Windows GLib2 library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir glib-%{version}
%oreon_prep
%build

export MINGW_BUILDDIR_SUFFIX=static
%mingw_meson --default-library=static
%mingw_ninja
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_meson --default-library=shared
%mingw_ninja
%install
export MINGW_BUILDDIR_SUFFIX=static
%mingw_ninja_install
export MINGW_BUILDDIR_SUFFIX=shared
%mingw_ninja_install
rm -f %{buildroot}/%{mingw32_libdir}/charset.alias
rm -f %{buildroot}/%{mingw64_libdir}/charset.alias
rm -rf %{buildroot}%{mingw32_datadir}/gdb
rm -rf %{buildroot}%{mingw64_datadir}/gdb
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw32_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw64_datadir}/gtk-doc
rm -rf %{buildroot}%{mingw32_datadir}/bash-completion
rm -rf %{buildroot}%{mingw64_datadir}/bash-completion
rm -f %{buildroot}%{mingw32_libdir}/*.def
rm -f %{buildroot}%{mingw64_libdir}/*.def
rm -f %{buildroot}%{mingw32_bindir}/gdbus-codegen
rm -rf %{buildroot}%{mingw32_libdir}/gdbus-2.0
sed -i 's|gdbus_codegen=.*|gdbus_codegen=%{_bindir}/gdbus-codegen|g' %{buildroot}%{mingw32_libdir}/pkgconfig/gio-2.0.pc
rm -f %{buildroot}%{mingw64_bindir}/gdbus-codegen
rm -rf %{buildroot}%{mingw64_libdir}/gdbus-2.0
sed -i 's|gdbus_codegen=.*|gdbus_codegen=%{_bindir}/gdbus-codegen|g' %{buildroot}%{mingw64_libdir}/pkgconfig/gio-2.0.pc
rm -rf %{buildroot}%{mingw32_libexecdir}/installed-tests/
rm -rf %{buildroot}%{mingw64_libexecdir}/installed-tests/
find %{buildroot} -name "*.la" -delete
%mingw_find_lang glib20
%py_byte_compile %{__python3} %{buildroot}%{mingw32_datadir}/glib-2.0/gdb
%py_byte_compile %{__python3} %{buildroot}%{mingw32_datadir}/glib-2.0/codegen
%py_byte_compile %{__python3} %{buildroot}%{mingw64_datadir}/glib-2.0/gdb
%py_byte_compile %{__python3} %{buildroot}%{mingw64_datadir}/glib-2.0/codegen
%oreon_autofiles mingw32-glib2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-glib2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-glib2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-glib2-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-glib2 -f %{oreon_filedir}/mingw32-glib2.list
%files -n mingw32-glib2-static -f %{oreon_filedir}/mingw32-glib2-static.list
%files -n mingw64-glib2 -f %{oreon_filedir}/mingw64-glib2.list
%files -n mingw64-glib2-static -f %{oreon_filedir}/mingw64-glib2-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.87.3-1
- Prepare for Oreon 11 (RP1)

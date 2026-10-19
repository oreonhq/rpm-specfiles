%global source0_hash 83e12c36a099a8a7019bf425e2c24af66eeb2ef5874251e694431a07d9805dae
%global with_mingw 0
Name: libgsf
Version: 1.14.60
Release:        1%{?dist}
Summary:        GNOME Structured File library
License: LGPL-2.1-only
URL:     https://gitlab.gnome.org/GNOME/libgsf/
Source0:        https://download.gnome.org/sources/%{name}/1.14/%{name}-%{version}.tar.xz
Obsoletes: libgsf-gnome < 1.14.22
Obsoletes: libgsf-python < 1.14.26
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  chrpath
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libxml2
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
A library for reading and writing structured files (e.g. MS OLE and Zip)

%package devel
Summary: Support files necessary to compile applications with libgsf
Requires: libgsf = %{version}-%{release}, glib2-devel, libxml2-devel
Requires: pkgconfig
Obsoletes: libgsf-gnome-devel < 1.14.22
%description devel
Libraries, headers, and support files necessary to compile applications using
libgsf.

%package -n mingw32-libgsf
Summary: MinGW GNOME Structured File library
BuildArch: noarch
%description -n mingw32-libgsf
A library for reading and writing structured files (e.g. MS OLE and Zip)

%package -n mingw64-libgsf
Summary: MinGW GNOME Structured File library
BuildArch: noarch
%description -n mingw64-libgsf
A library for reading and writing structured files (e.g. MS OLE and Zip)

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%global _configure ../configure
mkdir -p build/doc && pushd build
ln -s ../../doc/html doc # some day meson... libgsf!4
%configure --disable-gtk-doc --disable-static --enable-introspection=yes \
%if 0%{?flatpak}
--with-typelib_dir=%{_libdir}/girepository-1.0 --with-gir-dir=%{_datadir}/gir-1.0
%endif
%make_build
popd
%mingw_configure --disable-static
%mingw_make_build
%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
pushd build
%make_install
popd
%find_lang %{name}
%mingw_make_install
%mingw_debug_install_post
%mingw_find_lang %{name} --all-name
chrpath --delete %{buildroot}%{_bindir}/gsf*
find %{buildroot} -name '*.la' -delete -print
%ldconfig_scriptlets
%oreon_autofiles mingw32-libgsf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgsf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libgsf-devel -f %{oreon_filedir}/libgsf-devel.list
%files -n mingw32-libgsf -f %{oreon_filedir}/mingw32-libgsf.list
%files -n mingw64-libgsf -f %{oreon_filedir}/mingw64-libgsf.list

%changelog

%autochangelog

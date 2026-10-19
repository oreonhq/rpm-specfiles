%global source0_hash 2f0c9615577c4126909e251f9de0626c3ee7a152376c15b5544df10fc87e560b
%global with_mingw 0
Name:           gcab
Version:        1.6
Release:        10%{?dist}
Summary:        Cabinet file library and tool
License:        LGPL-2.1-or-later
URL:            http://ftp.gnome.org/pub/GNOME/sources/gcab
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gcab/%{version}/%{name}-%{version}.tar.xz
Requires:       libgcab1%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-zlib
BuildRequires:  vala
BuildRequires:  zlib-devel
# /oreon:deps
%description
gcab is a tool to manipulate Cabinet archive.

%package -n libgcab1
Summary:        Library to create Cabinet archives
%description -n libgcab1
libgcab is a library to manipulate Cabinet archive using GIO/GObject.

%package -n libgcab1-devel
Summary:        Development files to create Cabinet archives
Requires:       libgcab1%{?_isa} = %{version}-%{release}
Requires:       glib2-devel
Requires:       pkgconfig
%description -n libgcab1-devel
libgcab is a library to manipulate Cabinet archive.

Libraries, includes, etc. to compile with the gcab library.

%package -n mingw32-libgcab1
Summary: MinGW library to create Cabinet archive.
BuildArch: noarch
%description -n mingw32-libgcab1
libgcab is a library to manipulate Cabinet archive.

%package -n mingw64-libgcab1
Summary: MinGW library to create Cabinet archive.
BuildArch: noarch
%description -n mingw64-libgcab1
libgcab is a library to manipulate Cabinet archive.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%mingw_meson -Dintrospection=false -Ddocs=false
%mingw_ninja
%check

%meson_test
%install
%meson_install
%find_lang %{name}
%ldconfig_scriptlets -n libgcab1
%mingw_ninja_install
%mingw_debug_install_post
%mingw_find_lang %{name}
%oreon_autofiles libgcab1 usr/*/lib*.so.*
%oreon_autofiles libgcab1-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles mingw32-libgcab1 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgcab1 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libgcab1 -f %{oreon_filedir}/libgcab1.list
%files -n libgcab1-devel -f %{oreon_filedir}/libgcab1-devel.list
%files -n mingw32-libgcab1 -f %{oreon_filedir}/mingw32-libgcab1.list
%files -n mingw64-libgcab1 -f %{oreon_filedir}/mingw64-libgcab1.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6-10
- Prepare for Oreon 11 (RP1)

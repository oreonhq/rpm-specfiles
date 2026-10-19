%global source0_hash 9bfec346382416a3575d87299bc641b2a464aa519fd9b1287e318aa43a2f3b8b
%global with_mingw 0
%if 0%{?fedora} || (0%{?oreon} >= 11)
%global with_mingw 0%{!?_without_mingw:1}
%endif
Name: libvirt-glib
Version: 5.0.0
Release:        1%{?dist}
Summary:        libvirt glib integration for events
License: LGPL-2.1-or-later
URL: https://libvirt.org/
Source0:        https://libvirt.org/sources/glib/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libvirt-devel
BuildRequires:  libxml2-devel
BuildRequires:  meson
BuildRequires:  vala
# /oreon:deps
%package devel
Summary: libvirt glib integration for events development files
Requires: %{name} = %{version}-%{release}
%package -n libvirt-gconfig
Summary: libvirt object APIs for processing object configuration
%package -n libvirt-gobject
Summary: libvirt object APIs for managing virtualization hosts
Requires: %{name} = %{version}-%{release}
Requires: libvirt-gconfig = %{version}-%{release}
%package -n libvirt-gconfig-devel
Summary: libvirt object APIs for processing object configuration development files
Requires: libvirt-gconfig = %{version}-%{release}
%package -n libvirt-gobject-devel
Summary: libvirt object APIs for managing virtualization hosts development files
Requires: %{name}-devel = %{version}-%{release}
Requires: libvirt-gconfig-devel = %{version}-%{release}
Requires: libvirt-gobject = %{version}-%{release}
%description
This package provides integration between libvirt and the glib
event loop.

%description devel
This package provides development header files and libraries for
integration between libvirt and the glib event loop.

%description -n libvirt-gconfig
This package provides APIs for processing the object configuration
data

%description -n libvirt-gconfig-devel
This package provides development header files and libraries for
the object configuration APIs.

%description -n libvirt-gobject
This package provides APIs for managing virtualization host
objects

%description -n libvirt-gobject-devel
This package provides development header files and libraries for
managing virtualization host objects

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libvirt-glib-5.0.0
%oreon_prep
%build

%meson -Drpath=disabled
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles libvirt-gconfig usr/*/lib*.so.*
%oreon_autofiles libvirt-gobject usr/*/lib*.so.*
%oreon_autofiles libvirt-gconfig-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles libvirt-gobject-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libvirt-glib-devel -f %{oreon_filedir}/libvirt-glib-devel.list
%files -n libvirt-gconfig -f %{oreon_filedir}/libvirt-gconfig.list
%files -n libvirt-gobject -f %{oreon_filedir}/libvirt-gobject.list
%files -n libvirt-gconfig-devel -f %{oreon_filedir}/libvirt-gconfig-devel.list
%files -n libvirt-gobject-devel -f %{oreon_filedir}/libvirt-gobject-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.0.0-8
- Import

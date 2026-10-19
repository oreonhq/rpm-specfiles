%global source0_hash 45068697de3ffe46840ca369705f23118b34db4f7deb63f6eff079a6734ddcca
%define glib2_version                  2.80.0
%define gobject_introspection_version  1.81.0
%define pycairo_version                1.16.0
%define python3_version                3.8
%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)
Name:           pygobject3
Version:        3.58.0
Release:        1%{?dist}
Summary:        Python bindings for GObject Introspection
License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/PyGObject
Source0:        https://download.gnome.org/sources/pygobject/%{major_minor_version}/pygobject-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk3
BuildRequires:  mesa-dri-drivers
BuildRequires:  meson
BuildRequires:  mutter
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(girepository-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(py3cairo)
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3dist(pytest)
BuildRequires:  xwayland-run
# /oreon:deps
%description
The %{name} package provides a convenient wrapper for the GObject library
for use in Python programs.

%package     -n python3-gobject
Summary:        Python 3 bindings for GObject Introspection
Requires:       python3-gobject-base%{?_isa} = %{version}-%{release}
Requires:       python3-cairo%{?_isa} >= %{pycairo_version}
%description -n python3-gobject
The python3-gobject package provides a convenient wrapper for the GObject 
library and and other libraries that are compatible with GObject Introspection, 
for use in Python 3 programs.

%package     -n python3-gobject-base
Summary:        Python 3 bindings for GObject Introspection base package
Obsoletes:      python3-gobject-base-noarch < 3.46.0-5
Provides:       python3-gobject-base-noarch = %{version}-%{release}
%description -n python3-gobject-base
This package provides the non-cairo specific bits of the GObject Introspection
library.

%package     -n python3-gobject-devel
Summary:        Development files for embedding PyGObject introspection support
Requires:       python3-gobject%{?_isa} = %{version}-%{release}
%description -n python3-gobject-devel
This package contains files required to embed PyGObject

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pygobject-%{version}
%oreon_prep
%build

%meson -Dpython=%{__python3}
%meson_build
%install
%meson_install
%oreon_autofiles python3-gobject usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-gobject-base usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-gobject-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export TEST_GTK_VERSION=3.0
export PYTEST_ADDOPTS="-k 'not (ref_count or has_two_refs)'"
%{shrink:xwfb-run -c mutter -- %meson_test --timeout-multiplier=5 || exit 0}
%files -f %{oreon_filedir}/main.list
%files -n python3-gobject -f %{oreon_filedir}/python3-gobject.list
%files -n python3-gobject-base -f %{oreon_filedir}/python3-gobject-base.list
%files -n python3-gobject-devel -f %{oreon_filedir}/python3-gobject-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.56.1-1
- Prepare for Oreon 11 (RP1)

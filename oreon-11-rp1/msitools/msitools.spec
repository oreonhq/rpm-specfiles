%global source0_hash 1ed34279cf8080f14f1b8f10e649474125492a089912e7ca70e59dfa2e5a659b
%if 0%{?oreon} >= 11
%bcond_without check 1
%endif
%define _version_suffix %{nil}
%if 0%{?oreon} >= 11 || 0%{?fedora} >= 44
%define with_validate 0
%elifarch x86_64
%define with_validate 1
%else
%define with_validate 0
%endif
Name:           msitools
Version:        0.106
Release:        1%{?dist}
Summary:        Windows Installer tools
License:        LGPL-2.1-or-later AND GPL-2.0-or-later AND MS-RL
URL:            https://download.gnome.org/sources/%{name}
Source0:        https://download.gnome.org/sources/%{name}/%{version}/%{name}-%{version}.tar.xz
Requires:       libgsf >= 1.14.24-2
%if %{with_validate}
%if %{undefined rhel} || (0%{?oreon} >= 11)
%endif
%endif
# oreon:deps
BuildRequires:  bison
BuildRequires:  gettext
BuildRequires:  git-core
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libgcab1-devel
BuildRequires:  libgsf-devel
BuildRequires:  meson
BuildRequires:  vala
# /oreon:deps
%description
msitools is a collection of utilities to inspect and create Windows
Installer files.  It is useful in a cross-compilation environment such
as fedora-mingw.

%package -n libmsi1
Summary:        A library to manipulate Windows .MSI files
License:        LGPL-2.1-or-later AND blessing
%description -n libmsi1
libmsi is a GObject library to work with Windows Installer files.  It is
a port from the MSI library of the Wine project.

%package -n libmsi1-devel
Summary:        A library to manipulate Windows .MSI files
License:        LGPL-2.1-or-later
Requires:       libmsi1%{?_isa} = %{version}-%{release}
%description -n libmsi1-devel
The libmsi1-devel package includes the header files for libmsi.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -S git_am -n msitools-%{version}%{?_version_suffix}

%build

%if %{with_validate}
%meson -Dvalidate-wxi=true
%else
%meson
%endif
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles libmsi1 usr/*/lib*.so.*
%oreon_autofiles libmsi1-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%ldconfig_scriptlets -n libmsi1
%files -f %{oreon_filedir}/main.list
%files -n libmsi1 -f %{oreon_filedir}/libmsi1.list
%files -n libmsi1-devel -f %{oreon_filedir}/libmsi1-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.106.58-1
- Import

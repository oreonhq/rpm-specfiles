%global source0_hash 742cd353a7b6f64285c444cf33242176c70c4d711b877bec15e1f4ed3e064f1a
Name: libqmi
Version: 1.38.0
Release:        1%{?dist}
Summary:        Support library to use the Qualcomm MSM Interface (QMI) protocol
License: LGPL-2.1-or-later
URL: https://gitlab.freedesktop.org/mobile-broadband/libqmi/
Source0:        https://gitlab.freedesktop.org/mobile-broadband/libqmi/-/archive/%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gi-docgen
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  help2man
BuildRequires:  libmbim-devel
BuildRequires:  libqrtr-glib-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  python3
# /oreon:deps
%description
This package contains the libraries that make it easier to use QMI functionality
from applications that use glib.

%package devel
Summary: Header files for adding QMI support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel%{?_isa}
Requires: pkgconfig
%description devel
This package contains the header and pkg-config files for development
applications using QMI functionality from applications that use glib.

%package utils
Summary: Utilities to use the QMI protocol from the command line
Requires: %{name}%{?_isa} = %{version}-%{release}
License: GPL-2.0-or-later
%description utils
This package contains the utilities that make it easier to use QMI functionality
from the command line.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dgtk_doc=true -Dbash_completion=false
%meson_build
%install
%meson_install
find %{buildroot}%{_datadir}/gtk-doc |xargs touch --reference meson.build
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
cp -a src/qmicli/qmicli %{buildroot}%{_datadir}/bash-completion/completions/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%meson_test
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libqmi-devel -f %{oreon_filedir}/libqmi-devel.list
%files -n libqmi-utils -f %{oreon_filedir}/libqmi-utils.list

%changelog

%autochangelog

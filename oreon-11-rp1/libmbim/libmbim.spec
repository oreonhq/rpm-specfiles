%global source0_hash 2671244f03325bf6633a69ae8931be223c32e08beac6b2e147b4b768fe5e4684
Name: libmbim
Version: 1.34.0
Release:        1%{?dist}
Summary:        Support library for the Mobile Broadband Interface Model protocol
License: LGPL-2.1-or-later
URL: https://gitlab.freedesktop.org/mobile-broadband/libmbim/
Source0:        https://gitlab.freedesktop.org/mobile-broadband/libmbim/-/archive/%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  help2man
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3
# /oreon:deps
%description
This package contains the libraries that make it easier to use MBIM
functionality from applications that use glib.

%package devel
Summary: Header files for adding MBIM support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel%{?_isa}
Requires: pkgconfig
%description devel
This package contains the header and pkg-config files for developing
applications using MBIM functionality from applications that use glib.

%package utils
Summary: Utilities to use the MBIM protocol from the command line
Requires: %{name}%{?_isa} = %{version}-%{release}
License: GPL-2.0-or-later
%description utils
This package contains the utilities that make it easier to use MBIM
functionality from the command line.

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
cp -a src/mbimcli/mbimcli %{buildroot}%{_datadir}/bash-completion/completions/
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%check

%meson_test
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libmbim-devel -f %{oreon_filedir}/libmbim-devel.list
%files -n libmbim-utils -f %{oreon_filedir}/libmbim-utils.list

%changelog

%autochangelog

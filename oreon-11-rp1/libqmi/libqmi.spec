Name: libqmi
Version: 1.36.0
Release: 3%{?dist}
Summary: Support library to use the Qualcomm MSM Interface (QMI) protocol
License: LGPL-2.1-or-later
URL: https://gitlab.freedesktop.org/mobile-broadband/libqmi/
Source: https://gitlab.freedesktop.org/mobile-broadband/libqmi/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: meson >= 0.53
BuildRequires: gcc
BuildRequires: glib2-devel >= 2.56
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gudev-1.0) >= 147
BuildRequires: libmbim-devel >= 1.18.0
BuildRequires: libqrtr-glib-devel
BuildRequires: python3
BuildRequires: help2man

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
%autosetup -p1


%build
# Let's avoid BuildRequiring bash-completion because it changes behavior
# of shell, at least until the .pc file gets into the -devel subpackage.
# We'll just install the bash-completion file ourselves.
%meson -Dgtk_doc=true -Dbash_completion=false
%meson_build


%install
%meson_install
find %{buildroot}%{_datadir}/gtk-doc |xargs touch --reference meson.build
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
cp -a src/qmicli/qmicli %{buildroot}%{_datadir}/bash-completion/completions/


%check
%meson_test


%ldconfig_scriptlets


%files
%license COPYING.LIB
%doc NEWS AUTHORS README.md
%{_libdir}/libqmi-glib.so.*
%{_libdir}/girepository-1.0/Qmi-1.0.typelib


%files devel
%{_includedir}/libqmi-glib/
%{_libdir}/pkgconfig/qmi-glib.pc
%{_libdir}/libqmi-glib.so
%{_datadir}/gtk-doc/html/libqmi-glib/
%{_datadir}/gir-1.0/Qmi-1.0.gir


%files utils
%license COPYING
%{_bindir}/qmicli
%{_bindir}/qmi-network
%{_bindir}/qmi-firmware-update
%{_datadir}/bash-completion
%{_libexecdir}/qmi-proxy
%{_mandir}/man1/*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.36.0-3
- Prepare for Oreon 11 (RP1)

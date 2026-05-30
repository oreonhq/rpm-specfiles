%global source0_hash 69ec8883d887a426c6402440b200fa53c41e9da8e098333369f2388d3559e856

Name: libqrtr-glib
Version: 1.2.2
Release: 9%{?dist}
Summary: Support library to use and manage the QRTR (Qualcomm IPC Router) bus.
License: LGPL-2.1-or-later
URL: https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib
Source:        https://gitlab.freedesktop.org/mobile-broadband/libqrtr-glib/-/archive/%{version}/%{name}-%{version}.tar.bz2

BuildRequires: meson >= 0.53
BuildRequires: gcc
BuildRequires: glib2-devel >= 2.56
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gudev-1.0) >= 147
BuildRequires: python3

%description
This package contains the libraries that make it easier to use and
manage the QRTR (Qualcomm IPC Router) bus.


%package devel
Summary: Header files for adding QRTR support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel

%description devel
This package contains the header and pkg-config files for development
applications using QRTR functionality from applications that use glib.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install
find %{buildroot}%{_datadir}/gtk-doc |xargs touch --reference meson.build


%check
%meson_test


%ldconfig_scriptlets


%files
%license LICENSES/LGPL-2.1-or-later.txt
%doc NEWS AUTHORS README.md
%{_libdir}/libqrtr-glib.so.*
%{_libdir}/girepository-1.0/Qrtr-1.0.typelib


%files devel
%{_includedir}/libqrtr-glib/
%{_libdir}/libqrtr-glib.so
%{_libdir}/pkgconfig/qrtr-glib.pc
%{_datadir}/gtk-doc/html/libqrtr-glib/
%{_datadir}/gir-1.0/Qrtr-1.0.gir


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.2-9
- Prepare for Oreon 11 (RP1)

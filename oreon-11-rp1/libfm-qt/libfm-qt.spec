%global source0_hash df0ce97dbf1dc71fe440d5cec896fcd355d66d38e5fb19411d5d1efb28fd40ad

Name:          libfm-qt
Version:       2.3.1
Release:       2%{?dist}
Summary:       Companion library for PCManFM
License:       GPL-2.0-or-later
URL:           https://lxqt-project.org
Source0:       https://github.com/lxqt/libfm-qt/archive/%{version}/libfm-qt-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(lxqt2-build-tools)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(libfm)
BuildRequires: pkgconfig(lxqt)
BuildRequires: pkgconfig(libmenu-cache)
BuildRequires: pkgconfig(libexif)
BuildRequires: lxqt-menu-data
BuildRequires: perl

BuildRequires: qt6-qtbase-private-devel

BuildRequires: menu-cache-devel

%description
Libfm-Qt is a companion library providing components to build
desktop file managers.

%package devel
Summary: Development files for libfm-qt
Requires: libfm-qt%{?_isa} = %{version}-%{release}
Requires: menu-cache-devel
Requires: qt6-qtbase-private-devel

%description devel
libfm-qt-devel package contains libraries and header files for
developing applications that use libfm-qt.

%package l10n
BuildArch:      noarch
Summary:        Translations for libfm-qt
Requires:       libfm-qt
%description l10n
This package provides translations for the libfm-qt package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install
%find_lang libfm-qt --with-qt

%files
%doc AUTHORS CHANGELOG README.md
%license LICENSE
%{_libdir}/libfm-qt6.so.17
%{_libdir}/libfm-qt6.so.17.*
%{_datadir}/libfm-qt6

%files devel
%{_libdir}/libfm-qt6.so
%{_libdir}/pkgconfig/libfm-qt6.pc
%{_includedir}/libfm-qt6/
%dir %{_datadir}/cmake/fm-qt6
%{_datadir}/cmake/fm-qt6/*
%{_datadir}/libfm-qt6/archivers.list
%{_datadir}/libfm-qt6/terminals.list
%{_datadir}/mime/packages/libfm-qt6-mimetypes.xml

%files l10n -f libfm-qt.lang
%doc AUTHORS CHANGELOG README.md
%license LICENSE
%dir %{_datadir}/libfm-qt6/translations

%changelog
%autochangelog

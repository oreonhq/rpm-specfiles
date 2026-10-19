%global source0_hash df0ce97dbf1dc71fe440d5cec896fcd355d66d38e5fb19411d5d1efb28fd40ad
Name:          libfm-qt
Version:       2.3.1
Release:        1%{?dist}
Summary:        Companion library for PCManFM
License:       GPL-2.0-or-later
URL:           https://lxqt-project.org
Source0:        https://github.com/lxqt/libfm-qt/archive/%{version}/libfm-qt-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  gcc-c++
BuildRequires:  lxqt-menu-data
BuildRequires:  menu-cache-devel
BuildRequires:  perl
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libfm)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
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
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%find_lang libfm-qt --with-qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libfm-qt-devel -f %{oreon_filedir}/libfm-qt-devel.list
%files -n libfm-qt-l10n -f %{oreon_filedir}/libfm-qt-l10n.list

%changelog

%autochangelog

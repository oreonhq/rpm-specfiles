# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 31e72bea959f9093bbc41023ab67f9d23bcf62c1f557064caa48b4c2f7709917
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global qt_module qtx11extras

Summary: Qt5 - X11 support library
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin 5.15
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
The X11 Extras module provides features specific to platforms using X11, e.g.
Linux and UNIX-like systems including embedded Linux systems that use the X
Window System.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%prep
%oreon_sha256
%autosetup -n %{qt_module}-everywhere-src-%{version}

%build
%{qmake_qt5}

%make_build

%install
make install INSTALL_ROOT=%{buildroot}

pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

%ldconfig_scriptlets

%files
%license LICENSE.GPL3-EXCEPT LICENSE.LGPL* LICENSE.GPL*
%{_qt5_libdir}/libQt5X11Extras.so.5*

%files devel
%{_qt5_headerdir}/QtX11Extras/
%{_qt5_libdir}/libQt5X11Extras.so
%{_qt5_libdir}/libQt5X11Extras.prl
%dir %{_qt5_libdir}/cmake/Qt5X11Extras/
%{_qt5_libdir}/cmake/Qt5X11Extras/Qt5X11ExtrasConfig*.cmake
%{_qt5_libdir}/pkgconfig/Qt5X11Extras.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_x11extras*.pri

%changelog
%autochangelog

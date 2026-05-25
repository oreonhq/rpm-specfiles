%global qt_module qtx11extras

Summary: Qt5 - X11 support library
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

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
%autosetup -n %{qt_module}-everywhere-src-%{version}


%build
%{qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import

%global qt_module qtconnectivity

Summary: Qt5 - Connectivity components
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

## upstream patches
## repo: https://invent.kde.org/qt/qt/qtconnectivity
## branch: kde/5.15
## git format-patch v5.15.18-lts-lgpl
Patch1:  0001-QLowEnergyControllerPrivateBluez-guard-against-malfo.patch

Patch100: %{name}-gcc11.patch

# filter qml provides
%global __provides_exclude_from ^%{_qt5_archdatadir}/qml/.*\\.so$

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel >= %{version}
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel >= %{version}
BuildRequires: pkgconfig(bluez)

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
%{qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

%if 0%{?docs}
make install_docs INSTALL_ROOT=%{buildroot}
%endif

# hardlink files to {_bindir}, add -qt5 postfix to not conflict
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt5_bindir}
for i in * ; do
  case "${i}" in
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

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
%license LICENSE.GPL* LICENSE.LGPL*
%{_bindir}/sdpscanner
%{_qt5_bindir}/sdpscanner
%{_qt5_libdir}/libQt5Bluetooth.so.5*
%{_qt5_archdatadir}/qml/QtBluetooth/
%{_qt5_libdir}/libQt5Nfc.so.5*
%{_qt5_archdatadir}/qml/QtNfc/

%files devel
%{_qt5_headerdir}/QtBluetooth/
%{_qt5_libdir}/libQt5Bluetooth.so
%{_qt5_libdir}/libQt5Bluetooth.prl
%dir %{_qt5_libdir}/cmake/Qt5Bluetooth/
%{_qt5_libdir}/cmake/Qt5Bluetooth/Qt5BluetoothConfig*.cmake
%{_qt5_libdir}/pkgconfig/Qt5Bluetooth.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_bluetooth*.pri
%{_qt5_headerdir}/QtNfc/
%{_qt5_libdir}/libQt5Nfc.so
%{_qt5_libdir}/libQt5Nfc.prl
%dir %{_qt5_libdir}/cmake/Qt5Nfc/
%{_qt5_libdir}/cmake/Qt5Nfc/Qt5NfcConfig*.cmake
%{_qt5_libdir}/pkgconfig/Qt5Nfc.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_nfc*.pri

%files examples
%{_qt5_examplesdir}/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import

%global qt_module qtquickcontrols2

Name:    qt5-%{qt_module}
Summary: Qt5 - module with set of QtQuick controls for embedded
Version: 5.15.18
Release: 2%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

Patch1:  0001-Unset-mouseGrabberPopup-if-it-s-removed-from-childre.patch
Patch2:  0002-Ensure-we-don-t-crash-when-changing-sizes-after-clea.patch
Patch3:  0003-implement-a11y-pressing-of-qquickabstractbutton.patch
Patch4:  0004-Fix-the-popup-position-of-a-Menu.patch
Patch5:  0005-Accessibility-respect-value-in-attached-Accessible-i.patch

# filter qml provides
%global __provides_exclude_from ^%{_qt5_archdatadir}/qml/.*\\.so$

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
#libQt53DRender.so.5(Qt_5_PRIVATE_API)(64bit)
#libQt5Core.so.5(Qt_5_PRIVATE_API)(64bit)
#libQt5Gui.so.5(Qt_5_PRIVATE_API)(64bit)
#libQt5Qml.so.5(Qt_5_PRIVATE_API)(64bit)
#libQt5Quick.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel

Requires: qt5-qtdeclarative%{?_isa} >= %{version}
Requires: qt5-qtgraphicaleffects%{_isa} >= %{version}

%description
The Qt Labs Controls module provides a set of controls that can be used to
build complete interfaces in Qt Quick.

Unlike Qt Quick Controls, these controls are optimized for embedded systems
and so are preferred for hardware with limited resources.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
Requires: qt5-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary:        Examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%autosetup -p1 -n %{qt_module}-everywhere-src-%{version}

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

# Remove .la leftovers
rm -f %{buildroot}%{_qt5_libdir}/libQt5*.la


%ldconfig_scriptlets

%files
%license LICENSE.LGPLv3 LICENSE.GPLv3
%{_qt5_libdir}/libQt5QuickTemplates2.so.5*
%{_qt5_libdir}/libQt5QuickControls2.so.5*
%{_qt5_qmldir}/Qt/labs/calendar
%{_qt5_qmldir}/Qt/labs/platform
%{_qt5_archdatadir}/qml/QtQuick/Controls.2/
%{_qt5_archdatadir}/qml/QtQuick/Templates.2/

%files examples
%{_qt5_examplesdir}/quickcontrols2/

%files devel
%{_qt5_headerdir}/
%{_qt5_libdir}/pkgconfig/*.pc
%{_qt5_libdir}/libQt5QuickTemplates2.so
%{_qt5_libdir}/libQt5QuickControls2.so
%{_qt5_libdir}/libQt5QuickTemplates2.prl
%{_qt5_libdir}/libQt5QuickControls2.prl
%{_qt5_libdir}/qt5/mkspecs/modules/*
%{_libdir}/cmake/Qt5QuickControls2/
%{_libdir}/cmake/Qt5QuickTemplates2/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import

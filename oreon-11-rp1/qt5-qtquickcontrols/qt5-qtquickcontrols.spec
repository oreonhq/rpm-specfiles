%global qt_module qtquickcontrols

Name:    qt5-%{qt_module}
Summary: Qt5 - module with set of QtQuick controls
Version: 5.15.18
Release: 2%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

# filter qml provides
%global __provides_exclude_from ^%{_qt5_archdatadir}/qml/.*\\.so$

BuildRequires: make
BuildRequires:  qt5-qtbase-devel >= %{version}
BuildRequires:  qt5-qtbase-static >= %{version}
BuildRequires:  qt5-qtbase-private-devel
#libQt5Gui.so.5(Qt_5_PRIVATE_API)(64bit)
#libQt5Qml.so.5(Qt_5_PRIVATE_API)(64bit)
#libQt5Quick.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires:  qt5-qtdeclarative-devel

%description
The Qt Quick Controls module provides a set of controls that can be used to
build complete interfaces in Qt Quick.

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


%files
%license LICENSE.*
%{_qt5_archdatadir}/qml/QtQuick/

%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Prepare for Oreon 11 (RP1)

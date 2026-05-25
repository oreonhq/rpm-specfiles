%global qt_module qtserialbus

Summary: Qt5 - SerialBus component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

## upstreamable patches
# workaround FTBFS against kernel-header-5.2.0+
Patch100: qtserialbus-everywhere-src-5.12.3-SIOCGSTAMP.patch

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
#libQt5Core.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtserialport-devel >= %{version}

%description
Qt Serial Bus (API) provides classes and functions to access the various
industrial serial buses and protocols, such as CAN, ModBus, and others.

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
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} .. \
  %{?_qt5_examplesdir:CONFIG+=qt_example_installs}

%make_build


%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}


%ldconfig_scriptlets

%files
%license LICENSE.*
%{_qt5_libdir}/libQt5SerialBus.so.5*
%{_qt5_bindir}/canbusutil
%{_qt5_plugindir}/canbus

%files devel
%{_qt5_headerdir}/QtSerialBus/
%{_qt5_libdir}/libQt5SerialBus.so
%{_qt5_libdir}/libQt5SerialBus.prl
%dir %{_qt5_libdir}/cmake/Qt5SerialBus/
%{_qt5_libdir}/cmake/Qt5SerialBus
%{_qt5_libdir}/pkgconfig/Qt5SerialBus.pc
%{_qt5_archdatadir}/mkspecs/modules/*
%exclude %{_qt5_libdir}/libQt5SerialBus.la

# no examples, yet
%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import

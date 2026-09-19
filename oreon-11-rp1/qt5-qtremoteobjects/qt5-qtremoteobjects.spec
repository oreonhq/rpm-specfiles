%global source0_hash 66b41538740a517973219d882d1ddf7288f3fdcbd5919205d86f539c2fb6b2f6

%global qt_module qtremoteobjects

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Summary: Qt5 - Qt Remote Objects
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
#libQt5Core.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel

%description
Qt Remote Objects (QtRO) is an inter-process communication (IPC) module developed for Qt.

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{qt_module}-everywhere-src-%{version}

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
%{_qt5_libdir}/libQt5RemoteObjects.so.5*
%{_qt5_bindir}/repc
## split out? -- rex
%{_qt5_qmldir}/QtQml/RemoteObjects/
%{_qt5_qmldir}/QtRemoteObjects/

%files devel
%{_qt5_headerdir}/QtRemoteObjects/
%{_qt5_headerdir}/QtRepParser/
%{_qt5_libdir}/libQt5RemoteObjects.so
%{_qt5_libdir}/libQt5RemoteObjects.prl
%{_qt5_libdir}/cmake/Qt5RemoteObjects/
%{_qt5_libdir}/cmake/Qt5RepParser
%{_qt5_libdir}/pkgconfig/Qt5RemoteObjects.pc
%{_qt5_archdatadir}/mkspecs/features/*
%{_qt5_archdatadir}/mkspecs/modules/*
%exclude %{_qt5_libdir}/libQt5RemoteObjects.la
%{_qt5_libdir}/Qt5RepParser.la
%{_qt5_libdir}/libQt5RepParser.prl
%{_qt5_libdir}/pkgconfig/Qt5RepParser.pc
%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif

%changelog
%autochangelog

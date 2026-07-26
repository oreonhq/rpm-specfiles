%global source0_hash 56058a3d1f8e30e675aa62775e7fd4234b4de6b1a76e2759be13b3509e160010

%global qt_module qtdatavis3d

Summary: Qt5 - Qt Data Visualization component
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
BuildRequires: qt5-qtdeclarative-devel >= %{version}

%description
Qt Data Visualization module provides multiple graph types to visualize data in
3D space both with C++ and Qt Quick 2.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
Requires: qt5-qtdeclarative-devel%{?_isa}
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
%{qmake_qt5} ..
popd

%make_build -C %{_target_platform}

%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}
%if 0%{?flatpak}
# qtbase is part of runtime in /usr, this is built in /app
mv %{buildroot}/usr %{buildroot}%{_prefix}
sed -i -e "\|^libdir=|s|/usr/%{_lib}|%{_libdir}|" %{buildroot}%{_qt5_libdir}/*.la
sed -i -e "\|^prefix=|s|/usr|%{_prefix}|" %{buildroot}%{_qt5_libdir}/pkgconfig/*.pc
sed -i -e "\|^[^\#]|s|/usr|%{_prefix}|" %{buildroot}%{_qt5_libdir}/cmake/*/*.cmake
%endif

%ldconfig_scriptlets

%files
%license LICENSE.GPL3
%{_qt5_libdir}/libQt5DataVisualization.so.5*
%{_qt5_qmldir}/QtDataVisualization/

%files devel
%{_qt5_headerdir}/QtDataVisualization/
%{_qt5_libdir}/libQt5DataVisualization.so
%{_qt5_libdir}/libQt5DataVisualization.prl
%{_qt5_libdir}/pkgconfig/Qt5DataVisualization.pc
%{_qt5_libdir}/cmake/Qt5DataVisualization/
%{_qt5_archdatadir}/mkspecs/modules/*
%exclude %{_qt5_libdir}/libQt5DataVisualization.la

%if 0%{?_qt5_examplesdir:1}
# no examples, yet
%files examples
%{_qt5_examplesdir}/
%endif

%changelog
%autochangelog

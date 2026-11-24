# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 55bf570ec45a0d35c16137c389735053a181c2f68df2e733710fc5efe10d0c09
%global source1_hash 825118da352dcaf274581f3c314332732cac0767293b872f2d76808ec483dd28
%global source2_hash b7425a23ab3ddaa0d55f5081e2d11b9a40e89181ce68a96a25bbafeaa65b94db
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%if 0%{?fedora} < 32
%global metapackage 1
%endif

Name: qt5
Version: 5.15.18
Release: 1%{?dist}
Summary: Qt5 meta package
License: GPL-3.0-only
URL:     https://getfedora.org/
Source0: macros.qt5
Source1: macros.qt5-srpm
Source2: qmake-qt5.sh

Requires: qt5-qdbusviewer
Requires: qt5-qt3d
Requires: qt5-qtbase
Requires: qt5-qtbase-gui
Requires: qt5-qtbase-mysql
Requires: qt5-qtbase-postgresql
Requires: qt5-qtconnectivity
Requires: qt5-qtdeclarative
Requires: qt5-qtdoc
Requires: qt5-qtgraphicaleffects
Requires: qt5-qtimageformats
Requires: qt5-qtlocation
Requires: qt5-qtmultimedia
Requires: qt5-qtquickcontrols
Requires: qt5-qtquickcontrols2
Requires: qt5-qtscript
Requires: qt5-qtsensors
Requires: qt5-qtserialport
Requires: qt5-qtsvg
Requires: qt5-qttools
Requires: qt5-qtwayland
Requires: qt5-qtwebchannel
Requires: qt5-qtwebsockets
Requires: qt5-qtx11extras
Requires: qt5-qtxmlpatterns

%description
%{summary}.

%package devel
Summary: Qt5 meta devel package
Requires: qt5-rpm-macros
Requires: qt5-qttools-static
Requires: qt5-qtdeclarative-static
Requires: qt5-qtbase-static
Requires: qt5-designer
Requires: qt5-qdoc
Requires: qt5-qhelpgenerator
Requires: qt5-linguist
Requires: qt5-qt3d-devel
Requires: qt5-qtbase-devel
Requires: qt5-qtconnectivity-devel
Requires: qt5-qtdeclarative-devel
Requires: qt5-qtlocation-devel
Requires: qt5-qtmultimedia-devel
Requires: qt5-qtscript-devel
Requires: qt5-qtsensors-devel
Requires: qt5-qtserialport-devel
Requires: qt5-qtsvg-devel
Requires: qt5-qttools-devel
Requires: qt5-qtwayland-devel
Requires: qt5-qtwebchannel-devel
Requires: qt5-qtwebsockets-devel
Requires: qt5-qtx11extras-devel
Requires: qt5-qtxmlpatterns-devel

%description devel
%{summary}.

%package rpm-macros
Summary: RPM macros for building Qt5 and KDE Frameworks 5 packages
Conflicts: qt5-qtbase-devel < 5.6.0-0.23
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires: cmake >= 3
%endif
%if 0%{?rhel} && 0%{?rhel} < 8
Requires: cmake3
%endif
Requires: gcc-c++
BuildArch: noarch
%description rpm-macros
%{summary}.

%package srpm-macros
Summary: RPM macros for source Qt5 packages
BuildArch: noarch
%description srpm-macros
%{summary}.

%package filesystem
Summary: Filesystem for Qt 5 packages
%description filesystem
Filesystem for Qt 5 packages.

%install
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/bin
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/cmake
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/examples
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/imports
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/metatypes
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/modules
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/libexec
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/mkspecs
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/plugins
mkdir -p %{buildroot}%{_prefix}/{lib,%{_lib}}/qt5/qml
mkdir -p %{buildroot}%{_datadir}/qt5
mkdir -p %{buildroot}%{_docdir}/qt5
mkdir -p %{buildroot}%{_includedir}/qt5
mkdir -p %{buildroot}%{_datadir}/qt5/translations

install -Dpm644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.qt5
install -Dpm644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/macros.d/macros.qt5-srpm
install -Dpm755 %{SOURCE2} %{buildroot}%{_bindir}/qmake-qt5.sh
mkdir -p %{buildroot}%{_datadir}/qt5/wrappers
ln -s %{_bindir}/qmake-qt5.sh %{buildroot}%{_datadir}/qt5/wrappers/qmake-qt5
ln -s %{_bindir}/qmake-qt5.sh %{buildroot}%{_datadir}/qt5/wrappers/qmake

sed -i \
  -e "s|@@QT5_CFLAGS@@|%{?qt5_cflags}|g" \
  -e "s|@@QT5_CXXFLAGS@@|%{?qt5_cxxflags}|g" \
  -e "s|@@QT5_RPM_LD_FLAGS@@|%{?qt5_rpm_ld_flags}|g" \
  -e "s|@@QT5_RPM_OPT_FLAGS@@|%{?qt5_rpm_opt_flags}|g" \
  -e "s|@@QMAKE@@|%{_prefix}/%%{_lib}/qt5/bin/qmake|g" \
  -e "s|@@QMAKE_QT5_WRAPPER@@|%{_bindir}/qmake-qt5.sh|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.qt5

%if 0%{?metapackage}
mkdir -p %{buildroot}%{_docdir}/qt5
mkdir -p %{buildroot}%{_docdir}/qt5-devel
echo "- Qt5 meta package" > %{buildroot}%{_docdir}/qt5/README
echo "- Qt5 devel meta package" > %{buildroot}%{_docdir}/qt5-devel/README

%files
%{_docdir}/qt5/README

%files devel
%{_docdir}/qt5-devel/README
%endif

%files rpm-macros
%{_rpmconfigdir}/macros.d/macros.qt5
%{_bindir}/qmake-qt5.sh
%{_datadir}/qt5/wrappers/

%files srpm-macros
%{_rpmconfigdir}/macros.d/macros.qt5-srpm

%files filesystem
%dir %{_prefix}/lib/qt5
%dir %{_prefix}/%{_lib}/qt5
%dir %{_prefix}/lib/qt5/bin
%dir %{_prefix}/%{_lib}/qt5/bin
%dir %{_prefix}/lib/qt5/cmake
%dir %{_prefix}/%{_lib}/qt5/cmake
%dir %{_prefix}/lib/qt5/examples
%dir %{_prefix}/%{_lib}/qt5/examples
%dir %{_prefix}/lib/qt5/imports
%dir %{_prefix}/%{_lib}/qt5/imports
%dir %{_prefix}/lib/qt5/metatypes
%dir %{_prefix}/%{_lib}/qt5/metatypes
%dir %{_prefix}/lib/qt5/modules
%dir %{_prefix}/%{_lib}/qt5/modules
%dir %{_prefix}/lib/qt5/libexec
%dir %{_prefix}/%{_lib}/qt5/libexec
%dir %{_prefix}/lib/qt5/mkspecs
%dir %{_prefix}/%{_lib}/qt5/mkspecs
%dir %{_prefix}/lib/qt5/plugins
%dir %{_prefix}/%{_lib}/qt5/plugins
%dir %{_prefix}/lib/qt5/qml
%dir %{_prefix}/%{_lib}/qt5/qml
%dir %{_datadir}/qt5
%dir %{_docdir}/qt5
%dir %{_includedir}/qt5
%dir %{_datadir}/qt5/translations

%changelog
%autochangelog

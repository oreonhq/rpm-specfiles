%global source0_hash none
Name: qt5
Version: 5.15.18
Release:        1%{?dist}
Summary:        Qt5 meta package
License: GPL-3.0-only
URL:     https://getfedora.org/
Source0:        macros.qt5
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
# oreon:deps

# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-devel -f %{oreon_filedir}/qt5-devel.list
%files -n qt5-rpm-macros -f %{oreon_filedir}/qt5-rpm-macros.list
%files -n qt5-srpm-macros -f %{oreon_filedir}/qt5-srpm-macros.list
%files -n qt5-filesystem -f %{oreon_filedir}/qt5-filesystem.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Prepare for Oreon 11 (RP1)
%endif

%global source0_hash 0a8aa74c7c5ba1011e79e9dff09bfb9442e0bea372c7035162c17de57a5abebc
Name: qt6
Version: 6.12.0
Release:        1%{?dist}
Summary:        Qt6 meta package
License: GPL-3.0-only
URL:     https://getfedora.org/
Source0:        macros.qt6
Source1: macros.qt6-srpm
Source2: qmake-qt6.sh
Source3: qt6qml.attr
Source4: qt6qml.prov
Requires: qt6-qt3d
Requires: qt6-qt5compat
Requires: qt6-qtbase
Requires: qt6-qtbase-gui
Requires: qt6-qtbase-mysql
Requires: qt6-qtbase-postgresql
Requires: qt6-qtcharts
Requires: qt6-qtconnectivity
Requires: qt6-qtdatavis3d
Requires: qt6-qtdeclarative
Requires: qt6-qtgraphs
Requires: qt6-qthttpserver
Requires: qt6-qtimageformats
Requires: qt6-qtlocation
Requires: qt6-qtmultimedia
Requires: qt6-qtnetworkauth
Requires: qt6-qtpositioning
Requires: qt6-qtquick3d
Requires: qt6-qtquicktimeline
Requires: qt6-qtremoteobjects
Requires: qt6-qtscxml
Requires: qt6-qtsensors
Requires: qt6-qtserialbus
Requires: qt6-qtserialport
Requires: qt6-qtshadertools
Requires: qt6-qtsvg
Requires: qt6-qttools
Requires: qt6-qtvirtualkeyboard
Requires: qt6-qtwayland
Requires: qt6-qtwebchannel
Requires: qt6-qtwebsockets
# oreon:deps

# /oreon:deps
%description
%{summary}.

%package devel
Summary: Qt6 meta devel package
Requires: qt6-designer
Requires: qt6-linguist
Requires: qt6-qt3d-devel
Requires: qt6-qt5compat-devel
Requires: qt6-qtbase-devel
Requires: qt6-qtbase-static
Requires: qt6-qtcharts-devel
Requires: qt6-qtconnectivity-devel
Requires: qt6-qtdatavis3d-devel
Requires: qt6-qtdeclarative-devel
Requires: qt6-qtdeclarative-static
Requires: qt6-qtgraphs-devel
Requires: qt6-qthttpserver-devel
Requires: qt6-qtlocation-devel
Requires: qt6-qtmultimedia-devel
Requires: qt6-qtnetworkauth-devel
Requires: qt6-qtpositioning-devel
Requires: qt6-qtquick3d-devel
Requires: qt6-qtquicktimeline-devel
Requires: qt6-qtremoteobjects-devel
Requires: qt6-qtscxml-devel
Requires: qt6-qtsensors-devel
Requires: qt6-qtserialbus-devel
Requires: qt6-qtserialport-devel
Requires: qt6-qtshadertools-devel
Requires: qt6-qtsvg-devel
Requires: qt6-qttools-devel
Requires: qt6-qttools-static
Requires: qt6-qtvirtualkeyboard-devel
Requires: qt6-qtwayland-devel
Requires: qt6-qtwebchannel-devel
Requires: qt6-qtwebsockets-devel
Requires: qt6-rpm-macros
%description devel
%{summary}.

%package rpm-macros
Summary: RPM macros for building Qt6 and KDE Frameworks 6 packages
Requires: cmake >= 3
Requires: gcc-c++
BuildArch: noarch
%description rpm-macros
%{summary}.

%package srpm-macros
Summary: RPM macros for source Qt6 packages
BuildArch: noarch
%description srpm-macros
%{summary}.

%package filesystem
Summary: Filesystem for Qt6 packages
%description filesystem
Filesystem for Qt 6 packages.

%install
mkdir -p %{buildroot}%{_prefix}/lib/qt6
mkdir -p %{buildroot}%{_prefix}/lib/qt6/bin
mkdir -p %{buildroot}%{_prefix}/lib/qt6/cmake
mkdir -p %{buildroot}%{_prefix}/lib/qt6/examples
mkdir -p %{buildroot}%{_prefix}/lib/qt6/imports
mkdir -p %{buildroot}%{_prefix}/lib/qt6/metatypes
mkdir -p %{buildroot}%{_prefix}/lib/qt6/modules
mkdir -p %{buildroot}%{_prefix}/lib/qt6/libexec
mkdir -p %{buildroot}%{_prefix}/lib/qt6/mkspecs
mkdir -p %{buildroot}%{_prefix}/lib/qt6/plugins
mkdir -p %{buildroot}%{_prefix}/lib/qt6/qml
%if "%{_lib}" != "lib"
mkdir -p %{buildroot}%{_prefix}/%{_lib}/qt6
mkdir -p %{buildroot}%{_prefix}/%{_lib}/qt6/bin
mkdir -p %{buildroot}%{_prefix}/%{_lib}/qt6/cmake
mkdir -p %{buildroot}%{_prefix}/%{_lib}/qt6/examples
mkdir -p %{buildroot}%{_prefix}/%{_lib}/qt6/imports
mkdir -p %{buildroot}%{_prefix}/%{_lib}/qt6/metatypes
mkdir -p %{buildroot}%{_prefix}/%{_lib}/qt6/modules
mkdir -p %{buildroot}%{_prefix}/%{_lib}/qt6/libexec
mkdir -p %{buildroot}%{_prefix}/%{_lib}/qt6/mkspecs
mkdir -p %{buildroot}%{_prefix}/%{_lib}/qt6/plugins
mkdir -p %{buildroot}%{_prefix}/%{_lib}/qt6/qml
%endif
mkdir -p %{buildroot}%{_datadir}/qt6
mkdir -p %{buildroot}%{_docdir}/qt6
mkdir -p %{buildroot}%{_includedir}/qt6
mkdir -p %{buildroot}%{_datadir}/qt6/translations
install -Dpm644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/macros.qt6
install -Dpm644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.qt6-srpm
install -Dpm755 %{SOURCE2} %{buildroot}%{_bindir}/qmake-qt6.sh
install -Dpm644 %{SOURCE3} %{buildroot}%{_fileattrsdir}/qt6qml.attr
install -Dpm755 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/qt6qml.prov
mkdir -p %{buildroot}%{_datadir}/qt6/wrappers
ln -s %{_bindir}/qmake-qt6.sh %{buildroot}%{_datadir}/qt6/wrappers/qmake-qt6
ln -s %{_bindir}/qmake-qt6.sh %{buildroot}%{_datadir}/qt6/wrappers/qmake
sed -i \
  -e "s|@@QT6_CFLAGS@@|%{?qt6_cflags}|g" \
  -e "s|@@QT6_CXXFLAGS@@|%{?qt6_cxxflags}|g" \
  -e "s|@@QT6_RPM_LD_FLAGS@@|%{?qt6_rpm_ld_flags}|g" \
  -e "s|@@QT6_RPM_OPT_FLAGS@@|%{?qt6_rpm_opt_flags}|g" \
  -e "s|@@QMAKE@@|%{_prefix}/%%{_lib}/qt6/bin/qmake|g" \
  -e "s|@@QMAKE_QT6_WRAPPER@@|%{_bindir}/qmake-qt6.sh|g" \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.qt6
%if 0%{?metapackage}
mkdir -p %{buildroot}%{_docdir}/qt6
mkdir -p %{buildroot}%{_docdir}/qt6-devel
echo "- Qt6 meta package" > %{buildroot}%{_docdir}/qt6/README
echo "- Qt6 devel meta package" > %{buildroot}%{_docdir}/qt6-devel/README
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt6-devel -f %{oreon_filedir}/qt6-devel.list
%files -n qt6-rpm-macros -f %{oreon_filedir}/qt6-rpm-macros.list
%files -n qt6-srpm-macros -f %{oreon_filedir}/qt6-srpm-macros.list
%files -n qt6-filesystem -f %{oreon_filedir}/qt6-filesystem.list

%changelog

%autochangelog
%endif

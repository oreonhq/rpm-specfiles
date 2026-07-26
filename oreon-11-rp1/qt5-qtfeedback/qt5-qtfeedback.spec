%global source0_hash e5ae4a7e570ce636d425277eb2094dfae102e6d11156f1d55db55eb2b2a49c16

%global qt_module qtfeedback

# Disable automatic .la file removal
%global __brp_remove_la_files %nil

Summary: Qt5 Tactile Feedback
Name:    qt5-qtfeedback
Version: 20180903gita14bd0b
Release: 13%{?dist}

License: GPL-2.0-or-later AND LGPL-3.0-only AND GFDL-1.3-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0 AND LGPL-2.1-only WITH Qt-LGPL-exception-1.1
Url:     https://code.qt.io/cgit/qt/qtfeedback.git/
Source0: %{qt_module}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: make

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtdeclarative-devel

%description
Qt5 tactile feedback libraries. This enables capabilities like vibrator feedback
for virtual keyboards.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{qt_module}-%{version} -p1
#  Taken from OpenSuse package (otherwise it fails to build)
touch .git # To make sure syncqt is used

%build
%{qmake_qt5} \
  CONFIG+=package multimedia_disabled=yes immersion_enabled=no meegotouchfeedback_enabled=no

%make_build

%install
make install INSTALL_ROOT=%{buildroot}
%if 0%{?flatpak}
# qtbase is part of runtime in /usr, this is built in /app
mv %{buildroot}/usr %{buildroot}%{_prefix}
sed -i -e "\|^libdir=|s|/usr/%{_lib}|%{_libdir}|" %{buildroot}%{_qt5_libdir}/*.la
sed -i -e "\|^prefix=|s|/usr|%{_prefix}|" %{buildroot}%{_qt5_libdir}/pkgconfig/*.pc
sed -i -e "\|^[^\#]|s|/usr|%{_prefix}|" %{buildroot}%{_qt5_libdir}/cmake/*/*.cmake
%endif

%ldconfig_scriptlets

%files
%license LICENSE* LGPL_EXCEPTION.txt
%{_qt5_libdir}/libQt5Feedback.so.*
%{_qt5_libdir}/qt5/qml/QtFeedback/*

%files devel
%{_qt5_libdir}/libQt5Feedback.so
%{_qt5_libdir}/libQt5Feedback.prl
%{_qt5_libdir}/libQt5Feedback.la
%{_qt5_libdir}/pkgconfig/Qt5Feedback.pc
%{_qt5_includedir}/QtFeedback/
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_feedback*.pri
%{_qt5_libdir}/cmake/Qt5Feedback/*.cmake

%changelog
%autochangelog

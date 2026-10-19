%global source0_hash 9d63759185e8faecd92f8d90e5a198010393e3d7fa3cb1e68f06b963d2bf95f9
%global qt_module qtfeedback
%global __brp_remove_la_files %nil
Summary:        Qt5 Tactile Feedback
Name:    qt5-qtfeedback
Version: 20180903gita14bd0b
Release:        13%{?dist}
License: GPL-2.0-or-later AND LGPL-3.0-only AND GFDL-1.3-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0 AND LGPL-2.1-only WITH Qt-LGPL-exception-1.1
Url:     https://code.qt.io/cgit/qt/qtfeedback.git/
Source0:        https://github.com/qt/%{qt_module}/archive/a14bd0bb1373cde86e09e3619fb9dc70f34c71f2.tar.gz#/%{qt_module}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
# /oreon:deps
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

%autosetup -n %{qt_module}-a14bd0bb1373cde86e09e3619fb9dc70f34c71f2 -p1
#  Taken from OpenSuse package (otherwise it fails to build)
touch .git # To make sure syncqt is used

%build

%{qmake_qt5} \
  CONFIG+=package multimedia_disabled=yes immersion_enabled=no meegotouchfeedback_enabled=no
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
%if 0%{?flatpak}
mv %{buildroot}/usr %{buildroot}%{_prefix}
sed -i -e "\|^libdir=|s|/usr/%{_lib}|%{_libdir}|" %{buildroot}%{_qt5_libdir}/*.la
sed -i -e "\|^prefix=|s|/usr|%{_prefix}|" %{buildroot}%{_qt5_libdir}/pkgconfig/*.pc
sed -i -e "\|^[^\#]|s|/usr|%{_prefix}|" %{buildroot}%{_qt5_libdir}/cmake/*/*.cmake
%endif
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtfeedback-devel -f %{oreon_filedir}/qt5-qtfeedback-devel.list

%changelog

%autochangelog

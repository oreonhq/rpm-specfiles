%global source0_hash 78b05bfac92bef099209aa56fdf4ca4558172583752f6736450fc0368bde01df
%global qt_module qtquickcontrols
Name:    qt5-%{qt_module}
Summary:        Qt5 - module with set of QtQuick controls
Version: 5.15.18
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
%global __provides_exclude_from ^%{_qt5_archdatadir}/qml/.*\\.so$
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# oreon:deps
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtdeclarative-devel
# /oreon:deps
%description
The Qt Quick Controls module provides a set of controls that can be used to
build complete interfaces in Qt Quick.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1

%build

%{qmake_qt5}
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtquickcontrols-examples -f %{oreon_filedir}/qt5-qtquickcontrols-examples.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import

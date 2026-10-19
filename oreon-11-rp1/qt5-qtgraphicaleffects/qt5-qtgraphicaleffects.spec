%global source0_hash dbefca590ef1d1f1c79c396f0f28f73cc16465c3a80803acc4a3ffa2f6d63225
%global qt_module qtgraphicaleffects
Summary:        Qt5 - QtGraphicalEffects component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        2%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
%global __provides_exclude_from ^%{_qt5_archdatadir}/qml/.*\\.so$
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# oreon:deps
BuildRequires:  libmng-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
# /oreon:deps
%description
The Qt Graphical Effects module provides a set of QML types for adding
visually impressive and configurable effects to user interfaces. Effects
are visual items that can be added to Qt Quick user interface as UI
components.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{qt_module}-everywhere-src-%{version}

%build

%{qmake_qt5}
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import

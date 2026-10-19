%global source0_hash 66b41538740a517973219d882d1ddf7288f3fdcbd5919205d86f539c2fb6b2f6
%global qt_module qtremoteobjects
%global __brp_remove_la_files %nil
Summary:        Qt5 - Qt Remote Objects
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# oreon:deps
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtremoteobjects-devel -f %{oreon_filedir}/qt5-qtremoteobjects-devel.list
%files -n qt5-qtremoteobjects-examples -f %{oreon_filedir}/qt5-qtremoteobjects-examples.list

%changelog

%autochangelog

%global source0_hash febbca9d491feca0fa2d770e912590b4ef18e461f739ca6e855ea62a488bbb6d
%{?mingw_package_header}
%global qt_module qt3d
%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{qt_version}%{?pre:-%{pre}}
%endif
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%define qt_version %(echo %{version} | cut -d~ -f1)
Name:           mingw-qt6-%{qt_module}
Version:        6.10.2
Release:        1%{?dist}
Summary:        Qt6 for Windows - Qt3d component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/
BuildArch:      noarch
%if 0%{?commit:1}
Source0:        http://download.qt.io/official_releases/qt/%{release_version}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%else
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase
BuildRequires:  mingw32-qt6-qtdeclarative
BuildRequires:  mingw32-qt6-qtshadertools
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase
BuildRequires:  mingw64-qt6-qtdeclarative
BuildRequires:  mingw64-qt6-qtshadertools
BuildRequires:  ninja-build
# /oreon:deps
%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt3d component
%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt3d component
%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%{?mingw_debug_package}

%prep

%autosetup -p1 -n %{source_folder}

%build

export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%mingw_cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-qt6-qt3d -f %{oreon_filedir}/mingw32-qt6-qt3d.list
%files -n mingw64-qt6-qt3d -f %{oreon_filedir}/mingw64-qt6-qt3d.list

%changelog

%autochangelog

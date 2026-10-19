%global source0_hash 642433ce7a058f537d93766a72b40f838efc897f9e442a825824d094ede1b3a3
%{?mingw_package_header}
%undefine _debugsource_packages
%undefine _debuginfo_subpackages
%global __debug_install_post %%{mingw_debug_install_post}; %{_bindir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}
%global qt_module qt3d
%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-qt5-%{qt_module}
Version:        5.15.18
Release:        1%{?dist}
Summary:        Qt5 for Windows - Qt3d component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/
%if 0%{?commit:1}
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
%else
%endif
Patch0:         qt3d-fix-zlib-linker-flags.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qtbase-devel
BuildRequires:  mingw32-qt5-qtbase-static
BuildRequires:  mingw32-qt5-qtdeclarative
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qtbase-devel
BuildRequires:  mingw64-qt5-qtbase-static
BuildRequires:  mingw64-qt5-qtdeclarative
BuildRequires:  zlib-devel
# /oreon:deps
%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - Qt3d component
BuildArch:      noarch
%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw32-qt5-%{qt_module}-tools
Summary:        Qt5 for Windows - Native tools for the Qt3d component
Requires:       mingw32-qt5-%{qt_module} = %{version}-%{release}
%description -n mingw32-qt5-%{qt_module}-tools
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - Qt3d component
BuildArch:      noarch
%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw64-qt5-%{qt_module}-tools
Summary:        Qt5 for Windows - Native tools for the Qt3d component
Requires:       mingw64-qt5-%{qt_module} = %{version}-%{release}
%description -n mingw64-qt5-%{qt_module}-tools
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%{?mingw_debug_package}

%prep

%autosetup -p1 -n %{source_folder}
%if 0%{?commit:1}
# Make sure the syncqt tool is run when using a git snapshot
mkdir .git
%endif

%build

%mingw_qmake_qt5 ../%{qt_module}.pro
%mingw_make_build
%install
%mingw_make install INSTALL_ROOT=%{buildroot}
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-qt5-%{qt_module}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-qt5-%{qt_module}.debugfiles
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-qt5-qt3d -f %{oreon_filedir}/mingw32-qt5-qt3d.list
%files -n mingw32-qt5-qt3d-tools -f %{oreon_filedir}/mingw32-qt5-qt3d-tools.list
%files -n mingw64-qt5-qt3d -f %{oreon_filedir}/mingw64-qt5-qt3d.list
%files -n mingw64-qt5-qt3d-tools -f %{oreon_filedir}/mingw64-qt5-qt3d-tools.list

%changelog

%autochangelog

%global source0_hash 78b05bfac92bef099209aa56fdf4ca4558172583752f6736450fc0368bde01df
%?mingw_package_header
%global qt_module qtquickcontrols
%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-qt5-%{qt_module}
Version:        5.15.18
Release:        1%{?dist}
Summary:        Qt5 for Windows - QtQuickControls component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/
%if 0%{?commit:1}
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
%else
%endif
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qmldevtools-devel
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qtdeclarative
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qmldevtools-devel
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qtdeclarative
# /oreon:deps
%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtQuickControls component
Requires:       mingw32-qt5-qtdeclarative
%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw32-qt5-%{qt_module}-static
Summary:       Static version of the mingw32-qt5-qtquickcontrols library
Requires:      mingw32-qt5-%{qt_module} = %{version}-%{release}
Requires:      mingw32-qt5-qtbase-static
Requires:      mingw32-qt5-qtdeclarative-static
%description -n mingw32-qt5-%{qt_module}-static
Static version of the mingw32-qt5-qtquickcontrols library.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtQuickControls component
Requires:       mingw64-qt5-qtdeclarative
%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw64-qt5-%{qt_module}-static
Summary:       Static version of the mingw64-qt5-qtquickcontrols library
Requires:      mingw64-qt5-%{qt_module} = %{version}-%{release}
Requires:      mingw64-qt5-qtbase-static
Requires:      mingw64-qt5-qtdeclarative-static
%description -n mingw64-qt5-%{qt_module}-static
Static version of the mingw64-qt5-qtquickcontrols library.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{source_folder}
%if 0%{?commit:1}
# Make sure the syncqt tool is run when using a git snapshot
mkdir .git
%endif

%build

MINGW_BUILDDIR_SUFFIX=_static %mingw_qmake_qt5 ../%{qt_module}.pro CONFIG+=static
MINGW_BUILDDIR_SUFFIX=_static %mingw_make_build
MINGW_BUILDDIR_SUFFIX=_shared %mingw_qmake_qt5 ../%{qt_module}.pro CONFIG+=shared
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make_build
%install
MINGW_BUILDDIR_SUFFIX=_static %mingw_make install INSTALL_ROOT=%{buildroot}
MINGW_BUILDDIR_SUFFIX=_shared %mingw_make install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-qt5-qtquickcontrols -f %{oreon_filedir}/mingw32-qt5-qtquickcontrols.list
%files -n mingw32-qt5-qtquickcontrols-static -f %{oreon_filedir}/mingw32-qt5-qtquickcontrols-static.list
%files -n mingw64-qt5-qtquickcontrols -f %{oreon_filedir}/mingw64-qt5-qtquickcontrols.list
%files -n mingw64-qt5-qtquickcontrols-static -f %{oreon_filedir}/mingw64-qt5-qtquickcontrols-static.list

%changelog

%autochangelog

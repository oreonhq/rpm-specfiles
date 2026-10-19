%global source0_hash 6716d2878d2146f13f11f0fb12f3437c09d85033bdd0684efacb43ea00fa1828
%{?mingw_package_header}
%global qt_module qtscript
%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-qt5-%{qt_module}
Version:        5.15.18
Release:        2%{?dist}
Summary:        Qt5 for Windows - QtScript component
License:        LicenseRef-Callaway-GPLv3-with-exceptions OR LGPL-2.0-or-later WITH FLTK-exception
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
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase
# /oreon:deps
%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtScript component
%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtScript component
%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{source_folder}
%if 0%{?commit:1}
# Make sure the syncqt tool is run when using a git snapshot
mkdir .git
%endif

%build

%mingw_qmake_qt5 ../qtscript.pro
%mingw_make_build
%install
%mingw_make install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-qt5-qtscript -f %{oreon_filedir}/mingw32-qt5-qtscript.list
%files -n mingw64-qt5-qtscript -f %{oreon_filedir}/mingw64-qt5-qtscript.list

%changelog

%autochangelog

%global source0_hash 6716d2878d2146f13f11f0fb12f3437c09d85033bdd0684efacb43ea00fa1828

%{?mingw_package_header}

%global qt_module qtscript
#global pre rc

#global commit d142740257fde3c9a1e17fd352bf0d5100b547ff
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt5-%{qt_module}
Version:        5.15.18
Release:        2%{?dist}
Summary:        Qt5 for Windows - QtScript component

# Automatically converted from old format: GPLv3 with exceptions or LGPLv2 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv3-with-exceptions OR LGPL-2.0-or-later WITH FLTK-exception
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}

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

# .prl files aren't interesting for us

# Win32
%files -n mingw32-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw32_bindir}/Qt5Script.dll
%{mingw32_bindir}/Qt5ScriptTools.dll
%{mingw32_includedir}/qt5/QtScript/
%{mingw32_includedir}/qt5/QtScriptTools/
%{mingw32_libdir}/*.prl
%{mingw32_libdir}/libQt5Script.dll.a
%{mingw32_libdir}/libQt5ScriptTools.dll.a
%{mingw32_libdir}/cmake/Qt5Script/
%{mingw32_libdir}/cmake/Qt5ScriptTools/
%{mingw32_libdir}/pkgconfig/Qt5Script.pc
%{mingw32_libdir}/pkgconfig/Qt5ScriptTools.pc
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_script.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_script_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_scripttools.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_scripttools_private.pri

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt5Script.dll
%{mingw64_bindir}/Qt5ScriptTools.dll
%{mingw64_includedir}/qt5/QtScript/
%{mingw64_includedir}/qt5/QtScriptTools/
%{mingw64_libdir}/*.prl
%{mingw64_libdir}/libQt5Script.dll.a
%{mingw64_libdir}/libQt5ScriptTools.dll.a
%{mingw64_libdir}/cmake/Qt5Script/
%{mingw64_libdir}/cmake/Qt5ScriptTools/
%{mingw64_libdir}/pkgconfig/Qt5Script.pc
%{mingw64_libdir}/pkgconfig/Qt5ScriptTools.pc
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_script.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_script_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_scripttools.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_scripttools_private.pri

%changelog
%autochangelog

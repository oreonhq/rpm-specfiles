%global source0_hash 931e0969d9f9d8f233e5e9bf9db0cea9ce9914d49982f1795fe6191010113568
%{?mingw_package_header}
%undefine _debugsource_packages
%undefine _debuginfo_subpackages
%global __debug_install_post %%{mingw_debug_install_post}; %{_bindir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}
%global qt_module qttools
%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
Name:           mingw-qt5-%{qt_module}
Version:        5.15.18
Release:        1%{?dist}
Summary:        Qt5 for Windows - QtTools component
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/
%if 0%{?commit:1}
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
%else
%endif
Patch0:         qttools-fix-qaxwidget-build.patch
Patch1:         qttools-qt5-suffix.patch
Patch2:         qttools-gcc11.patch
Patch3:         qttools-incompatible-pointer.patch
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qmldevtools-devel
BuildRequires:  mingw32-qt5-qtactiveqt
BuildRequires:  mingw32-qt5-qtbase
BuildRequires:  mingw32-qt5-qtbase-devel
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qmldevtools-devel
BuildRequires:  mingw64-qt5-qtactiveqt
BuildRequires:  mingw64-qt5-qtbase
BuildRequires:  mingw64-qt5-qtbase-devel
# /oreon:deps
%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtTools component
BuildArch:      noarch
%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw32-qt5-%{qt_module}-tools
Summary:        Qt5 for Windows - QtTools component
Obsoletes:      mingw32-qt5-%{qt_module}-lrelease < 5.1.2-1
Provides:       mingw32-qt5-%{qt_module}-lrelease = 5.1.2-1
Requires:       mingw32-qt5-qmldevtools-devel >= 5.6.0
%description -n mingw32-qt5-%{qt_module}-tools
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtTools component
BuildArch:      noarch
%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw64-qt5-%{qt_module}-tools
Summary:        Qt5 for Windows - QtTools component
Obsoletes:      mingw64-qt5-%{qt_module}-lrelease < 5.1.2-1
Provides:       mingw64-qt5-%{qt_module}-lrelease = 5.1.2-1
Requires:       mingw64-qt5-qmldevtools-devel >= 5.6.0
%description -n mingw64-qt5-%{qt_module}-tools
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

%mingw_qmake_qt5 ../%{qt_module}.pro
%mingw_make_build
%install
%mingw_make install INSTALL_ROOT=%{buildroot}
rm -f %{buildroot}%{mingw32_libdir}/*.dll
rm -f %{buildroot}%{mingw64_libdir}/*.dll
for fn in %{buildroot}%{mingw32_bindir}/*.exe %{buildroot}%{mingw64_bindir}/*.exe ; do
    fn_new=$(echo $fn | sed s/'.exe$'/'-qt5.exe'/)
    mv $fn $fn_new
done
mkdir -p %{buildroot}%{_bindir}
for tool in lconvert lupdate lrelease; do
    ln -s ../%{mingw32_target}/bin/qt5/$tool %{buildroot}%{_bindir}/%{mingw32_target}-$tool-qt5
    ln -s ../%{mingw64_target}/bin/qt5/$tool %{buildroot}%{_bindir}/%{mingw64_target}-$tool-qt5
done
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-qt5-qttools -f %{oreon_filedir}/mingw32-qt5-qttools.list
%files -n mingw32-qt5-qttools-tools -f %{oreon_filedir}/mingw32-qt5-qttools-tools.list
%files -n mingw64-qt5-qttools -f %{oreon_filedir}/mingw64-qt5-qttools.list
%files -n mingw64-qt5-qttools-tools -f %{oreon_filedir}/mingw64-qt5-qttools-tools.list

%changelog

%autochangelog

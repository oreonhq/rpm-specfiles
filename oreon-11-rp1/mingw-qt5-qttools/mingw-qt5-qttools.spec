%global source0_hash 931e0969d9f9d8f233e5e9bf9db0cea9ce9914d49982f1795fe6191010113568

%{?mingw_package_header}

# Disable debuginfo subpackages and debugsource packages for now to use old logic
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Override the __debug_install_post argument as this package
# contains both native as well as cross compiled binaries
%global __debug_install_post %%{mingw_debug_install_post}; %{_bindir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}

%global qt_module qttools
#global pre beta

#global commit 769fa282ac8a4b98698dada6969452363e0eb415
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
Summary:        Qt5 for Windows - QtTools component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif

# Fix undefined references when buildling qaxwidget designer plugin
Patch0:         qttools-fix-qaxwidget-build.patch
# Run tools with -qt5 suffix
Patch1:         qttools-qt5-suffix.patch
# gcc-11 related fixes
Patch2:         qttools-gcc11.patch
# Fix passing incompatible pointer
Patch3:         qttools-incompatible-pointer.patch

BuildRequires:  gcc-c++
BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtbase-devel = %{version}
BuildRequires:  mingw32-qt5-qmldevtools-devel = %{version}
BuildRequires:  mingw32-qt5-qtactiveqt = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtbase-devel = %{version}
BuildRequires:  mingw64-qt5-qmldevtools-devel = %{version}
BuildRequires:  mingw64-qt5-qtactiveqt = %{version}

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

# Some tools depend on libQt5QmlDevTools.so.5 which is in
# a non-default path so the regular RPM dependency generator
# doesn't automatically add the correct Requires tag
# https://bugzilla.redhat.com/show_bug.cgi?id=1301577
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

# Some tools depend on libQt5QmlDevTools.so.5 which is in
# a non-default path so the regular RPM dependency generator
# doesn't automatically add the correct Requires tag
# https://bugzilla.redhat.com/show_bug.cgi?id=1301577
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

# The .dll's are installed in both %%{mingw32_bindir} and %%{mingw32_libdir}
# One copy of the .dll's is sufficient
rm -f %{buildroot}%{mingw32_libdir}/*.dll
rm -f %{buildroot}%{mingw64_libdir}/*.dll

# Make sure the executables don't conflict with their mingw-qt4 counterpart
for fn in %{buildroot}%{mingw32_bindir}/*.exe %{buildroot}%{mingw64_bindir}/*.exe ; do
    fn_new=$(echo $fn | sed s/'.exe$'/'-qt5.exe'/)
    mv $fn $fn_new
done

# Create symlinks for the tools lconvert, lupdate and lrelease tools
mkdir -p %{buildroot}%{_bindir}

for tool in lconvert lupdate lrelease; do
    ln -s ../%{mingw32_target}/bin/qt5/$tool %{buildroot}%{_bindir}/%{mingw32_target}-$tool-qt5
    ln -s ../%{mingw64_target}/bin/qt5/$tool %{buildroot}%{_bindir}/%{mingw64_target}-$tool-qt5
done

# Win32
%files -n mingw32-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw32_bindir}/Qt5Designer.dll
%{mingw32_bindir}/Qt5DesignerComponents.dll
%{mingw32_bindir}/Qt5Help.dll
%{mingw32_bindir}/assistant-qt5.exe
%{mingw32_bindir}/designer-qt5.exe
%{mingw32_bindir}/linguist-qt5.exe
%{mingw32_bindir}/pixeltool-qt5.exe
%{mingw32_bindir}/qcollectiongenerator-qt5.exe
%{mingw32_bindir}/qdbus-qt5.exe
%{mingw32_bindir}/qdbusviewer-qt5.exe
%{mingw32_bindir}/qhelpgenerator-qt5.exe
%{mingw32_bindir}/qtdiag-qt5.exe
%{mingw32_bindir}/qdistancefieldgenerator-qt5.exe
%{mingw32_bindir}/qtpaths-qt5.exe
%{mingw32_bindir}/qtplugininfo-qt5.exe
%{mingw32_includedir}/qt5/QtDesigner/
%{mingw32_includedir}/qt5/QtDesignerComponents/
%{mingw32_includedir}/qt5/QtHelp/
%{mingw32_includedir}/qt5/QtUiPlugin/
%{mingw32_includedir}/qt5/QtUiTools/
%{mingw32_libdir}/*.prl
%{mingw32_libdir}/libQt5Designer.dll.a
%{mingw32_libdir}/libQt5DesignerComponents.dll.a
%{mingw32_libdir}/libQt5Help.dll.a
# QtUiTools is only built as static library by default
%{mingw32_libdir}/libQt5UiTools.a
%{mingw32_libdir}/qt5/plugins/designer/
%{mingw32_libdir}/cmake/Qt5AttributionsScannerTools/
%{mingw32_libdir}/cmake/Qt5Designer/
%{mingw32_libdir}/cmake/Qt5DesignerComponents/
%{mingw32_libdir}/cmake/Qt5Help/
%{mingw32_libdir}/cmake/Qt5LinguistTools/
%{mingw32_libdir}/cmake/Qt5UiPlugin/
%{mingw32_libdir}/cmake/Qt5UiTools/
%{mingw32_libdir}/pkgconfig/Qt5Designer.pc
%{mingw32_libdir}/pkgconfig/Qt5Help.pc
%{mingw32_libdir}/pkgconfig/Qt5UiTools.pc
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_designer.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_designer_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_designercomponents_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_help.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_help_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_uiplugin.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_uitools.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_uitools_private.pri
%{mingw32_datadir}/qt5/phrasebooks/

%files -n mingw32-qt5-%{qt_module}-tools
%{_bindir}/%{mingw32_target}-lconvert-qt5
%{_bindir}/%{mingw32_target}-lupdate-qt5
%{_bindir}/%{mingw32_target}-lrelease-qt5
%{_prefix}/%{mingw32_target}/bin/qt5/lconvert
%{_prefix}/%{mingw32_target}/bin/qt5/lupdate
%{_prefix}/%{mingw32_target}/bin/qt5/lupdate-pro
%{_prefix}/%{mingw32_target}/bin/qt5/lprodump
%{_prefix}/%{mingw32_target}/bin/qt5/lrelease
%{_prefix}/%{mingw32_target}/bin/qt5/lrelease-pro
%{_prefix}/%{mingw32_target}/bin/qt5/qtattributionsscanner
%{_prefix}/%{mingw32_target}/bin/qt5/windeployqt

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt5Designer.dll
%{mingw64_bindir}/Qt5DesignerComponents.dll
%{mingw64_bindir}/Qt5Help.dll
%{mingw64_bindir}/assistant-qt5.exe
%{mingw64_bindir}/designer-qt5.exe
%{mingw64_bindir}/linguist-qt5.exe
%{mingw64_bindir}/pixeltool-qt5.exe
%{mingw64_bindir}/qcollectiongenerator-qt5.exe
%{mingw64_bindir}/qdbus-qt5.exe
%{mingw64_bindir}/qdbusviewer-qt5.exe
%{mingw64_bindir}/qhelpgenerator-qt5.exe
%{mingw64_bindir}/qtdiag-qt5.exe
%{mingw64_bindir}/qdistancefieldgenerator-qt5.exe
%{mingw64_bindir}/qtpaths-qt5.exe
%{mingw64_bindir}/qtplugininfo-qt5.exe
%{mingw64_includedir}/qt5/QtDesigner/
%{mingw64_includedir}/qt5/QtDesignerComponents/
%{mingw64_includedir}/qt5/QtHelp/
%{mingw64_includedir}/qt5/QtUiPlugin/
%{mingw64_includedir}/qt5/QtUiTools/
%{mingw64_libdir}/*.prl
%{mingw64_libdir}/libQt5Designer.dll.a
%{mingw64_libdir}/libQt5DesignerComponents.dll.a
%{mingw64_libdir}/libQt5Help.dll.a
# QtUiTools is only built as static library by default
%{mingw64_libdir}/libQt5UiTools.a
%{mingw64_libdir}/qt5/plugins/designer/
%{mingw64_libdir}/cmake/Qt5AttributionsScannerTools/
%{mingw64_libdir}/cmake/Qt5Designer/
%{mingw64_libdir}/cmake/Qt5DesignerComponents/
%{mingw64_libdir}/cmake/Qt5Help/
%{mingw64_libdir}/cmake/Qt5LinguistTools/
%{mingw64_libdir}/cmake/Qt5UiPlugin/
%{mingw64_libdir}/cmake/Qt5UiTools/
%{mingw64_libdir}/pkgconfig/Qt5Designer.pc
%{mingw64_libdir}/pkgconfig/Qt5Help.pc
%{mingw64_libdir}/pkgconfig/Qt5UiTools.pc
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_designer.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_designer_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_designercomponents_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_help.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_help_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_uiplugin.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_uitools.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_uitools_private.pri
%{mingw64_datadir}/qt5/phrasebooks/

%files -n mingw64-qt5-%{qt_module}-tools
%{_bindir}/%{mingw64_target}-lconvert-qt5
%{_bindir}/%{mingw64_target}-lupdate-qt5
%{_bindir}/%{mingw64_target}-lrelease-qt5
%{_prefix}/%{mingw64_target}/bin/qt5/lconvert
%{_prefix}/%{mingw64_target}/bin/qt5/lupdate
%{_prefix}/%{mingw64_target}/bin/qt5/lupdate-pro
%{_prefix}/%{mingw64_target}/bin/qt5/lprodump
%{_prefix}/%{mingw64_target}/bin/qt5/lrelease
%{_prefix}/%{mingw64_target}/bin/qt5/lrelease-pro
%{_prefix}/%{mingw64_target}/bin/qt5/qtattributionsscanner
%{_prefix}/%{mingw64_target}/bin/qt5/windeployqt

%changelog
%autochangelog

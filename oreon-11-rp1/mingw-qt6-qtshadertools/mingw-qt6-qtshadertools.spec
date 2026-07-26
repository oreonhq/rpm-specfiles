%global source0_hash 18d9dbbc4f7e6e96e6ed89a9965dc032e2b58158b65156c035537826216716c9

%{?mingw_package_header}

%global qt_module qtshadertools
#global pre rc

#global commit a73dfa7c63b82e25f93e44ed6386664373aaca74
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{qt_version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%define qt_version %(echo %{version} | cut -d~ -f1)

Name:           mingw-qt6-%{qt_module}
Version:        6.10.2
Release:        1%{?dist}
Summary:        Qt6 for Windows - Qt Shader Tools component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{qt_version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{qt_version}%{?pre:-%pre}.tar.xz
%endif
Patch0:         qtshadertools_gcc13.patch

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  qt6-qtshadertools-devel = %{version}

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-vulkan-headers

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-vulkan-headers

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt Serial Port component
# Dependency for host tools
Requires:       qt6-qtshadertools-devel = %{version}

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt Serial Port component
# Dependency for host tools
Requires:       qt6-qtshadertools-devel = %{version}

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{source_folder}

%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%mingw_cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja

%install
%mingw_ninja_install

# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/Qt6ShaderTools.dll
%{mingw32_libdir}/cmake/Qt6ShaderTools/
%{mingw32_libdir}/cmake/Qt6ShaderToolsPrivate/
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtShaderToolsTestsConfig.cmake
%{mingw32_libdir}/libQt6ShaderTools.dll.a
%{mingw32_libdir}/Qt6ShaderTools.prl
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_shadertools_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_shadertools.pri
%{mingw32_libdir}/qt6/metatypes/qt6shadertools_metatypes.json
%{mingw32_libdir}/qt6/modules/ShaderTools.json
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx
%{mingw32_libdir}/pkgconfig/Qt6ShaderTools.pc
%{mingw32_includedir}/qt6/QtShaderTools/

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6ShaderTools.dll
%{mingw64_libdir}/cmake/Qt6ShaderTools/
%{mingw64_libdir}/cmake/Qt6ShaderToolsPrivate/
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtShaderToolsTestsConfig.cmake
%{mingw64_libdir}/libQt6ShaderTools.dll.a
%{mingw64_libdir}/Qt6ShaderTools.prl
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_shadertools_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_shadertools.pri
%{mingw64_libdir}/qt6/metatypes/qt6shadertools_metatypes.json
%{mingw64_libdir}/qt6/modules/ShaderTools.json
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx
%{mingw64_libdir}/pkgconfig/Qt6ShaderTools.pc
%{mingw64_includedir}/qt6/QtShaderTools/

%changelog
%autochangelog

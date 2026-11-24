# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 805046b8b7757665586890b375940047e874ae3ab00adb6d3f2b38fc6b200b1c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global qt_module qtshadertools

Summary: Qt6 - Qt Shader Tools module builds on the SPIR-V Open Source Ecosystem
Name:    qt6-%{qt_module}
Version: 6.11.2
Release: 1%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz

Patch0: qtshadertools-unbundle-glslang.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel%{?_isa}
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: glslang-devel
BuildRequires: spirv-tools-devel
BuildRequires: pkgconfig(xkbcommon) >= 0.4.1

Provides: bundled(spirv-cross)

%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: spirv-tools
%description devel
%{summary}.

%prep
%oreon_sha256
%autosetup -n %{qt_module}-everywhere-src-%{qt_version} -p1

rm -rf src/3rdparty/glslang/glslang
pushd src/3rdparty/glslang/SPIRV
find . -not -name SPVRemapper.cpp -not -name SPVRemapper.h -not -name doc.h \
       -not -path . -delete
popd

%build
%cmake_qt6

%cmake_build

%install
%cmake_install

mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    qsb)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}-qt6
      ;;
    *)
      ln -v  ${i} %{buildroot}%{_bindir}/${i}
      ;;
  esac
done
popd

pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd

%ldconfig_scriptlets

%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/qtshadertools-%{qt_version}.spdx
%{_bindir}/qsb-qt6
%{_qt6_bindir}/qsb
%{_qt6_libdir}/libQt6ShaderTools.so.6*

%files devel
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_headerdir}/QtShaderTools/
%{_qt6_libdir}/libQt6ShaderTools.prl
%{_qt6_libdir}/libQt6ShaderTools.so
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtShaderToolsTestsConfig.cmake
%dir %{_qt6_libdir}/cmake/Qt6ShaderTools/
%dir %{_qt6_libdir}/cmake/Qt6ShaderToolsPrivate/
%{_qt6_libdir}/cmake/Qt6ShaderTools/*.cmake
%{_qt6_libdir}/cmake/Qt6ShaderToolsPrivate/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6ShaderToolsTools/
%{_qt6_libdir}/cmake/Qt6ShaderToolsTools/*.cmake
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/pkgconfig/Qt6ShaderTools.pc

%changelog
%autochangelog

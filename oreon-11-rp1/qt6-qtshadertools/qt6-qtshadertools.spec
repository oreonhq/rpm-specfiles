%global source0_hash none

%global qt_module qtshadertools

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

Summary: Qt6 - Qt Shader Tools module builds on the SPIR-V Open Source Ecosystem
Name:    qt6-%{qt_module}
Version: 6.10.3
Release: 2%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0:        https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

# Downstream patches
# Patch0: qtshadertools-unbundle-glslang.patch

# Upstream patches

# Upstreamable patches

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
# BuildRequires: glslang-devel
# BuildRequires: spirv-tools-devel
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1

# Make sure 3rdparty/glslang isn't used
# pushd src/3rdparty
# rm -rf glslang
# popd

%build
%cmake_qt6

%cmake_build


%install
%cmake_install

# hardlink files to %%{_bindir}, add -qt6 postfix to not conflict
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

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
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
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-2
- Sync module to Qt 6.10.3 (match qt6-qtbase / qt6-rpm-macros)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-2
- Prepare for Oreon 11 (RP1)

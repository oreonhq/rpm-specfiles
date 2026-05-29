%global source0_hash none

%global qt_module qtquick3d

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

# Always bundle assimp and OpenXR. Oreon mock often defines %%{?fedora} without
# %%{?oreon}, which flipped these back to system libs and made qt6-qtquick3d
# require libassimp.so / libopenxr_loader.so even though we never want that
# closure on the ISO (see anaconda-dnf-problems.log).
%global system_assimp 0
%global system_openxr 0
%if %{system_assimp}
%global _qt_feat_system_assimp ON
%else
%global _qt_feat_system_assimp OFF
%endif
%if %{system_openxr}
%global _qt_feat_system_openxr ON
%else
%global _qt_feat_system_openxr OFF
%endif

Summary: Qt6 - Quick3D Libraries and utilities
Name:    qt6-%{qt_module}
Version: 6.10.3
Release: 8%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif
Patch0:  qtquick3d-fix-build-with-gcc11.patch
# Shipped in every SRPM so %%{?fedora} >= 43 and Oreon builds always have the file
# Applied in %%prep only when using system assimp (Fedora 43+ or %%{?oreon})
# From https://gitlab.archlinux.org/archlinux/packaging/packages/qt6-quick3d
Patch1:  qtquick3d-fix-build-with-assimp6.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros >= %{version}
BuildRequires: qt6-qtbase-static >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel
BuildRequires: qt6-qtdeclarative-static
BuildRequires: pkgconfig(Qt6QuickLayouts)
BuildRequires: qt6-qtquicktimeline-devel
BuildRequires: qt6-qtshadertools-devel
%if 0%{?system_assimp}
BuildRequires: pkgconfig(assimp) >= 5.0.0
%else
Provides:      bundled(assimp)
%endif
%if 0%{?system_openxr}
BuildRequires: openxr-devel
%else
Provides:      bundled(openxr)
%endif

# Bundled embree is only used on aarch64 and x86_64
# Could be potentially unbundled
%ifarch aarch64 x86_64
Provides:      bundled(embree3) = 3.13.3
%endif

%description
The Qt 6 Quick3D library.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# BuildRequires: qt6-qtquick3d-devel (same version as this package)
%description examples
%{summary}.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}}
%patch -P 0 -p1
%if 0%{?system_assimp}
%patch -P 1 -p1
%endif


%build
%if 0%{?rhel} >= 10
%ifarch x86_64
# The bundled embree attempts to limit optimization to SSE4.1 and disable AVX,
# but RHEL 10 defaults to -march=x86-64-v3 which includes AVX, resulting in
# build failures due to missing symbols from the AVX code which is not built.
CXXFLAGS="$CXXFLAGS -mno-avx"
%endif
%endif

# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}

%cmake_qt6 \
  -DCMAKE_SKIP_PRECOMPILE_HEADERS=ON \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF} \
  -DFEATURE_system_assimp=%{_qt_feat_system_assimp} \
  -DFEATURE_system_openxr=%{_qt_feat_system_openxr}

%cmake_build


%install
%cmake_install

# hardlink files to %%{_bindir}, add -qt6 postfix to not conflict
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    balsam|meshdebug|shadergen|balsamui|instancer|materialeditor|shapegen|lightmapviewer)
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
%license LICENSES/GPL*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6Quick3D.so.6*
%{_qt6_libdir}/libQt6Quick3DAssetImport.so.6*
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.so.6*
%{_qt6_libdir}/libQt6Quick3DUtils.so.6*
%{_qt6_libdir}/libQt6Quick3DIblBaker.so.6*
%{_qt6_libdir}/libQt6Quick3DParticles.so.6*
%{_qt6_libdir}/libQt6Quick3DAssetUtils.so.6*
%{_qt6_libdir}/libQt6Quick3DEffects.so.6*
%{_qt6_libdir}/libQt6Quick3DHelpers.so.6*
%{_qt6_libdir}/libQt6Quick3DHelpersImpl.so*
%{_qt6_libdir}/libQt6Quick3DParticleEffects.so.6*
%{_qt6_libdir}/libQt6Quick3DGlslParser.so.6*
%{_qt6_libdir}/libQt6Quick3DXr.so.6*
%dir %{_qt6_qmldir}/QtQuick3D/
%{_qt6_qmldir}/QtQuick3D/
%dir %{_qt6_plugindir}/assetimporters
%{_qt6_plugindir}/assetimporters/*.so

%files devel
%{_bindir}/balsam-qt6
%{_bindir}/meshdebug-qt6
%{_bindir}/shadergen-qt6
%{_bindir}/balsamui-qt6
%{_bindir}/instancer-qt6
%{_bindir}/materialeditor-qt6
%{_bindir}/shapegen-qt6
%{_bindir}/lightmapviewer-qt6
%{_qt6_bindir}/balsam
%{_qt6_bindir}/meshdebug
%{_qt6_bindir}/shadergen
%{_qt6_bindir}/balsamui
%{_qt6_bindir}/instancer
%{_qt6_bindir}/materialeditor
%{_qt6_bindir}/shapegen
%{_qt6_bindir}/lightmapviewer
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_includedir}/QtQuick3D
%{_qt6_includedir}/QtQuick3DAssetImport
%{_qt6_includedir}/QtQuick3DIblBaker
%{_qt6_includedir}/QtQuick3DParticles
%{_qt6_includedir}/QtQuick3DRuntimeRender
%{_qt6_includedir}/QtQuick3DUtils
%{_qt6_includedir}/QtQuick3DAssetUtils
%{_qt6_includedir}/QtQuick3DHelpers
%{_qt6_includedir}/QtQuick3DHelpersImpl
%{_qt6_includedir}/QtQuick3DGlslParser
%{_qt6_includedir}/QtQuick3DXr
%ifarch x86_64 aarch64
%dir %{_qt6_libdir}/cmake/Qt6BundledEmbree/
%{_qt6_libdir}/cmake/Qt6/FindWrapBundledEmbreeConfigExtra.cmake
%{_qt6_libdir}/cmake/Qt6BundledEmbree/*.cmake
%endif
%if !0%{?system_openxr}
%dir %{_qt6_libdir}/cmake/Qt6BundledOpenXR/
%{_qt6_libdir}/cmake/Qt6BundledOpenXR/*.cmake
%endif
%dir %{_qt6_libdir}/cmake/Qt6Quick3D/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DAssetImport/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DAssetImportPrivate
%dir %{_qt6_libdir}/cmake/Qt6Quick3DAssetUtils/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DAssetUtilsPrivate
%dir %{_qt6_libdir}/cmake/Qt6Quick3DEffects/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DGlslParserPrivate
%dir %{_qt6_libdir}/cmake/Qt6Quick3DHelpers/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DHelpersPrivate/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DHelpersImpl/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DHelpersImplPrivate
%dir %{_qt6_libdir}/cmake/Qt6Quick3DIblBaker
%dir %{_qt6_libdir}/cmake/Qt6Quick3DIblBakerPrivate
%dir %{_qt6_libdir}/cmake/Qt6Quick3DParticleEffects
%dir %{_qt6_libdir}/cmake/Qt6Quick3DParticles
%dir %{_qt6_libdir}/cmake/Qt6Quick3DParticlesPrivate
%dir %{_qt6_libdir}/cmake/Qt6Quick3DPrivate
%dir %{_qt6_libdir}/cmake/Qt6Quick3DRuntimeRender/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DRuntimeRenderPrivate
%dir %{_qt6_libdir}/cmake/Qt6Quick3DTools/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DUtils/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DUtilsPrivate
%dir %{_qt6_libdir}/cmake/Qt6Quick3DXr/
%dir %{_qt6_libdir}/cmake/Qt6Quick3DXrPrivate
%{_qt6_libdir}/cmake/Qt6/*.cmake
%{_qt6_libdir}/cmake/Qt6/FindWrapQuick3DAssimp.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/*.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3D/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DAssetImport/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DAssetImportPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DAssetUtils/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DAssetUtilsPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DEffects/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DGlslParserPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DHelpers/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DHelpersPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DHelpersImpl/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DHelpersImplPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DIblBaker/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DIblBakerPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DParticleEffects/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DParticles/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DParticlesPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DRuntimeRender/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DRuntimeRenderPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DTools/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DUtils/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DUtilsPrivate/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DXr/*.cmake
%{_qt6_libdir}/cmake/Qt6Quick3DXrPrivate/*.cmake
%ifarch x86_64 aarch64
%{_qt6_libdir}/libQt6BundledEmbree.a
%endif
%if !0%{?system_openxr}
%{_qt6_libdir}/libQt6BundledOpenXR.a
%endif
%{_qt6_libdir}/libQt6Quick3DXr.prl
%{_qt6_libdir}/libQt6Quick3DXr.so
%{_qt6_libdir}/libQt6Quick3D.prl
%{_qt6_libdir}/libQt6Quick3D.so
%{_qt6_libdir}/libQt6Quick3DAssetImport.prl
%{_qt6_libdir}/libQt6Quick3DAssetImport.so
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.prl
%{_qt6_libdir}/libQt6Quick3DRuntimeRender.so
%{_qt6_libdir}/libQt6Quick3DUtils.prl
%{_qt6_libdir}/libQt6Quick3DUtils.so
%{_qt6_libdir}/libQt6Quick3DIblBaker.prl
%{_qt6_libdir}/libQt6Quick3DIblBaker.so
%{_qt6_libdir}/libQt6Quick3DParticles.prl
%{_qt6_libdir}/libQt6Quick3DParticles.so
%{_qt6_libdir}/libQt6Quick3DAssetUtils.prl
%{_qt6_libdir}/libQt6Quick3DAssetUtils.so
%{_qt6_libdir}/libQt6Quick3DEffects.prl
%{_qt6_libdir}/libQt6Quick3DEffects.so
%{_qt6_libdir}/libQt6Quick3DHelpers.prl
%{_qt6_libdir}/libQt6Quick3DHelpers.so
%{_qt6_libdir}/libQt6Quick3DHelpersImpl.prl
%{_qt6_libdir}/libQt6Quick3DHelpersImpl.so
%{_qt6_libdir}/libQt6Quick3DGlslParser.prl
%{_qt6_libdir}/libQt6Quick3DGlslParser.so
%{_qt6_libdir}/libQt6Quick3DParticleEffects.prl
%{_qt6_libdir}/libQt6Quick3DParticleEffects.so
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_plugindir}/qmltooling/libqmldbg_quick3dprofiler.so
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif

%changelog
* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-8
- Drop qt6-qtquicklayouts-devel (not in Fedora 43); keep pkgconfig(Qt6QuickLayouts)

* Sun Apr 19 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-7
- BR qt6-qtquicklayouts-devel, skip CMake PCH (aarch64 / disk)

* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-3
- Sync module to Qt 6.10.3 (match qt6-qtbase / qt6-rpm-macros)

* Wed Apr 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-3
- Always list assimp6 patch in SRPM apply only for Fedora 43+ or %%{?oreon}

* Tue Apr 07 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-2
- Oreon uses system assimp like Fedora, apply assimp6 wrap patch when %%{?oreon} is set

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-1
- Prepare for Oreon 11 (RP1)

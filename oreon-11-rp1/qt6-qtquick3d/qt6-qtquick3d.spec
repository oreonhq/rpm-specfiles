%global source0_hash 6ced6edbd25fb5a632fe770ae820b376bf50233e8d62002c79a69a505a2e429e
%global qt_module qtquick3d
%if 0%{?unstable}
%global prerelease rc
%endif
%global examples 1
%if 0%{?fedora} || (0%{?oreon} >= 11)
%global system_assimp 1
%global system_openxr 1
%endif
Summary:        Qt6 - Quick3D Libraries and utilities
Name:    qt6-%{qt_module}
Version: 6.12.0
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
Source0:        https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-s%{prerelease}-%{version}.tar.xz
%else
%endif
Patch0:  qtquick3d-fix-build-with-gcc11.patch
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
%if 0%{?system_assimp}
%else
Provides:      bundled(assimp)
%endif
%if 0%{?system_openxr}
%else
Provides:      bundled(openxr)
%endif
%ifarch aarch64 x86_64
Provides:      bundled(embree3) = 3.13.3
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  openxr-devel
BuildRequires:  pkgconfig(Qt6QuickLayouts)
BuildRequires:  pkgconfig(assimp)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-static
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtdeclarative-static
BuildRequires:  qt6-qtquicktimeline-devel
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qt6-rpm-macros
# /oreon:deps
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
%description examples
%{summary}.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1

%build

%define _lto_cflags %{nil}
%cmake_qt6 \
  -DCMAKE_SKIP_PRECOMPILE_HEADERS=ON \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF} \
  -DFEATURE_system_assimp=%{?system_assimp:ON}%{!?system_assimp:OFF} \
  -DFEATURE_system_openxr=%{?system_openxr:ON}%{!?system_openxr:OFF}
%cmake_build
%install
%cmake_install
mkdir %{buildroot}%{_bindir}
pushd %{buildroot}%{_qt6_bindir}
for i in * ; do
  case "${i}" in
    balsam|meshdebug|shadergen|balsamui|instancer|materialeditor|shapegen|lightmapviewer|particleshadergen)
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt6-qtquick3d-devel -f %{oreon_filedir}/qt6-qtquick3d-devel.list
%files -n qt6-qtquick3d-examples -f %{oreon_filedir}/qt6-qtquick3d-examples.list

%changelog

%autochangelog

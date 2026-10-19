%global source0_hash d16f7489945c6c9e971cedd4362202a2681f3c10393461e1f5e74425f7fef59a
%global qt_module qt3d
%if 0%{?unstable}
%global prerelease rc
%endif
Summary:        Qt6 - Qt3D QML bindings and C++ APIs
Name:    qt6-%{qt_module}
Version: 6.12.0
Release:        1%{?dist}
%global examples 1
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
%else
Source0:        https://download.qt.io/a%{prerelease}hive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-s%{prerelease}-%{version}.tar.xz
%endif
Source1: qt3dcore-config-multilib_p.h
Patch0:  qt3d-assimp-fix-build.patch
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
%global bundled_assimp 1
Requires: qt6-qtimageformats%{?_isa} >= %{version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtbase-static
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtimageformats
BuildRequires:  qt6-qtshadertools-devel
BuildRequires:  qt6-rpm-macros
# /oreon:deps
%description
Qt 3D provides functionality for near-realtime simulation systems with
support for 2D and 3D rendering in both Qt C++ and Qt Quick applications).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
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
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF} \
  -DFEATURE_qt3d_system_assimp=%{?bundled_assimp:OFF}%{!?bundled_assimp:ON}
%cmake_build
%install
%cmake_install
%ifarch %{multilib_archs}
  mv %{buildroot}%{_qt6_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config_p.h %{buildroot}%{_qt6_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config-%{__isa_bits}_p.h
  install -p -m644 -D %{SOURCE1} %{buildroot}%{_qt6_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config_p.h
%endif
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
%files -n qt6-qt3d-devel -f %{oreon_filedir}/qt6-qt3d-devel.list
%files -n qt6-qt3d-examples -f %{oreon_filedir}/qt6-qt3d-examples.list

%changelog

%autochangelog

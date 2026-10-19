%global source0_hash 642433ce7a058f537d93766a72b40f838efc897f9e442a825824d094ede1b3a3
%global qt_module qt3d
%global multilib_archs x86_64 %{ix86} %{?mips} ppc64 ppc s390x s390 sparc64 sparcv9
Summary:        Qt5 - Qt3D QML bindings and C++ APIs
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
Source1: qt3dcore-config-multilib_p.h
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
%if 0%{?fedora} || (0%{?oreon} >= 11)
%endif
Requires: qt5-qtimageformats%{?_isa} >= %{version}
# oreon:deps
BuildRequires:  make
BuildRequires:  pkgconfig(assimp)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtimageformats
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  qt5-rpm-macros
# /oreon:deps
%description
Qt 3D provides functionality for near-realtime simulation systems with
support for 2D and 3D rendering in both Qt C++ and Qt Quick applications).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{qt_module}-everywhere-src-%{version}

%build

%define _lto_cflags %{nil}
%{qmake_qt5}
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
%ifarch %{multilib_archs}
  mv %{buildroot}%{_qt5_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config_p.h %{buildroot}%{_qt5_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config-%{__isa_bits}_p.h
  install -p -m644 -D %{SOURCE1} %{buildroot}%{_qt5_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config_p.h
%endif
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
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
%files -n qt5-qt3d-devel -f %{oreon_filedir}/qt5-qt3d-devel.list
%files -n qt5-qt3d-examples -f %{oreon_filedir}/qt5-qt3d-examples.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import

%global source0_hash 3dfc92cb64fb330ff4538bec7f5c34906289728d53b046f478f05787ddc00db9
%global qt_module qtquickcontrols2
Name:    qt5-%{qt_module}
Summary:        Qt5 - module with set of QtQuick controls for embedded
Version: 5.15.18
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
Patch1:  0001-Unset-mouseGrabberPopup-if-it-s-removed-from-childre.patch
Patch2:  0002-Ensure-we-don-t-crash-when-changing-sizes-after-clea.patch
Patch3:  0003-implement-a11y-pressing-of-qquickabstractbutton.patch
Patch4:  0004-Fix-the-popup-position-of-a-Menu.patch
Patch5:  0005-Accessibility-respect-value-in-attached-Accessible-i.patch
%global __provides_exclude_from ^%{_qt5_archdatadir}/qml/.*\\.so$
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires: qt5-qtdeclarative%{?_isa} >= %{version}
Requires: qt5-qtgraphicaleffects%{_isa} >= %{version}
# oreon:deps
BuildRequires:  make
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
# /oreon:deps
%description
The Qt Labs Controls module provides a set of controls that can be used to
build complete interfaces in Qt Quick.

Unlike Qt Quick Controls, these controls are optimized for embedded systems
and so are preferred for hardware with limited resources.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
Requires: qt5-qtdeclarative-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary:        Examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{qt_module}-everywhere-src-%{version}

%build

%{qmake_qt5}
%make_build
%install
make install INSTALL_ROOT=%{buildroot}
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd
rm -f %{buildroot}%{_qt5_libdir}/libQt5*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtquickcontrols2-devel -f %{oreon_filedir}/qt5-qtquickcontrols2-devel.list
%files -n qt5-qtquickcontrols2-examples -f %{oreon_filedir}/qt5-qtquickcontrols2-examples.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import

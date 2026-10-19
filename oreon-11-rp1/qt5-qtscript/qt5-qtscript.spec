%global source0_hash 6716d2878d2146f13f11f0fb12f3437c09d85033bdd0684efacb43ea00fa1828
%if !0%{?bootstrap}
%ifnarch %{arm}
%global tests 1
%endif
%endif
%global qt_module qtscript
Summary:        Qt5 - QtScript component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
Patch100: qtscript-everywhere-src-5.12.1-s390.patch
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Provides: bundled(javascriptcore) = 0~snapshot110127
%if ! 0%{?bootstrap}
%endif
%if 0%{?tests}
%endif
# oreon:deps
BuildRequires:  dbus-x11
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mesa-dri-drivers
BuildRequires:  pkgconfig(Qt5UiTools)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  time
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-private-devel = %{version}-%{release}
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
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1

#patch100 -p1 -b .s390

%build

%define _lto_cflags %{nil}
%qmake_qt5
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
sed -i \
  -e "/^QMAKE_PRL_BUILD_DIR/d" \
  -e "/^QMAKE_PRL_LIBS/d" \
  %{buildroot}%{_qt5_libdir}/*.prl
rm -fv %{buildroot}%{_qt5_libdir}/lib*.la
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
export PATH=%{buildroot}%{_qt5_bindir}:$PATH
export LD_LIBRARY_PATH=%{buildroot}%{_qt5_libdir}
%make_build -k sub-tests-all ||:
timeout 180 \
xvfb-run -a \
time \
%make_build check -k -C tests ||:
if [ "$?" -eq "124" ]; then
echo 'make check timeout reached!'
exit 1
fi
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n qt5-qtscript-devel -f %{oreon_filedir}/qt5-qtscript-devel.list
%files -n qt5-qtscript-examples -f %{oreon_filedir}/qt5-qtscript-examples.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import

%global source0_hash a8e6358a31c44ccdf1bfc46c95a77a6bfc7fc1f536aadb913ed4f4405c570cf6
%global with_qt4 1
%global ubuntu 16.04
%global snapshot 20160218
%global tarballversion 0.9.2
%global __cmake_in_source_build 1
Summary:        A Qt implementation of the DBusMenu protocol
Name:    dbusmenu-qt
Version: 0.9.3
Release:        1%{?dist}
License: LGPL-2.0-or-later
URL: https://launchpad.net/libdbusmenu-qt/
%if 0%{?snapshot}
Source0:        https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/lib%{name}/%{version}+%{ubuntu}.%{snapshot}-0ubuntu%{with_qt4}/lib%{name}_%{version}+%{ubuntu}.%{snapshot}.orig.tar.gz
%else
%endif
%if 0%{?with_qt4}
%endif
Provides: libdbusmenu-qt = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  dbus-x11
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(QJson)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(QtDBus)
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  xorg-x11-server-Xvfb
# /oreon:deps
%description
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%if 0%{?with_qt4}
%endif
%package devel
Summary: Development files for %{name}
Provides: libdbusmenu-qt-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package doc
Summary: Development and API documentation for %{name}
BuildArch: noarch
Conflicts: dbusmenu-qt-devel < 0.9.3
%description doc
%{summary}.

%package -n dbusmenu-qt5
Summary: A Qt implementation of the DBusMenu protocol
Provides: libdbusmenu-qt5 = %{version}-%{release}
%description -n dbusmenu-qt5
This library provides a Qt5 implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%package -n dbusmenu-qt5-devel
Summary: Development files for dbusmenu-qt5
Provides: libdbusmenu-qt5-devel = %{version}-%{release}
Requires: dbusmenu-qt5%{?_isa} = %{version}-%{release}
%description -n dbusmenu-qt5-devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n libdbusmenu-qt-%{version}+%{ubuntu}.%{snapshot}

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%if 0%{?with_qt4}
mkdir %{_target_platform}
pushd %{_target_platform}
%cmake .. \
  -DUSE_QT4:BOOL=ON \
  -DUSE_QT5:BOOL=OFF \
  -DWITH_DOC:BOOL=ON
popd
%make_build -C %{_target_platform}
%endif
mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%cmake .. \
  -DUSE_QT4:BOOL=OFF \
  -DUSE_QT5:BOOL=ON \
  -DWITH_DOC:BOOL=OFF
popd
%ninja_build -C %{_target_platform}-qt5
%install
%if 0%{?with_qt4}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%endif
%ninja_install -C %{_target_platform}-qt5
rm -rfv %{buildroot}%{_docdir}/libdbusmenu-qt*-doc
%oreon_autofiles dbusmenu-qt-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles dbusmenu-qt-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dbusmenu-qt5 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles dbusmenu-qt5-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
%if 0%{?with_qt4}
test "$(pkg-config --modversion dbusmenu-qt)" = "%{tarballversion}"
%endif
test "$(pkg-config --modversion dbusmenu-qt5)" = "%{tarballversion}"
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a dbus-launch --exit-with-session make -C %{_target_platform} check ARGS="--output-on-failure --timeout 300" ||:
%if 0%{?with_qt4}
%ldconfig_scriptlets
%endif
%files -f %{oreon_filedir}/main.list
%files -n dbusmenu-qt-devel -f %{oreon_filedir}/dbusmenu-qt-devel.list
%files -n dbusmenu-qt-doc -f %{oreon_filedir}/dbusmenu-qt-doc.list
%files -n dbusmenu-qt5 -f %{oreon_filedir}/dbusmenu-qt5.list
%files -n dbusmenu-qt5-devel -f %{oreon_filedir}/dbusmenu-qt5-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.3-0.40.20160218
- Import

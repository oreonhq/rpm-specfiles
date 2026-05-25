%global with_qt4 1
%if 0%{?rhel} || 0%{?oreon}
%global with_qt4 0
%endif

%global ubuntu 16.04
%global snapshot 20160218
# FIXME?  pkg-config files still report as 0.9.2
%global tarballversion 0.9.2

# set this until when/if we port to new cmake macros
%global __cmake_in_source_build 1

Summary: A Qt implementation of the DBusMenu protocol 
Name:    dbusmenu-qt
Version: 0.9.3
Release: 0.40.%{snapshot}%{?dist}

License: LGPL-2.0-or-later
URL: https://launchpad.net/libdbusmenu-qt/
%if 0%{?snapshot}
# bzr branch lp:libdbusmenu-qt && cd libdbusmenu-qt && bzr export --root=libdbusmenu-qt-%{version}-%{snapshot}bzr.tar.gz
#Source0:  libdbusmenu-qt-%{version}-%{snapshot}bzr.tar.gz
Source0:  https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/libdbusmenu-qt/%{version}+%{ubuntu}.%{snapshot}-0ubuntu1/libdbusmenu-qt_%{version}+%{ubuntu}.%{snapshot}.orig.tar.gz
%else
Source0:  https://launchpad.net/libdbusmenu-qt/trunk/%{version}/+download/libdbusmenu-qt-%{version}.tar.bz2
%endif


## upstream patches

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: pkgconfig
%if 0%{?with_qt4}
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtGui)
%endif # with_qt4
BuildRequires: pkgconfig(Qt5DBus) pkgconfig(Qt5Widgets)
# test-suite
BuildRequires: xorg-x11-server-Xvfb dbus-x11
BuildRequires: make

Provides: libdbusmenu-qt = %{version}-%{release}

%description
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.

%if 0%{?with_qt4}
%package devel
Summary: Development files for %{name}
Provides: libdbusmenu-qt-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package doc
Summary: Development and API documentation for %{name}
BuildArch: noarch
# when -doc content was moved here
Conflicts: dbusmenu-qt-devel < 0.9.3
%description doc
%{summary}.
%endif # with_qt4

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
%autosetup -n libdbusmenu-qt-%{version}+%{ubuntu}.%{snapshot}


%build
# TODO: Please submit an issue to upstream (rhbz#2380533)
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
%endif # with_qt4

mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%cmake .. \
  -DUSE_QT4:BOOL=OFF \
  -DUSE_QT5:BOOL=ON \
  -DWITH_DOC:BOOL=OFF

popd

%make_build -C %{_target_platform}-qt5


%install
%if 0%{?with_qt4}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%endif # with_qt4
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5

# unpackaged files
rm -rfv %{buildroot}%{_docdir}/libdbusmenu-qt*-doc


%check
# verify pkg-config version
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
%if 0%{?with_qt4}
test "$(pkg-config --modversion dbusmenu-qt)" = "%{tarballversion}"
%endif # with_qt4
test "$(pkg-config --modversion dbusmenu-qt5)" = "%{tarballversion}"
# test suite
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a dbus-launch --exit-with-session make -C %{_target_platform} check ARGS="--output-on-failure --timeout 300" ||:


%if 0%{?with_qt4}
%ldconfig_scriptlets

%files
%doc README
%license COPYING
%{_libdir}/libdbusmenu-qt.so.2*

%files devel
%doc %{_target_platform}/html/
%{_includedir}/dbusmenu-qt/
%{_libdir}/libdbusmenu-qt.so
%{_libdir}/cmake/dbusmenu-qt/
%{_libdir}/pkgconfig/dbusmenu-qt.pc

%files doc
%doc %{_target_platform}/html/
%endif # with_qt4

%ldconfig_scriptlets -n dbusmenu-qt5

%files -n dbusmenu-qt5
%doc README
%license COPYING
%{_libdir}/libdbusmenu-qt5.so.2*

%files -n dbusmenu-qt5-devel
%{_includedir}/dbusmenu-qt5/
%{_libdir}/libdbusmenu-qt5.so
%{_libdir}/pkgconfig/dbusmenu-qt5.pc
%{_libdir}/cmake/dbusmenu-qt5/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.9.3-0.40.20160218
- Import

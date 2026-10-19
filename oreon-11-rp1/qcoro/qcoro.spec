%global source0_hash 4bff7513c5c8e301b66308df05795043b1792ed16381a484e5c990171b8ff19e
%global use_qt5 %[!(0%{?rhel} >= 11)]
%global use_qt6 1
%global appname QCoro
%global qt5_build_dir release-qt5
%global qt6_build_dir release-qt6
Name: qcoro
Version: 0.13.0
Release:        1%{?dist}
License: MIT
Summary:        C++ Coroutines for Qt
URL: https://github.com/danvratil/%{name}
Source0:        https://github.com/danvratil/qcoro/archive/refs/tags/v%{version}.tar.gz#/qcoro-%{version}.tar.gz
%if 0%{?use_qt5}
%endif
%if 0%{?use_qt6}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5WebSockets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  dbus-x11
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description

%if 0%{?use_qt5}
%package qt5
Summary: C++ Coroutines for Qt 5
Provides: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name} < %{?epoch:%{epoch}:}%{version}-%{release}
%package qt5-devel
Summary: Development files for %{appname} (Qt 5 version)
Requires: %{name}-qt5%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
Provides: %{name}-devel = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: %{name}-devel < %{?epoch:%{epoch}:}%{version}-%{release}
%description qt5
%description qt5-devel
%endif

%if 0%{?use_qt6}
%package qt6
Summary: C++ Coroutines for Qt 6
%package qt6-devel
Summary: Development files for %{appname} (Qt 6 version)
Requires: %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description qt6
%description qt6-devel
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if 0%{?use_qt5}
mkdir %{qt5_build_dir} && pushd %{qt5_build_dir}
%cmake -G Ninja \
    -S'..' \
    -DCMAKE_BUILD_TYPE=Release \
    -DECM_MKSPECS_INSTALL_DIR=%{_libdir}/qt5/mkspecs/modules \
    -DUSE_QT_VERSION:STRING=5 \
    -DBUILD_TESTING:BOOL=ON \
    -DQCORO_BUILD_EXAMPLES:BOOL=ON \
    -DQCORO_ENABLE_ASAN:BOOL=OFF \
    -DQCORO_WITH_QML:BOOL=ON \
    -DQCORO_WITH_QTDBUS:BOOL=ON \
    -DQCORO_WITH_QTNETWORK:BOOL=ON \
    -DQCORO_WITH_QTQUICK:BOOL=ON \
    -DQCORO_WITH_QTWEBSOCKETS:BOOL=ON
%cmake_build
popd
%endif
%if 0%{?use_qt6}
mkdir %{qt6_build_dir} && pushd %{qt6_build_dir}
%cmake -G Ninja \
    -S'..' \
    -DCMAKE_BUILD_TYPE=Release \
    -DECM_MKSPECS_INSTALL_DIR=%{_libdir}/qt6/mkspecs/modules \
    -DUSE_QT_VERSION:STRING=6 \
    -DBUILD_TESTING:BOOL=ON \
    -DQCORO_BUILD_EXAMPLES:BOOL=ON \
    -DQCORO_ENABLE_ASAN:BOOL=OFF \
    -DQCORO_WITH_QML:BOOL=ON \
    -DQCORO_WITH_QTDBUS:BOOL=ON \
    -DQCORO_WITH_QTNETWORK:BOOL=ON \
    -DQCORO_WITH_QTQUICK:BOOL=ON \
    -DQCORO_WITH_QTWEBSOCKETS:BOOL=ON
%cmake_build
popd
%endif
%install
%if 0%{?use_qt5}
pushd %{qt5_build_dir}
%cmake_install
popd
%endif
%if 0%{?use_qt6}
pushd %{qt6_build_dir}
%cmake_install
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

%if 0%{?use_qt5}
pushd %{qt5_build_dir}
%ctest --timeout 3600
popd
%endif
%if 0%{?use_qt6}
pushd %{qt6_build_dir}
%ctest --timeout 3600 -E networkreply
popd
%endif
%if 0%{?use_qt5}
%files -f %{oreon_filedir}/main.list
%files -n qcoro-qt5 -f %{oreon_filedir}/qcoro-qt5.list
%files -n qcoro-qt5-devel -f %{oreon_filedir}/qcoro-qt5-devel.list
%files -n qcoro-qt6 -f %{oreon_filedir}/qcoro-qt6.list
%files -n qcoro-qt6-devel -f %{oreon_filedir}/qcoro-qt6-devel.list

%changelog

%autochangelog
%endif

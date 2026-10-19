%global source0_hash e44ed8d5a9618b3ca7ba2983ed9c5f7572e6e0a5b199f94868834b71ccbebd43
%bcond qt5 1
%bcond qt6 1
%global appname FutureSQL
%global qt5_build_dir release-qt5
%global qt6_build_dir release-qt6
Name:    futuresql
Version: 0.1.1
Release:        1%{?dist}
License: (LGPL-2.1-only OR LGPL-3.0-only) AND BSD-2-Clause
Summary:        Non-blocking database framework for Qt
URL:     https://invent.kde.org/libraries/futuresql/
Source0:        https://download.kde.org/stable/futuresql/%{name}-%{version}.tar.xz
%if %{with qt5}
%endif
%if %{with qt6}
%endif
# oreon:deps
BuildRequires:  cmake(QCoro5Core)
BuildRequires:  cmake(QCoro6Core)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description

%if %{with qt5}
%package qt5
Summary: Non-blocking database framework for Qt 5
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

%if %{with qt6}
%package qt6
Summary: Non-blocking database framework for Qt 6
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

%if %{with qt5}
mkdir %{qt5_build_dir} && pushd %{qt5_build_dir}
%cmake -G Ninja \
    -S .. \
    -DBUILD_WITH_QT6:BOOL=OFF \
    -DBUILD_EXAMPLES:BOOL=ON \
    -DBUILD_TESTING:BOOL=ON
%cmake_build
popd
%endif
%if %{with qt6}
mkdir %{qt6_build_dir} && pushd %{qt6_build_dir}
%cmake -G Ninja \
    -S .. \
    -DBUILD_WITH_QT6:BOOL=ON \
    -DBUILD_EXAMPLES:BOOL=OFF \
    -DBUILD_TESTING:BOOL=ON
%cmake_build
popd
%endif
%install
%if %{with qt5}
pushd %{qt5_build_dir}
%cmake_install
popd
%endif
%if %{with qt6}
pushd %{qt6_build_dir}
%cmake_install
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

%if %{with qt5}
pushd %{qt5_build_dir}
%ctest --timeout 3600
popd
%endif
%if %{with qt6}
pushd %{qt6_build_dir}
%ctest --timeout 3600
popd
%endif
%if %{with qt5}
%files -f %{oreon_filedir}/main.list
%files -n futuresql-qt5 -f %{oreon_filedir}/futuresql-qt5.list
%files -n futuresql-qt5-devel -f %{oreon_filedir}/futuresql-qt5-devel.list
%files -n futuresql-qt6 -f %{oreon_filedir}/futuresql-qt6.list
%files -n futuresql-qt6-devel -f %{oreon_filedir}/futuresql-qt6-devel.list

%changelog

%autochangelog
%endif

%global source0_hash ac0fe5df480fa893d3e16da626bf5028c944e9b41f504f6fe0fe49273247d636
%global appname Quotient
%global libname lib%{appname}
Name: libquotient
Version: 0.9.6.1
Release:        1%{?dist}
License: BSD-3-Clause AND LGPL-2.1-or-later
URL: https://github.com/quotient-im/%{libname}
Summary:        Qt library to write cross-platform clients for Matrix
Source0:        https://github.com/quotient-im/%{libname}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Olm)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(openssl)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description

%package qt6
Summary: Files for qt6
Obsoletes: %{name}-qt5 < 0.9.0
%description qt6

%package qt6-devel
Summary: Development files for %{name} for qt6
Requires: %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: cmake(Olm)
Requires: cmake(Qt6Keychain)
Requires: cmake(Qt6Sql)
Requires: pkgconfig(openssl)
Obsoletes: %{name}-qt5-devel < 0.9.0
%description qt6-devel

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{libname}-%{version}
rm -rf 3rdparty

%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir}/%{appname}Qt6 \
    -DQuotient_ENABLE_E2EE:BOOL=ON \
    -DQuotient_INSTALL_TESTS:BOOL=OFF \
    -DQuotient_INSTALL_EXAMPLE:BOOL=OFF \
    -DBUILD_WITH_QT6=ON
%cmake_build
%check

%ctest --exclude-regex 'testolmaccount|testkeyverification'
%install
%cmake_install
rm -rf %{buildroot}%{_datadir}/ndk-modules
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libquotient-qt6 -f %{oreon_filedir}/libquotient-qt6.list
%files -n libquotient-qt6-devel -f %{oreon_filedir}/libquotient-qt6-devel.list

%changelog

%autochangelog


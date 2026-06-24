%global source0_hash none

%global appname Quotient
%global libname lib%{appname}
%global _description %{expand:
The Quotient project aims to produce a Qt-based SDK to develop applications
for Matrix. libQuotient is a library that enables client applications. It is
the backbone of Quaternion, Spectral and other projects. Versions 0.5.x and
older use the previous name - libQMatrixClient.}

Name: libquotient
Version: 0.9.5
Release: 5%{?dist}

License: BSD-3-Clause AND LGPL-2.1-or-later
URL: https://github.com/quotient-im/%{libname}
Summary: Qt library to write cross-platform clients for Matrix
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake(Olm)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: pkgconfig(openssl)
BuildRequires: qt6-qtbase-private-devel

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description %_description

%package qt6
Summary: Files for qt6
Obsoletes: %{name}-qt5 < 0.9.0
%description qt6 %_description

%package qt6-devel
Summary: Development files for %{name} for qt6
Requires: %{name}-qt6%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: cmake(Olm)
Requires: cmake(Qt6Keychain)
Requires: cmake(Qt6Sql)
Requires: pkgconfig(openssl)
Obsoletes: %{name}-qt5-devel < 0.9.0
%description qt6-devel %_description

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

%files qt6
%license COPYING
%doc README.md CONTRIBUTING.md SECURITY.md
%{_libdir}/%{libname}Qt6.so.0*

%files qt6-devel
%{_includedir}/%{appname}Qt6/
%{_libdir}/cmake/%{appname}Qt6/
%{_libdir}/%{libname}Qt6.so
%{_libdir}/pkgconfig/%{appname}Qt6.pc

%changelog
%autochangelog


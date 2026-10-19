%global source0_hash 9322b30c085cc8de12b51ad022ed877eea6f332deafb094c020b94292871278f
%global debug_package %{nil}
%global commit bb474a201baa798784d696d2d9d762a9d2807f96
Name: tde2e
Version: 1.8.51
Release:        1%{?dist}
License: BSL-1.0 AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL: https://github.com/tdlib/td
Summary:        Cross-platform library for building Telegram clients
Source0:        https://github.com/tdlib/td/archive/%{commit}/tdlib-%{version}.tar.gz
ExcludeArch:    %{ix86} s390x
# oreon:deps
BuildRequires:  abseil-cpp-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  google-crc32c-devel
BuildRequires:  gperf
BuildRequires:  gperftools-devel
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
TDE2E is a cross-platform library for building Telegram clients.

%package devel
Summary: Cross-platform library for building Telegram clients
Provides:   %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Conflicts:  tdlib-devel
Conflicts:  tdlib-static
%description devel
TDE2E is a cross-platform library for building Telegram clients.
Contains development files and static libraries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n td-%{commit} -p1

%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DBUILD_TESTING:BOOL=OFF \
    -DTD_ENABLE_JNI:BOOL=OFF \
    -DTD_ENABLE_DOTNET:BOOL=OFF \
    -DTD_WITH_ABSEIL:BOOL=ON \
    -DTD_E2E_ONLY:BOOL=ON \
    -DTDE2E_ENABLE_INSTALL:BOOL=ON \
    -DTDE2E_INSTALL_INCLUDES:BOOL=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n tde2e-devel -f %{oreon_filedir}/tde2e-devel.list

%changelog

%autochangelog

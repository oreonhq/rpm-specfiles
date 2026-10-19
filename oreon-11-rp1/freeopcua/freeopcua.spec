%global source0_hash 329d658fbbf404dbd6c4841f4bd247ab30b5c784b6a3d3f62cbec09d120c798c
%global commit bd13aee2455c1d137bee45f7d2aedea8dd30115c
%global snapdate 20220717
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           freeopcua
Version:        0
Release:        1%{?dist}
Summary:        Open Source C++ OPC-UA Server and Client Library
License:        LGPL-3.0-or-later
URL:            http://freeopcua.github.io/
Source0:        https://github.com/FreeOpcUa/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         freeopcua.build-flags.patch
Patch1:         freeopcua.catch-exception-in-destructor.patch
Patch2:         freeopcua.set-soversion.patch
Patch3:         freeopcua-fmt9-formatter.patch
Patch4:         freeopcua-fmt10-fmt-format.patch
Patch5:         freeopcua-gcc14-headers.patch
Patch6:         freeopcua.cmake-version.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  spdlog-devel
# /oreon:deps
%description
A LGPL C++ library to develop server and client OPC-UA applications.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   spdlog-devel
%description  devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

# Remove bundled spdlog
rm -rf include/opc/spdlog

%build

%cmake -DCMAKE_INSTALL_LIBDIR=%{?_lib} -DSSL_SUPPORT_MBEDTLS=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n freeopcua-devel -f %{oreon_filedir}/freeopcua-devel.list

%changelog

%autochangelog

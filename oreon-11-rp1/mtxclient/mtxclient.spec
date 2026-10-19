%global source0_hash 203be46a08e1dc6cfc068d0911f3b09976f48e4cc4302c3517b9c0f4e53631e3
Name: mtxclient
Version: 0.10.1
Release:        1%{?dist}
License: MIT
Summary:        Client API library for Matrix, built on top of Boost.Asio
URL: https://github.com/Nheko-Reborn/%{name}
Source0:        https://github.com/Nheko-Reborn/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Olm)
BuildRequires:  cmake(fmt)
BuildRequires:  cmake(mpark_variant)
BuildRequires:  cmake(nlohmann_json)
BuildRequires:  cmake(spdlog)
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(coeurl)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Client API library for the Matrix protocol, built on top of Boost.Asio.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DHUNTER_ENABLED:BOOL=OFF \
    -DUSE_BUNDLED_COEURL:BOOL=OFF \
    -DUSE_BUNDLED_GTEST:BOOL=OFF \
    -DUSE_BUNDLED_JSON:BOOL=OFF \
    -DUSE_BUNDLED_LIBCURL:BOOL=OFF \
    -DUSE_BUNDLED_LIBEVENT:BOOL=OFF \
    -DUSE_BUNDLED_OLM:BOOL=OFF \
    -DUSE_BUNDLED_OPENSSL:BOOL=OFF \
    -DUSE_BUNDLED_SPDLOG:BOOL=OFF \
    -DASAN:BOOL=OFF \
    -DCOVERAGE:BOOL=OFF \
    -DIWYU:BOOL=OFF \
    -DBUILD_LIB_TESTS:BOOL=OFF \
    -DBUILD_LIB_EXAMPLES:BOOL=OFF
%cmake_build
%install
%cmake_install
ln -s libmatrix_client.so.%{version} %{buildroot}%{_libdir}/libmatrix_client.so.0
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mtxclient-devel -f %{oreon_filedir}/mtxclient-devel.list

%changelog

%autochangelog

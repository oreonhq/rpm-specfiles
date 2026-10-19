%global source0_hash 6742551505cc6b6b387279353627a27a93a3461b34284ba94666c365ad6cfcfd
%global _cmake_shared_libs %{nil}
Name:           cryfs
Version:        1.0.3
Release:        1%{?dist}
Summary:        Cryptographic filesystem for the cloud
License:        LGPL-3.0-only
URL:            https://www.cryfs.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Include-stdexcept-when-using-logic_error.patch
Patch1:         0002-Fix-versioneer-compatibility-with-Python-312.patch
Patch2: cryfs-boost-process-v1.patch
ExcludeArch: i686
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(range-v3)
BuildRequires:  cmake(spdlog)
BuildRequires:  cryptopp-devel
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  python3
BuildRequires:  python3-versioneer
# /oreon:deps
%description
CryFS provides a FUSE-based mount that encrypts file contents, file
sizes, metadata and directory structure. It uses encrypted same-size
blocks to store both the files themselves and the blocks' relations
to one another. These blocks are stored as individual files in the
base directory, which can then be synchronized to remote storage
(using an external tool).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
    -G Ninja \
    -DDEPENDENCY_CONFIG=./cmake-utils/DependenciesFromLocalSystem.cmake \
    -DBUILD_TESTING=OFF \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
    -DCRYFS_UPDATE_CHECKS=OFF \
    -DCMAKE_BUILD_TYPE=Release \
    -DBoost_USE_STATIC_LIBS=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

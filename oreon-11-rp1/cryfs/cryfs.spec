%global source0_hash 0dacf667a6de6ba5161872e1c82426cbd6dbfb6bb6c3ce6fbb12aafd725b471b

# The shared libraries are useless
%global _cmake_shared_libs %{nil}

Name:           cryfs
Version:        0.11.3
Release:        15%{?dist}
Summary:        Cryptographic filesystem for the cloud
# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:        LGPL-3.0-only
URL:            https://www.cryfs.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Add a missing stdexcept include to fix build
# https://github.com/cryfs/cryfs/pull/448
# https://bugzilla.redhat.com/show_bug.cgi?id=2171464
Patch0:         0001-Include-stdexcept-when-using-logic_error.patch
# https://github.com/cryfs/cryfs/issues/459
Patch1:         0002-Fix-versioneer-compatibility-with-Python-312.patch
# Need to use Boost.Process v1 for Boost 1.90.0
Patch2: cryfs-boost-process-v1.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  boost-devel

BuildRequires:  cryptopp-devel

BuildRequires:  python3
BuildRequires:  python3-versioneer

BuildRequires:  cmake(range-v3)
BuildRequires:  cmake(spdlog)
BuildRequires:  pkgconfig(fuse)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libssl)

# Required library doesn't exist
ExcludeArch: i686

%description
CryFS provides a FUSE-based mount that encrypts file contents, file
sizes, metadata and directory structure. It uses encrypted same-size
blocks to store both the files themselves and the blocks' relations
to one another. These blocks are stored as individual files in the
base directory, which can then be synchronized to remote storage
(using an external tool).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

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

%files
%license LICENSE.txt
%doc README.md ChangeLog.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-unmount
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog

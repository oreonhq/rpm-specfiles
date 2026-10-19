%global source0_hash 4f462f51a3468166ea4cf87c80e001dc1999093264cf55cbda3492ca39a7730b
%global debug_package %{nil}
Name:           parallel-hashmap
Version:        2.0.0
Release:        1%{?dist}
Summary:        Family of header-only hashmap and btree containers
License:        Apache-2.0
URL:            https://github.com/greg7mdp/parallel-hashmap
Source0:        https://github.com/greg7mdp/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          0001-CMakeLists.txt-use-external-gtest-fallback-to-fetching-the-source-288.patch
Patch:          0002-Download-gtest-unless-PHMAP_DOWNLOAD_GTEST-is-turned-off.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
# /oreon:deps
%description
This repository aims to provide a set of excellent hash map implementations, as
well as a btree alternative to std::map and std::set.

%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch
%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%conf
%cmake \
    -DPHMAP_DOWNLOAD_GTEST=OFF \
    -DPHMAP_BUILD_EXAMPLES=OFF

%build

%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n parallel-hashmap-devel -f %{oreon_filedir}/parallel-hashmap-devel.list

%changelog

%autochangelog

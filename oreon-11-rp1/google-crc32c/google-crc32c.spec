%global source0_hash ac07840513072b7fcebda6e821068aa04889018f24e10e46181068fb214d7e56
%bcond_with tests
%global         srcname     google-crc32c
%global         reponame    crc32c
%global         forgeurl    https://github.com/google/%{reponame}
Version:        1.1.2
%global         tag         %{version}
%forgemeta -a
Name:           %{srcname}
Release:        1%{?dist}
License:        BSD-3-Clause
Summary:        CRC32C implementation with support for CPU-specific acceleration instructions
Url:            %forgeurl
Source0:        %{forgeurl}/archive/%{version}/%{reponame}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
# /oreon:deps
%description
This project collects a few CRC32C implementations under an umbrella that
dispatches to a suitable implementation based on the host computer's hardware
capabilities. CRC32C is specified as the CRC that uses the iSCSI polynomial in
RFC 3720. The polynomial was introduced by G. Castagnoli, S. Braeuer and M.
Herrmann. CRC32C is used in software such as Btrfs, ext4, Ceph and leveldb.

%package devel
Summary:        Development files for %{srcname}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{srcname}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{reponame}-%{version}

%build

%cmake \
    -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
    -DCMAKE_BUILD_TYPE=Release \
    -DCRC32C_BUILD_BENCHMARKS=OFF \
    -DCRC32C_BUILD_TESTS=OFF \
    -DCRC32C_USE_GLOG=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with tests}
%check

%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n google-crc32c-devel -f %{oreon_filedir}/google-crc32c-devel.list

%changelog

%autochangelog

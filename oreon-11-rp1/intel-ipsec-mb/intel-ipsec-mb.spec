%global source0_hash b0e22e113ebbaa4aa8fd2332897540bff87bfabf397daeb05301b603947dda83
%global major 2
%global minor 0
%global patch 2
%global desc %{expand: \
Intel Multi-Buffer Crypto for IPsec Library is highly-optimized software
implementations of the core cryptographic processing for IPsec, which provides
industry-leading performance on a range of Intel Processors.}
Name:               intel-ipsec-mb
Version:            2.0.2
Release:        1%{?dist}
Summary:        IPsec cryptography library optimized for Intel Architecture
License:            BSD-3-Clause
URL:                https://github.com/intel/intel-ipsec-mb
Source0:        https://github.com/intel/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:      x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  nasm
# /oreon:deps
%description
%{desc}

%package -n intel-ipsec-mb-devel
Summary:            Development files for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
%description devel %{desc}

Development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
sed -i 's|man/man7|share/man/man7|g' lib/cmake/unix.cmake

%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles intel-ipsec-mb-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n intel-ipsec-mb-devel -f %{oreon_filedir}/intel-ipsec-mb-devel.list

%changelog

%autochangelog


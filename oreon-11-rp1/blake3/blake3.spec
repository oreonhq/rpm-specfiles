%global source0_hash c6782a28842b1c0478524ac06a4f2ede784038ee298d6e2162c0b089c4306a3c
%global needs_gcc_toolset 0%{?el8} || 0%{?el9}
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%bcond_without tbb
%else
%bcond_with tbb
%endif
Name:           blake3
Version:        1.8.7
Release:        1%{?dist}
Summary:        Official C implementation of the BLAKE3 cryptographic hash function
License:        Apache-2.0
URL:            https://github.com/BLAKE3-team/BLAKE3/
Source0:        https://github.com/BLAKE3-team/BLAKE3//archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         0001-Fix-building-the-test-application-on-non-x86-machine.patch
%if %{needs_gcc_toolset}
%else
%endif
%if %{with tbb}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libasan
BuildRequires:  libubsan
BuildRequires:  python3
BuildRequires:  tbb-devel
# /oreon:deps
%description
BLAKE3 is a cryptographic hash function that is:
- Much faster than MD5, SHA-1, SHA-2, SHA-3, and BLAKE2.
- Secure, unlike MD5 and SHA-1. And secure against length extension, unlike
  SHA-2.
- Highly parallelizable across any number of threads and SIMD lanes, because
  it's a Merkle tree on the inside.
- Capable of verified streaming and incremental updates, again because it's a
  Merkle tree.
- A PRF, MAC, KDF, and XOF, as well as a regular hash.
- One algorithm with no variants, which is fast on x86-64 and also on smaller
  architectures.

%package devel
Summary: %{summary} - development files
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Development files for the %{name} library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir BLAKE3-%{version}
%oreon_prep
%build

export ASMFLAGS="%{build_cflags}"
%if %{needs_gcc_toolset}
. /opt/rh/gcc-toolset-14/enable
%endif
cd c
%cmake \
%if 0%{with tbb}
  -DBLAKE3_USE_TBB=ON
%endif
%cmake_build
%check

%ifnarch x86_64
%define non_x86_64_flags BLAKE3_NO_SSE2=1 BLAKE3_NO_SSE41=1 BLAKE3_NO_AVX2=1 BLAKE3_NO_AVX512=1
%endif
%ifarch %{arm32} aarch64
%define arm_flags %{?flags} BLAKE3_USE_NEON=1
%endif
%if %{needs_gcc_toolset}
. /opt/rh/gcc-toolset-14/enable
%endif
cd c
%make_build %{?non_x86_64_flags} %{?arm_flags} -f Makefile.testing test
%make_build %{?non_x86_64_flags} BLAKE3_NO_NEON=1 -f Makefile.testing test_asm
%install
cd c
%cmake_install
%oreon_autofiles blake3-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n blake3-devel -f %{oreon_filedir}/blake3-devel.list

%changelog

%autochangelog


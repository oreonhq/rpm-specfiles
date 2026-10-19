%global source0_hash 46c60960e283ead6f386c1fa6084914a5bc9624f37f16357e77dc74fb59844d4
%global debug_package %{nil}
%global srctag ippcp_2021.10.0
%global mbx_int_major 11
%global mbx_int_minor 11
%global desc %{expand: \
Intel IPP Cryptography library provides optimized versions of RSA, ECDSA, ECDH
and x25519 multi-buffer algorithms based on Intel Advanced Vector Extensions 
512 (Intel AVX-512) integer fused multiply-add (IFMA) operations. SM4 based on
Intel Advanced Vector Extensions 512 (Intel AVX-512) GFNI and SM3 based on 
Intel Advanced Vector Extensions 512 (Intel AVX-512) instructions.}
Name:		intel-ipp-crypto-mb
Version:	1.0.10
Release:        1%{?dist}
Summary:        Intel IPP Cryptography multi-buffer library
License:	Apache-2.0
URL:		https://github.com/intel/ipp-crypto
Source0:        https://github.com/intel/ipp-crypto/archive/%{srctag}/%{name}-%{srctag}.tar.gz
ExclusiveArch:	x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel
# /oreon:deps
%description
%{desc}

%package devel
Summary: Development files for %{name}
Provides:	%{name}-static = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel %{desc}

Development files.

%package static
Summary: Static libraries for %{name} development
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description static %{desc}

Static library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cryptography-primitives-%{srctag}
# library path fix
sed -i 's/"lib\"/"lib64"/g' sources/ippcp/crypto_mb/src/CMakeLists.txt

%build

pushd sources/ippcp/crypto_mb
%cmake \
	-DARCH=intel64 \
	-DMERGED_BLD:BOOL=off \
	-DCMAKE_C_FLAGS="%{build_cflags} -Wno-error=unused-but-set-variable" \
	-DCMAKE_CXX_FLAGS="%{build_cxxflags} -Wno-error=unused-but-set-variable"
%cmake_build
popd
%install
pushd sources/ippcp/crypto_mb
%cmake_install
popd
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n intel-ipp-crypto-mb-devel -f %{oreon_filedir}/intel-ipp-crypto-mb-devel.list
%files -n intel-ipp-crypto-mb-static -f %{oreon_filedir}/intel-ipp-crypto-mb-static.list

%changelog

%autochangelog

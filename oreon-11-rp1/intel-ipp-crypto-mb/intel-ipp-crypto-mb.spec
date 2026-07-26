%global source0_hash 5152fbcac11a52a20858780a87b4e9f759250cabf4c1b054a9379b001511c15c

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
Release:	6%{?dist}
Summary:	Intel IPP Cryptography multi-buffer library

License:	Apache-2.0
URL:		https://github.com/intel/ipp-crypto
Source0:	%{url}/archive/%{srctag}/%{name}-%{srctag}.tar.gz

# Upstream exclusively uses x86_64-specific intrinsics
ExclusiveArch:	x86_64

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	openssl-devel >= 1.1.0

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

%autosetup -n ipp-crypto-%{srctag}
# library path fix
sed -i 's/"lib\"/"lib64"/g' sources/ippcp/crypto_mb/src/CMakeLists.txt

%build
pushd sources/ippcp/crypto_mb
%cmake \
	-DARCH=intel64 \
	-DMERGED_BLD:BOOL=off
%cmake_build
popd

%install
pushd sources/ippcp/crypto_mb
%cmake_install
popd

%ldconfig_scriptlets

%files
%license LICENSE
%doc sources/ippcp/crypto_mb/Readme.md
%{_libdir}/libcrypto_mb.so.%{mbx_int_major}
%{_libdir}/libcrypto_mb.so.%{mbx_int_major}.%{mbx_int_minor}

%files devel
%{_includedir}/crypto_mb
%{_libdir}/libcrypto_mb.so

%files static
%license LICENSE
%{_libdir}/libcrypto_mb.a

%changelog
%autochangelog

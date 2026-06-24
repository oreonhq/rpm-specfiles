%global source0_hash none

# Versions numbers
%global major 2
%global minor 0
%global patch 2

%global desc %{expand: \
Intel Multi-Buffer Crypto for IPsec Library is highly-optimized software
implementations of the core cryptographic processing for IPsec, which provides
industry-leading performance on a range of Intel Processors.}

Name:               intel-ipsec-mb
Version:            2.0.2
Release:            1%{?dist}
Summary:            IPsec cryptography library optimized for Intel Architecture

License:            BSD-3-Clause
URL:                https://github.com/intel/intel-ipsec-mb
Source0:            %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

ExclusiveArch:      x86_64

BuildRequires:      cmake
BuildRequires:      gcc
BuildRequires:      gcc-c++
BuildRequires:      nasm >= 2.14

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

%check
%ctest

%ldconfig_scriptlets

%files
%license LICENSE
%doc README.md ReleaseNotes.txt
%{_libdir}/libIPSec_MB.so.%{major}
%{_libdir}/libIPSec_MB.so.%{major}.%{minor}.%{patch}
%{_mandir}/man7/libipsec-mb.*

%files -n %{name}-devel
%{_includedir}/intel-ipsec-mb.h
%{_libdir}/libIPSec_MB.so
%{_mandir}/man7/libipsec-mb-dev.*

%changelog
%autochangelog


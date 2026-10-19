%global source0_hash df999915204eb1eba311d89e83d1edd3a514d5a07374745d6a9e5b2dd0d59c08
%global oqs_version 0.12.0
Name:       liboqs
Version:    %{oqs_version}
Release:        1%{?dist}
Summary:        liboqs is an open source C library for quantum-safe cryptographic algorithms.
License:    MIT AND Apache-2.0 AND BSD-3-Clause AND (BSD-3-Clause OR GPL-1.0-or-later) AND CC0-1.0 AND Unlicense
URL:        https://github.com/open-quantum-safe/liboqs.git
Source0:        https://github.com/open-quantum-safe/liboqs/archive/refs/tags/%{version}.tar.gz#/liboqs-%{version}.tar.gz
Patch1:	    liboqs-0.12.0-acvp_patch.patch
Patch2:	    liboqs-0.10.0-std-stricter.patch
Patch3:	    liboqs-0.12.0-openssl-memfuncs.patch
%if %{undefined rhel} || (0%{?oreon} >= 11)
%endif
%ifarch %{valgrind_arches}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-yaml
BuildRequires:  unzip
BuildRequires:  xsltproc
# /oreon:deps
%description
liboqs provides:
 - a collection of open source implementations of quantum-safe key encapsulation mechanism (KEM) and digital signature algorithms; the full list can be found below
 - a common API for these algorithms
 - a test harness and benchmarking routines
liboqs is part of the Open Quantum Safe (OQS) project led by Douglas Stebila and Michele Mosca, which aims to develop and integrate into applications quantum-safe cryptography to facilitate deployment and testing in real world contexts. In particular, OQS provides prototype integrations of liboqs into TLS and SSH, through OpenSSL and OpenSSH.

%package devel
Summary:          Development libraries for liboqs
Requires:         liboqs%{?_isa} = %{version}-%{release}
%description devel
Header and Library files for doing development with liboqs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -T -b 0 -q -n liboqs-%{oqs_version}
%autopatch -p1
#hobble
rm -rf src/kem/bike
rm -rf src/kem/bike/additional_r4
rm -rf src/kem/classic_mceliece
rm -rf src/kem/frodokem
rm -rf src/kem/hqc
rm -rf src/kem/ntruprime
# code_conventions is for upstream CI, requires astyle
# pytest-xdist is not available in RHEL due to dependencies
sed -e '/COMMAND.*pytest/s|$| --ignore tests/test_code_conventions.py|' \
%if %{defined rhel} || (0%{?oreon} >= 11)
    -e 's/--numprocesses=auto//' \
%endif
    -i tests/CMakeLists.txt

%build

%cmake -GNinja -DBUILD_SHARED_LIBS=ON -DOQS_USE_AES_OPENSSL=ON -DOQS_USE_AES_INSTRUCTIONS=OFF -DOQS_DIST_BUILD=ON -DOQS_ALGS_ENABLED=NIST_2024 -DOQS_USE_SHA3_OPENSSL=ON -DOQS_DLOPEN_OPENSSL=ON -DCMAKE_BUILD_TYPE=Debug -LAH ..
%cmake_build
%check

cd "%{_vpath_builddir}"
ninja run_tests
%install
%cmake_install
for i in liboqsTargets.cmake liboqsTargets-debug.cmake
do
  cp $RPM_BUILD_ROOT/%{_libdir}/cmake/liboqs/$i /tmp/$i
  sed -e "s;$RPM_BUILD_ROOT;;g" /tmp/$i   > $RPM_BUILD_ROOT/%{_libdir}/cmake/liboqs/$i
  rm /tmp/$i
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n liboqs-devel -f %{oreon_filedir}/liboqs-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.12.0-6
- Import

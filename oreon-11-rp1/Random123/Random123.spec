%global source0_hash effafd8656b18030b2a5b995cd3650c51a7c45052e6e1c21e48b9fa7a59d926e
%global debug_package %{nil}
Name:       Random123
Version:    1.14.0
Release:        1%{?dist}
Summary:        Library of random number generators
License:    BSD-3-Clause
URL:        https://github.com/DEShawResearch/random123/
Source0:        https://github.com/DEShawResearch/random123//archive/v%{version}/%{name}-%{version}.tar.gz
Patch:      0001-add-missing-headers.patch
Patch:      enable-riscv.patch
ExcludeArch:    mips64r2 mips32r2 s390
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  patch
# /oreon:deps
%description
Random123 is a library of "counter-based" random number generators (CBRNGs), in
which the Nth random number can be obtained by applying a stateless mixing
function to N instead of the conventional approach of using N iterations of a
stateful transformation. CBRNGs were originally developed for use in MD
applications on Anton, but they are ideal for a wide range of applications on
modern multi-core CPUs, GPUs, clusters, and special-purpose hardware. Three
families of non-cryptographic CBRNGs are described in a paper presented at the
SC11 conference: ARS (based on the Advanced Encryption System (AES)), Threefry
(based on the Threefish encryption function), and Philox (based on integer
multiplication). They all satisfy rigorous statistical testing (passing
BigCrush in TestU01), vectorize and parallelize well (each generator can
produce at least 264 independent streams), have long periods (the period of
each stream is at least 2128), require little or no memory or state, and have
excellent performance (a few clock cycles per byte of random output). The
Random123 library can be used with CPU (C and C++) and GPU (CUDA and OpenCL)
applications.

%package devel
Summary:   Development files for %{name}
Provides:  %{name} = %{version}-%{release}
%description devel
Development files for %{name}.

%package doc
Summary:    Documentation for %{name}
%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir random123-%{version}
%oreon_prep
%build

pushd docs
    doxygen Doxyfile
popd
%install
mkdir -p -m 0755 $RPM_BUILD_ROOT/%{_includedir}/%{name}/
cp -a include/Random123/*  $RPM_BUILD_ROOT/%{_includedir}/%{name}/
%oreon_autofiles Random123-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles Random123-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd tests
    cp GNUmakefile Makefile
    %set_build_flags
    make
popd
%files -f %{oreon_filedir}/main.list
%files -n Random123-devel -f %{oreon_filedir}/Random123-devel.list
%files -n Random123-doc -f %{oreon_filedir}/Random123-doc.list

%changelog

%autochangelog

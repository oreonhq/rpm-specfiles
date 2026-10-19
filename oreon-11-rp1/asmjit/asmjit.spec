%global source0_hash dee5ca76f3a52de1c349a0d1df4efb479e9a0789cfe6d8e38900fb90b567bfd8
%global with_snapshot 1
%global gitdate 20231007
%global commit 6e71f6be0c1ccd6d1dab052ae4e6610e3b031aa7
%global shortcommit %(c=%{commit}; echo ${c:0:8})
%global desc %{expand: \
AsmJit is a lightweight library suitable for low-latency machine code 
generation written in C++. It can generate machine code for X86, X86_64, and
AArch64 architectures. It has a type-safe API that allows C++ compiler to do
semantic checks at compile-time even before the assembled code is generated
or executed.}
Name:		asmjit
Version:	0.0%{?with_snapshot:^%{gitdate}git%{shortcommit}}
Release:        1%{?dist}
Summary:        A lightweight library suitable for low-latency machine code generation
License:	Zlib
URL:		https://asmjit.com
Source0:        https://github.com/%{name}/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:		asmjit-fedora.patch
ExclusiveArch:	aarch64 x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
%{desc}

%package devel
Summary:	Headers and libraries for %{name}
Provides:	%{name}%{?_isa} = %{version}-%{release}
%description devel
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

%build

%cmake -G Ninja \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
	-DASMJIT_STATIC=0 \
	-DASMJIT_TEST=1
%cmake_build
%install
%cmake_install
%oreon_autofiles asmjit-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n asmjit-devel -f %{oreon_filedir}/asmjit-devel.list

%changelog

%autochangelog

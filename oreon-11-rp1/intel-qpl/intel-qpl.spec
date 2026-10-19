%global source0_hash f676dd38a1c81896c92de7c295757eb737eb8af1b831a279420dfeec223e6ff5
Name:		intel-qpl
Version:	1.9.0
Release:        1%{?dist}
Summary:        Intel Query Processing Library
License:	MIT
URL:		https://github.com/intel/qpl
Source0:        https://github.com/intel/qpl/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		qpl-fedora.patch
Patch1:		qpl-werror.patch
ExclusiveArch:	x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  libtsan
BuildRequires:  libuuid-devel
BuildRequires:  nasm
# /oreon:deps
%description
The Intel Query Processing Library (Intel QPL) is an open-source library to 
provide high-performance query processing operations on Intel CPUs. Intel QPL
is aimed to support capabilities of the new Intel In-Memory Analytics 
Accelerator (Intel IAA) available on Next Generation Intel Xeon Scalable 
processors, codenamed Sapphire Rapids processor, such as very high throughput
compression and decompression combined with primitive analytic functions, as 
well as to provide highly-optimized SW fallback on other Intel CPUs.
Intel QPL primarily targets applications such as big-data and in-memory 
analytic databases.
	
%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	accel-config-libs
%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n qpl-%{version}
# Continue to use Gtest 1.14.0 instead of 1.15.2
sed -i -e 's|GTEST_INTERNAL_ATTRIBUTE_MAYBE_UNUSED|GTEST_ATTRIBUTE_UNUSED_|g' tools/tests/common/test_cases.hpp

%build

%cmake \
		-DCMAKE_BUILD_TYPE=RelWithDebInfo \
		-DDYNAMIC_LOADING_LIBACCEL_CONFIG=ON \
		-DQPL_LIBRARY_TYPE=SHARED \
		-DSANITIZE_THREADS=ON \
		-DQPL_BUILD_TESTS=ON \
		-DQPL_BUILD_EXAMPLES=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%__cmake_builddir/tools/tests/functional/tests --dataset=tools/testdata/ --gtest_filter=ta_unit*
%files -f %{oreon_filedir}/main.list
%files -n intel-qpl-devel -f %{oreon_filedir}/intel-qpl-devel.list

%changelog

%autochangelog

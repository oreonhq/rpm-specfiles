%global source0_hash 5c90d6ebd0ea1c3dfaa070950a5ea2ee5e119e3d101217f12fc4ba197efd0f05
%global debug_package %{nil}
%global commit 36459f42a84207330eae706c47e6fab712e6a149
%global shortcommit %%(c=%{commit}; echo ${c:0:7})
Summary:        A toolkit for programming parallel shared memory algorithms
Name:     parlaylib
License:  MIT
Version:  2.3.1^20230215git%{shortcommit}
Release:        1%{?dist}
URL:      https://github.com/cmuparlay/parlaylib
Source0:        https://github.com/cmuparlay/%{name}/archive/%{commit}/%{name}-36459f4.tar.gz
Patch0:   nodownload.patch
ExcludeArch:  aarch64 s390x arm-hfp ppc64le i686
# oreon:deps
BuildRequires:  clang-tools-extra-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  libstdc++-devel
BuildRequires:  llvm
BuildRequires:  re2-devel
# /oreon:deps
%description
ParlayLib is a header only C++ library for developing efficient parallel
algorithms and software on shared-memory multicore machines. It provides
additional tools and primitives that go beyond what is available in the
C++ standard library, and simplifies the task of programming provably
efficient and scalable parallel algorithms. It consists of a sequence
data type (analogous to std::vector), many parallel routines and
algorithms, a work-stealing scheduler to support nested parallelism,
and a scalable memory allocator.

%package devel
Summary:        A toolkit for programming parallel shared memory algorithms
Provides:       %{name}-static = %{version}-%{release}
%description devel
ParlayLib is a header only C++ library for developing efficient parallel
algorithms and software on shared-memory multicore machines. It provides
additional tools and primitives that go beyond what is available in the
C++ standard library, and simplifies the task of programming provably
efficient and scalable parallel algorithms. It consists of a sequence
data type (analogous to std::vector), many parallel routines and
algorithms, a work-stealing scheduler to support nested parallelism,
and a scalable memory allocator.

%package examples
Summary:    Examples for programming parallel shared memory algorithms
BuildArch:  noarch
%description examples
ParlayLib is a header only C++ library for developing efficient parallel
algorithms and software on shared-memory multicore machines. It provides
additional tools and primitives that go beyond what is available in the
C++ standard library, and simplifies the task of programming provably
efficient and scalable parallel algorithms. It consists of a sequence
data type (analogous to std::vector), many parallel routines and
algorithms, a work-stealing scheduler to support nested parallelism,
and a scalable memory allocator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

%cmake -DBUILD_TESTING=ON \
       -DCMAKE_BUILD_TYPE=RELWITHDEBINFO \
       -DFETCH_CONTENT_FULLY_DISCONNECTED=ON \
       -DENABLE_CLANG_TIDY=ON \
       -DENABLE_CPP_CHECK=ON \
       -DPARLAY_TEST=ON \
       -DPARLAY_OPENMP=ON \
       -DPARLAY_EXAMPLES=ON \
       -DCMAKE_INSTALL_DATAROOTDIR=%{_libdir}/cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest --timeout 7200
%files -f %{oreon_filedir}/main.list
%files -n parlaylib-devel -f %{oreon_filedir}/parlaylib-devel.list
%files -n parlaylib-examples -f %{oreon_filedir}/parlaylib-examples.list

%changelog

%autochangelog

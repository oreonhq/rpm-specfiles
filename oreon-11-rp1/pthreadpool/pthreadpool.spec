%global source0_hash 9e8fb6a8ce03616b84f773d7b50ebe0ea2fe3af5b7df6c6f96fa6b3f049a3303

%global commit0 4fe0e1e183925bf8cfa6aae24237e724a96479b8
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global date0 20230829

Summary:        Portable thread pool
Name:           pthreadpool
License:        BSD-2-Clause
Version:        0.0^git%{date0}.%{shortcommit0}
Release:        9%{?dist}

URL:            https://github.com/Maratyszcza/%{name}
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

Patch0:        0001-pthreadpool-fedora-cmake-changes.patch

BuildRequires: cmake
BuildRequires: fxdiv-devel
BuildRequires: gcc-c++
BuildRequires: gtest-devel

%description
pthreadpool is a portable and efficient thread pool
implementation. It provides similar functionality
to #pragma omp parallel for, but with additional features.

Features:
* C interface (C++-compatible).
* 1D-6D loops with step parameters.
* Run on user-specified or auto-detected number of threads.
* Work-stealing scheduling for efficient work balancing.
* Wait-free synchronization of work items.
* Compatible with Linux (including Android), macOS,
  iOS, Windows, Emscripten environments.
* 100% unit tests coverage.
* Throughput and latency microbenchmarks.

%package devel

Summary:        Portable thread pool
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
pthreadpool is a portable and efficient thread pool
implementation. It provides similar functionality
to #pragma omp parallel for, but with additional features.

Features:
* C interface (C++-compatible).
* 1D-6D loops with step parameters.
* Run on user-specified or auto-detected number of threads.
* Work-stealing scheduling for efficient work balancing.
* Wait-free synchronization of work items.
* Compatible with Linux (including Android), macOS,
  iOS, Windows, Emscripten environments.
* 100% unit tests coverage.
* Throughput and latency microbenchmarks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit0}

%build

%cmake \
       -DPTHREADPOOL_USE_SYSTEM_LIBS=ON \
       -DPTHREADPOOL_BUILD_BENCHMARKS=OFF \
       
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%license LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%doc README.md
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so

%changelog
%autochangelog

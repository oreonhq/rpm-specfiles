%global source0_hash 09a5877a8dd821374e5795d12b15187794831cb197c9e1c095247f8eab3cfe4d
%global commit       cedb1fc6f725ea1a51dc9f5bbdc1ec6ec00e33d7
%global shortcommit  %(c=%{commit}; echo ${c:0:7})
%global commitdate   20251007
Name:           qthreads
Version:        1.22^%{commitdate}git%{shortcommit}
Release:        1%{?dist}
Summary:        Lightweight locality-aware user-level threading runtime
License:        BSD-3-Clause AND MIT AND dtoa
URL:            https://www.sandia.gov/qthreads/
Source0:        https://github.com/sandialabs/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
ExcludeArch:    %{ix86} s390x
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  hwloc-devel
# /oreon:deps
%description
The Qthreads API is designed to make using large numbers of threads convenient
and easy. The Qthreads API also provides access to full/empty-bit (FEB)
semantics, where every word of memory can be marked either full or empty, and a
thread can wait for any word to attain either state.

Qthreads is essentially a library for spawning and controlling stackful
coroutines: threads with small (4-8k) stacks. The exposed user API resembles
OS threads, however the threads are entirely in user-space and use their
locked/unlocked status as part of their scheduling.

The library's metaphor is that there are many Qthreads and several "shepherds".
Shepherds generally map to specific processors or memory regions, but this is
not an explicit part of the API. Qthreads are assigned to specific shepherds
and are only allowed to migrate when running on a scheduler that supports work
stealing or when migration is explicitly triggered via user APIs.

The API includes utility functions for making threaded loops, sorting, and
similar operations convenient.

%package devel
Summary:   Development files for qthreads library
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files and development libraries for qthreads library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n qthreads-%{commit}

# Remove bundled HPGCC, only for benchmarks, to show it is unused
# and its LGPL license does not contribute to the built software
rm -rv test/benchmarks/mantevo/hpccg/

%build

%ifarch ppc64le
%cmake -DQTHREADS_CONTEXT_SWAP_IMPL=system
%else
%cmake
%endif
%cmake_build
%install
%cmake_install
install -t '%{buildroot}%{_mandir}/man3' -p -m 0644 -D man/man3/*.3
rm %{buildroot}%{_includedir}/qthread/.gitignore
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n qthreads-devel -f %{oreon_filedir}/qthreads-devel.list

%changelog

%autochangelog

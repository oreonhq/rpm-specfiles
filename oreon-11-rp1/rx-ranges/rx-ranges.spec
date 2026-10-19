%global source0_hash 535a89c8b12aebaacf9accb75d2f08d89cce8f4338e83716936977b03e14fb5d
%global debug_package %{nil}
Name:           rx-ranges
Version:        2.0.0
Release:        1%{?dist}
Summary:        Simpler ranges for C++17
License:        MIT
URL:            https://github.com/simonask/rx-ranges
VCS:            git:%{url}.git
Source0:        https://github.com/simonask/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{url}/commit/27e5191.patch
Patch:          %{url}/commit/a9ab841.patch
Patch:          %{url}/commit/dc74040.patch
Patch:          %{url}/commit/36b0614.patch
Patch:          %{url}/pull/48.patch
Patch:          %{url}/pull/49.patch
ExcludeArch:    %{ix86}
%global desc %{expand:This is a ranges-like library for C++17 that provides zero-overhead list
comprehensions with a pipe-like syntax.
Standard containers can be filtered, transformed, passed through various
algorithms, optimizing to loops that would not be more efficient if written by
hand.
The goal is to provide the tools to write more readable loops, where the intent
of the programmer is clearly communicated to the reader.  Mentally simulating
loops is a common but error-prone part of reading other people's code, and
indeed your own code from 3 months ago.
The library makes heavy use of modern C++17 features, so a compliant C++17
compiler is required.
Features:
- Arbitrary composability.
- Constexpr-friendly.
- No unnecessary temporary heap allocations (`foo | sort() | to_vector()` only
  allocates into the resulting container).
- Heap allocation minimization: `reserve()` is used on resulting containers,
  when possible.
- Open-ended generators (non-terminating, infinite ranges).
- Re-entrancy: A non-rvalue range can be used multiple times in a function.
- Compatible with standard containers (anything that supports `std::begin()`
  and `std::end()`).
- Compatible with standard algorithms (implicit conversion to iterator-like
  objects).
- Simple extensibility with custom range adapters. Just implement the
  `InputRange` faux-concept.
- Non-intrusive `operator|`. The ranges `foo | bar | baz` can be expressed as
  `baz(bar(foo))`, if using `operator|` would introduce ambiguous overloads.
- No dependencies beyond the standard library.
- Integration with foreign codebases (override hooks for `std::optional`,
  `std::remove_cvref_t`, assertions, etc.). Can easily be used as a submodule.
- Compiler support for all major compilers (GCC, Clang, MSVC).
- Zero-overhead, compared to manually written loops in optimized builds.
- Header-only, and single-header.
Other than usability concerns, these are the main differences from C++20
ranges:
- Bidirectional ranges.  Ranges can only be consumed linearly in the forward
  direction.
- Random-access ranges.  Ranges can only be consumed linearly in the forward
  direction.
- Internally using iterators.  The internal iteration objects are modeled with
  an "enumerator" concept instead (objects that provide `next()`, `get()`,
  `at_end()`, etc.), which simplifies custom extensions.  Implicit,
  zero-overhead conversion to iterators is provided for compatibility with
  standard algorithms and the range-based for loop syntax.
- Direct access to the data of underlying contiguous ranges (`data()` etc.).}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  cmake(doctest)
BuildRequires:  gcc-c++
# /oreon:deps
%description
%desc

%package devel
Summary:        Simpler ranges for C++17
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}
%description devel
%desc

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
%cmake

%build

%cmake_build
%install
mkdir -p %{buildroot}%{_includedir}
cp -a include/rx %{buildroot}%{_includedir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

cd test
CXXFLAGS='%{build_cxxflags} -I../include -DDOCTEST_CONFIG_IMPLEMENT_WITH_MAIN'
g++ $CXXFLAGS %{build_ldflags} -o test_ranges test_ranges.cpp
./test_ranges
g++ $CXXFLAGS %{build_ldflags} -o calendar calendar.cpp
./calendar
cd -
%files -f %{oreon_filedir}/main.list
%files -n rx-ranges-devel -f %{oreon_filedir}/rx-ranges-devel.list

%changelog

%autochangelog

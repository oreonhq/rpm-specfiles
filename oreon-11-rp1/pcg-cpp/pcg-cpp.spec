%global source0_hash 79f23706ed0cbc1bb57ea35d50d0abed66898b8f7b0bcf2aaecdfd234863b060
%global commit 428802d1a5634f96bcd0705fab379ff0113bcf13
%global snapdate 20220408
Name:           pcg-cpp
Summary:        PCG Random Number Generation, C++ Edition
Version:        0.98.1^%{snapdate}git%{sub %{commit} 1 7}
Release:        1%{?dist}
License:        MIT OR Apache-2.0
SourceLicense:  (%{license}) AND CC0-1.0
URL:            https://github.com/imneme/pcg-cpp
Source0:        https://github.com/imneme/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
ExcludeArch:    %{ix86}
%global debug_package %{nil}
%global common_description %{expand:
This code provides an implementation of the PCG family of random number
generators, which are fast, statistically excellent, and offer a number of
useful features.
Full details can be found at the PCG-Random website
(http://www.pcg-random.org/). This version of the code provides many family
members – if you just want one simple generator, you may prefer the minimal C
version of the library.
There are two kinds of generator, normal generators and extended generators.
Extended generators provide k dimensional equidistribution and can perform
party tricks, but generally speaking most people only need the normal
generators.
There are two ways to access the generators, using a convenience typedef or by
using the underlying templates directly (similar to C++11’s std::mt19937
typedef vs its std::mersenne_twister_engine template). For most users, the
convenience typedef is what you want, and probably you’re fine with pcg32 for
32-bit numbers. If you want 64-bit numbers, either use pcg64 (or, if you’re on
a 32-bit system, making 64 bits from two calls to pcg32_k2 may be faster).}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description %{common_description}

%package devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       pcg-cpp-static = %{version}-%{release}
%description devel %{common_description}

%package doc
Summary:        Documentation and examples for pcg-cpp
BuildArch:      noarch
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pcg-cpp-%{commit}
find . -name '.gitignore' -print -delete
# Make a copy of the sample/ directory that will not contain compiled
# executables, since we would like to install the sources as documentation.
cp -rp sample examples

%build

%make_build
%install
%make_install PREFIX=%{_prefix}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build test
%files -f %{oreon_filedir}/main.list
%files -n pcg-cpp-devel -f %{oreon_filedir}/pcg-cpp-devel.list
%files -n pcg-cpp-doc -f %{oreon_filedir}/pcg-cpp-doc.list

%changelog

%autochangelog

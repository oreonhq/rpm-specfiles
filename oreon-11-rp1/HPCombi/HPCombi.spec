%global source0_hash 6987e5c6c2db0f2f4ac3a103fb335bc95331515990f9bdd6ac74adcb1864a805
%global debug_package %{nil}
%global _docdir_fmt %{name}-devel
%global giturl  https://github.com/libsemigroups/HPCombi
Name:           HPCombi
Version:        1.1.2
Release:        1%{?dist}
Summary:        High Performance Combinatorics in C++ using vector instructions
License:        GPL-3.0-or-later
URL:            https://libsemigroups.github.io/HPCombi/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-unbundle-simde.patch
ExclusiveArch:  %{x86_64} %{arm64}
%global _desc %{expand:HPCombi is a C++17 header-only library using the SSE and AVX instruction sets,
and some equivalents, for very fast manipulation of combinatorial objects such
as transformations, permutations, and boolean matrices of small size.  The
goal of this project is to implement various new algorithms and benchmark them
on various compiler and architectures.
HPCombi was initially designed using the SSE and AVX instruction sets, and did
not work on machines without these instructions (such as ARM).  From v1.0.0
HPCombi supports processors with other instruction sets also, via SIMD
Everywhere.  It might be the case that the greatest performance gains are
achieved on processors supporting the SSE and AVX instruction sets, but the
HPCombi benchmarks indicate that there are also still significant gains on
other processors too.}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Catch2)
BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libsparsehash)
BuildRequires:  simde-static
# /oreon:deps
%description
%_desc

%package        devel
Summary:        High Performance Combinatorics in C++ using vector instructions
BuildArch:      noarch
Requires:       simde-static
Provides:       %{name}-static = %{version}-%{release}
%description    devel
%_desc

%package        doc
License:        GPL-3.0-or-later AND GPL-1.0-or-later AND MIT
Summary:        API documentation for HPCombi
BuildArch:      noarch
Provides:       bundled(js-jquery)
%description    doc
API documentation for HPCombi.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Ensure we can't use the bundled simde
rm -fr third_party

# Install the pkgconfig file in the noarch directory
sed -i 's,lib/,share/,' CMakeLists.txt

%build

%cmake -DBUILD_TESTING:BOOL=ON
%cmake_build
%install
%cmake_install
rm -fr %{buildroot}%{_datadir}/hpcombi
fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}
for f in %{buildroot}%{_includedir}/hpcombi/{epu8,perm16}.hpp; do
  sed -i.orig 's,"\(simde.*\)",<\1>,' $f
  fixtimestamp $f
done
for f in %{buildroot}%{_includedir}/hpcombi/*.hpp; do
  sed -i.orig 's,\(#include\) "\(.*\)",\1 <hpcombi/\2>,' $f
  fixtimestamp $f
done
%oreon_autofiles HPCombi-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles HPCombi-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifarch %{arm64}
%ctest -E EPU8
%else
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n HPCombi-devel -f %{oreon_filedir}/HPCombi-devel.list
%files -n HPCombi-doc -f %{oreon_filedir}/HPCombi-doc.list

%changelog

%autochangelog

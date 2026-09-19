%global source0_hash 542b6c47f522d581fbf39e51df32c7d1256ac0c626e7c2b41f1040d4b9d50d1e

%undefine __cmake_in_source_build
%ifarch %{valgrind_arches}
%global with_valgrind 1
%endif
%global soversion 2

Name:           libccd
Version:        2.1
Release:        17%{?dist}
Summary:        Library for collision detection between convex shapes

# The src/testsuites/cu/ directory contains some GPL-3.0-or-later code, but it
# is not incorporated in the binary RPMs and does not contribute to their
# licenses.
License:        BSD-3-Clause
URL:            http://libccd.danfis.cz
Source0:        https://github.com/danfis/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# This patch integrates additional programs that are present in
# the testsuites folder into CMake, via CTest.
# It also increments the version number to match the release.
# Not yet submitted  upstream
Patch0:         %{name}-2.1-ctest.patch
# This patch changes the ccd.pc file to point to the correct include
# directory.  Not yet submitted upstream
Patch1:         %{name}-2.1-pkgconfig.patch
# Convert check_regressions to python3
# Not submitted upstream
Patch2:         %{name}-2.1-py3.patch

BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  cmake
# These are required for executing the test suite
BuildRequires:  python3
%if 0%{?with_valgrind}
BuildRequires:  valgrind
%endif

%description
libccd implements variation on Gilbert-Johnson-Keerthi (GJK) algorithm + 
Expand Polytope Algorithm (EPA). It also implements Minkowski Portal 
Refinement (MPR, a.k.a. XenoCollide) algorithm as published in Game 
Programming Gems 7.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0 -b .ctest
%patch -P1 -p0 -b .pkgconfig
%patch -P2 -p0 -b .py3

%build
%cmake \
  -DBUILD_TESTS=ON \
  -DCMAKE_BUILD_TYPE=Release \
  ..
%cmake_build

%install
%cmake_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
rm -f %{buildroot}%{_libdir}/*.a
rm -rf %{buildroot}%{_docdir}/ccd

%check
%if 0%{?with_valgrind}
make -C build test ||exit 0
%endif

%files
%doc BSD-LICENSE README.md
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/ccd

%changelog
%autochangelog

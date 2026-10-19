%global source0_hash d6e9836de4c8883c079cce7955032e86e5dcbcb360de21207ef6c73c9710280d
%global commit 947f7ab2b7bbd71248b5bec738b5790a640c6cec
%global snapdate 20250418
%global cxx_std 17
Name:           c4log
Summary:        C++ type-safe logging, mean and lean
Version:        0.0.1^%{snapdate}.%{sub %{commit} 1 7}
%global so_version 0.0.1
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/biojppm/c4log
Source0:        https://github.com/biojppm/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source10:       patch-no-download
ExcludeArch:    %{ix86}
Patch:          c4log-b8b86f3-external-c4core.patch
# oreon:deps
BuildRequires:  c4project
BuildRequires:  cmake
BuildRequires:  cmake(c4core)
BuildRequires:  doctest-devel
BuildRequires:  doctest-static
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  python3-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Development files for c4log
Requires:       c4log%{?_isa} = %{version}-%{release}
Requires:       c4core-devel%{?_isa}
%description devel
The c4log-devel package contains libraries and header files for developing
applications that use c4log.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n c4log-%{commit} -p1

# Remove/unbundle additional dependencies

# c4project (CMake build scripts)
rm -rvf ext/c4core/cmake
cp -rvp %{_datadir}/cmake/c4project ext/c4core/cmake

# Patch out download of doctest:
'%{SOURCE10}' 'ext/c4core/cmake/c4Project.cmake' \
    '^    if\(_DOCTEST\)' '^    endif'

# Do not try to link against a nonexistent doctest library (doctest is
# header-only, and we do not have the complete CMake project for doctest that
# would provide a target that knows this):
sed -r -i 's/\bdoctest\b//' test/CMakeLists.txt

%conf
# We can stop the CMake scripts from downloading doctest by setting
# C4LOG_CACHE_DOWNLOAD_DOCTEST to any directory that exists.
%cmake -GNinja \
  -DCMAKE_CXX_STANDARD=%{cxx_std} \
  -DC4LOG_CACHE_DOWNLOAD_DOCTEST:PATH=/ \
  -DC4LOG_BUILD_TESTS=ON

%build

%cmake_build
%install
%cmake_install
if [ '%{_libdir}' != '%{_prefix}/lib' ]
then
  mkdir -p '%{buildroot}%{_libdir}'
  mv -v %{buildroot}%{_prefix}/lib/libc4log.so* '%{buildroot}%{_libdir}/'
  mkdir -p '%{buildroot}%{_libdir}/cmake'
  mv -v %{buildroot}%{_prefix}/lib/cmake/c4log '%{buildroot}%{_libdir}/cmake/'
  find %{buildroot}%{_libdir}/cmake/c4log -type f -name '*.cmake' -print0 |
    xargs -r -t -0 sed -r -i "s@/lib/@/$(basename '%{_libdir}')/@"
fi
%oreon_autofiles c4log-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cmake_build --target c4log-test-run-verbose
%files -f %{oreon_filedir}/main.list
%files -n c4log-devel -f %{oreon_filedir}/c4log-devel.list

%changelog

%autochangelog

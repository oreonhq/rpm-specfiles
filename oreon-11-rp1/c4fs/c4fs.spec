%global source0_hash 23b9043948a0d19c3cdbbbca8e3b00db01ef11263a2a63696e5bdd38a7f1bdac
%global commit a5bbd666a60ea522674f82c005575ad96a3135aa
%global snapdate 20260107
%global cxx_std 17
Name:           c4fs
Summary:        C++ file system utilities
Version:        0.0.1^%{snapdate}.%{sub %{commit} 1 7}
%global so_version 0.0.1
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/biojppm/c4fs
Source0:        https://github.com/biojppm/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          c4fs-1abba00-external-c4core.patch
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  c4project
BuildRequires:  cmake
BuildRequires:  cmake(c4core)
BuildRequires:  doctest-devel
BuildRequires:  doctest-static
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Development files for c4fs
Requires:       c4fs%{?_isa} = %{version}-%{release}
Requires:       c4core-devel%{?_isa}
%description devel
The c4fs-devel package contains libraries and header files for developing
applications that use c4fs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n c4fs-%{commit} -p1

# Remove/unbundle additional dependencies

# c4project (CMake build scripts)
find ext
cp -rp '%{_datadir}/cmake/c4project' ext/c4core/cmake

# Do not try to link against a nonexistent doctest library (doctest is
# header-only, and we do not have the complete CMake project for doctest that
# would provide a target that knows this):
sed -r -i \
    -e 's/(LIBS.*)\bdoctest\b/\1/' \
    -e 's/(c4_setup_testing\()DOCTEST\)/\1\)/' \
    test/CMakeLists.txt

%conf
# We can stop the CMake scripts from downloading doctest by setting
# C4FS_CACHE_DOWNLOAD_DOCTEST to any directory that exists.
%cmake -GNinja \
  -DCMAKE_CXX_STANDARD=%{cxx_std} \
  -DC4FS_CACHE_DOWNLOAD_DOCTEST:PATH=/ \
  -DC4FS_BUILD_TESTS=ON

%build

%cmake_build
%install
%cmake_install
if [ '%{_libdir}' != '%{_prefix}/lib' ]
then
  mkdir -p '%{buildroot}%{_libdir}'
  mv -v %{buildroot}%{_prefix}/lib/libc4fs.so* '%{buildroot}%{_libdir}/'
  mkdir -p '%{buildroot}%{_libdir}/cmake'
  mv -v %{buildroot}%{_prefix}/lib/cmake/c4fs '%{buildroot}%{_libdir}/cmake/'
  find %{buildroot}%{_libdir}/cmake/c4fs -type f -name '*.cmake' -print0 |
    xargs -r -t -0 sed -r -i "s@/lib/@/$(basename '%{_libdir}')/@"
fi
%oreon_autofiles c4fs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cmake_build --target c4fs-test-run-verbose
%files -f %{oreon_filedir}/main.list
%files -n c4fs-devel -f %{oreon_filedir}/c4fs-devel.list

%changelog

%autochangelog

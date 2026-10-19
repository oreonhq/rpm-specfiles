%global source0_hash 3c27b58ac47dbefec0c98addcdf679f7e8a09c76372d8d57299e417eba3c9695
%global cxx_std 17
Name:           c4core
Summary:        C++ core utilities
Version:        0.6.0
%global so_version 0.6.0
Release:        1%{?dist}
URL:            https://github.com/biojppm/c4core
SourceLicense:  MIT AND BSL-1.0
License:        %{shrink:
                MIT AND
                BSL-1.0 AND
                BSD-2-Clause AND
                (Apache-2.0 OR MIT OR BSL-1.0)
                }
Source0:        https://github.com/biojppm/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
%global common_description %{expand:
c4core is a library of low-level C++ utilities, written with low-latency
projects in mind.
Some of the utilities provided by c4core have already equivalent functionality
in the C++ standard, but they are provided as the existing C++ equivalent may
be insufficient (e.g., std::string_view), inefficient (e.g., std::string),
heavy (e.g. streams), or plainly unusable on some platforms/projects, (e.g.
exceptions); some other utilities have equivalent under consideration for C++
standardization; and yet some other utilities have (to the author’s knowledge)
no equivalent under consideration.}
# oreon:deps
BuildRequires:  c4project
BuildRequires:  cmake
BuildRequires:  debugbreak-static
BuildRequires:  doctest-static
BuildRequires:  fast_float-static
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description %{common_description}

%package devel
Summary:        %{summary}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       debugbreak-devel
Requires:       fast_float-devel
Provides:       bundled(ag-random) = 0^20180702git6dc334c
Provides:       bundled(SG14) = 0^20190524git3a3b806
%description devel %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n c4core-%{version}

# Remove/unbundle additional dependencies

# c4project (CMake build scripts)
rm -rvf cmake
ln -s '%{_datadir}/cmake/c4project' cmake

# Do not try to link against a nonexistent doctest library (doctest is
# header-only, and we do not have the complete CMake project for doctest that
# would provide a target that knows this):
sed -r -i \
    -e 's/(LIBS.*)\bdoctest\b/\1/' \
    -e 's/(c4_setup_testing\()DOCTEST\)/\1\)/' \
    test/CMakeLists.txt

# Normally, in releases, the “current.md” changelog file is empty and
# zero-length. When this is true, we remove it so it is not packaged.
if [ "$(stat -c '%s' changelog/current.md)" = '0' ]
then
  rm -vf changelog/current.md
fi

# debugbreak
rm -rvf src/c4/ext/debugbreak
mkdir src/c4/ext/debugbreak
ln -sv %{_includedir}/debugbreak.h src/c4/ext/debugbreak/

# fast_float
#
# The build system expects to produce an amalgamated header, fast_float_all.h,
# from the bundled fast_float. We therefore use a symbolic link to preserve the
# original bundled header path. The amalgamated header will be produced from
# the *system* fast_float headers. Once the amalgamated header is produced, we
# again replace it with a symbolic link to the main system fast_float header,
# thereby fully unbundling fast_float.
rm -rv src/c4/ext/fast_float
mkdir -p src/c4/ext/fast_float/include
ln -sv %{_includedir}/fast_float src/c4/ext/fast_float/include/
# Replace amalgamated single-file header produced by build system with one that
# trivially includes the main system fast_float header.
cat > src/c4/ext/fast_float_all.h <<EOF
#include <fast_float/fast_float.h>
EOF

%conf
# We can stop the CMake scripts from downloading doctest by setting
# C4CORE_CACHE_DOWNLOAD_DOCTEST to any directory that exists.
%cmake -GNinja \
  -DCMAKE_CXX_STANDARD=%{cxx_std} \
  -DC4CORE_CACHE_DOWNLOAD_DOCTEST:PATH=/ \
  -DC4CORE_BUILD_TESTS=ON

%build

%cmake_build
%install
%cmake_install
if [ '%{_libdir}' != '%{_prefix}/lib' ]
then
  mkdir -p '%{buildroot}%{_libdir}'
  mv -v %{buildroot}%{_prefix}/lib/libc4core.so* '%{buildroot}%{_libdir}/'
  mkdir -p '%{buildroot}%{_libdir}/cmake'
  mv -v %{buildroot}%{_prefix}/lib/cmake/c4core '%{buildroot}%{_libdir}/cmake/'
  find %{buildroot}%{_libdir}/cmake/c4core -type f -name '*.cmake' -print0 |
    xargs -r -t -0 sed -r -i "s@/lib/@/$(basename '%{_libdir}')/@"
fi
ln -svf '%{_includedir}/debugbreak.h' \
    '%{buildroot}%{_includedir}/c4/ext/debugbreak/'
%oreon_autofiles c4core-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cmake_build --target c4core-test-run-verbose
if grep -F 'FASTFLOAT_' \
    '%{buildroot}%{_includedir}/c4/ext/fast_float_all.h' >/dev/null
then
  echo 'Unwanted bundling of fast_float was detected!' 1>&2
  exit 1
fi
%files -f %{oreon_filedir}/main.list
%files -n c4core-devel -f %{oreon_filedir}/c4core-devel.list

%changelog

%autochangelog

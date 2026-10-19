%global source0_hash b7e953f13a30d7b6fd677e484de35febde954143a265da15dacd92ed171c73e6
%ifarch ppc64le s390x
%bcond tests 0
%else
%bcond tests 1
%endif
%global common_description %{expand:
TinyGLTF is a header only C++11 glTF 2.0 library.}
Name:           tinygltf
Version:        3.0.1
Release:        1%{?dist}
Summary:        Header only C++11 tiny glTF 2.0 library
License:        MIT
URL:            https://github.com/syoyo/tinygltf
Source0:        https://github.com/syoyo/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  catch1-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  json-devel
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  stb_image-devel
BuildRequires:  stb_image_write-devel
# /oreon:deps
%description    %{common_description}

%package        devel
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
Requires:       cmake-filesystem
Requires:       json-devel
Requires:       stb_image-devel >= 2.30^20251025gitf1c79c0-2
Requires:       stb_image_write-devel
%description    devel %{common_description}

%package        examples
Summary:        Examples for %{name}
%description    examples %{common_description}

This package provides examples exercising %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Replace bundled headers with system versions
ln -sf %{_includedir}/catch/catch.hpp tests/
rm json.hpp stb_image.h stb_image_write.h tests/catch.hpp
sed -i CMakeLists.txt \
  -e '/json.hpp/d' \
  -e '/stb_image.h/d' \
  -e '/stb_image_write.h/d'
sed -i tiny_gltf.h tests/tester.cc \
  -e 's:#include "catch.hpp":#include <catch/catch.hpp>:' \
  -e 's:#include "json.hpp":#include <nlohmann/json.hpp>:' \
  -e 's:#include "stb_image.h":#include <stb_image.h>:' \
  -e 's:#include "stb_image_write.h":#include <stb_image_write.h>:'

# The examples bundle a slew of third party libraries; these aren't built by
# default, so we just clobber them for now instead of unbundling
rm -r examples

# Drop unused bundled deps
rm -r deps tools

# Use our compiler and build flags to build the tests
sed -i tests/Makefile \
  -e 's:clang++:%{__cxx}:g' \
  -e 's:-O0:%{build_cxxflags} %{build_ldflags}:g'

%build

%cmake -DTINYGLTF_HEADER_ONLY=ON
%cmake_build
%make_build -C tests
%install
%cmake_install
install -Dpm0755 %{_vpath_builddir}/loader_example \
  %{buildroot}%{_bindir}/%{name}_loader_example
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

for t in tester tester_noexcept; do
  echo "Running $t"
  (cd tests && ./"$t")
done
%endif
%files -f %{oreon_filedir}/main.list
%files -n tinygltf-devel -f %{oreon_filedir}/tinygltf-devel.list
%files -n tinygltf-examples -f %{oreon_filedir}/tinygltf-examples.list

%changelog

%autochangelog

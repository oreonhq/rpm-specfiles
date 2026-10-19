%global source0_hash 234ba57a64153c96885a6271f15fdcf6c594ac8cb03adaad19abb8d3b2b533fa
%bcond check 0
Name:           blend2d
Version:        0.21.2
Release:        1%{?dist}
Summary:        2D Vector Graphics Engine Powered by a JIT Compiler
License:        Zlib
URL:            https://blend2d.com/
Source0:        https://blend2d.com/download/blend2d-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
# /oreon:deps
%description
Blend2D is a high performance 2D vector graphics engine written in C++ and
released under the Zlib license. The engine utilizes a built-in JIT compiler to
generate optimized pipelines at runtime and is capable of using multiple threads
to boost the performance beyond the possibilities of single-threaded rendering.
Additionally, the engine features a new rasterizer that has been written from
scratch. It delivers superior performance while quality is comparable to
rasterizers used by AGG, FreeType, and Qt. The performance has been optimized by
using an innovative approach to index data that is built during rasterization
and scanned during composition. The rasterizer is robust and excels in rendering
basic shapes, complex vector art, and text.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains development files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n blend2d -p1

sed -i 's/set_target_properties(${target} PROPERTIES/set_target_properties(${target} PROPERTIES SOVERSION 0/' CMakeLists.txt

%build

%cmake \
    -GNinja \
%if %{with check}
    -DBLEND2D_TEST=ON \
%endif
%cmake_build
%install
%cmake_install
%oreon_autofiles blend2d-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n blend2d-devel -f %{oreon_filedir}/blend2d-devel.list

%changelog

%autochangelog

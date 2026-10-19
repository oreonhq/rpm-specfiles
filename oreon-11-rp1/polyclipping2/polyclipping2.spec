%global source0_hash 2a3693aceab4aed3e39b743e038d87701acc53cf05ed7b2013aab3e0aec5287e
%bcond_without tests  # Disable tests by default
%bcond_without docs   # Enable docs by default
Name:           polyclipping2
Version:        2.0.1_DLLs_DLLs
Release:        1%{?dist}
Summary:        Polygon Clipping and Offsetting Library v2
License:        BSL-1.0
URL:            https://angusj.com/clipper2/Docs/Overview.htm
Source0:        https://github.com/AngusJohnson/Clipper2/archive/refs/tags/Clipper2_%{version}.tar.gz
Obsoletes:      clipper2 < %{version}
Provides:       clipper2 = %{version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  gtest-devel
# /oreon:deps
%description
This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with docs}
%package doc
Summary:        Documentation for %{name}
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildArch:      noarch
%description doc
Documentation for Clipper2 library.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Clipper2-Clipper2_%{version}
%oreon_prep
%build

%cmake -S CPP \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS=ON \
    -DCLIPPER2_BUILD_EXAMPLES=OFF \
    -DCLIPPER2_BUILD_TESTS=%{?with_tests:ON}%{!?with_tests:OFF} \
    -DCLIPPER2_DOCS=%{?with_docs:ON}%{!?with_docs:OFF} \
    -DCLIPPER2_HI_PRECISION=ON \
    -DCLIPPER2_PKGCONFIG=ON \
    -DUSE_EXTERNAL_GTEST=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

%ctest -E  "TestMultiplePolygons" \
   --test-dir %{_vpath_builddir}  # Out-of-source test directory
%endif
%files -f %{oreon_filedir}/main.list
%files -n polyclipping2-devel -f %{oreon_filedir}/polyclipping2-devel.list
%files -n polyclipping2-doc -f %{oreon_filedir}/polyclipping2-doc.list

%changelog

%autochangelog

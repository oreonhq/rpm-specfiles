%global source0_hash fcfa6a47a52d4c94dc960bdb747f17e077609235517b0bb5ce8097d6b747695a

%global debug_package %{nil}

Name:           earcut-hpp
Summary:        Fast, header-only polygon triangulation
Version:        2.2.4
Release:        1%{?dist}
License:        ISC
SourceLicense:  %{license} AND SGI-B-2.0
URL:            https://github.com/mapbox/earcut.hpp
Source0:        https://github.com/mapbox/earcut.hpp/archive/v%{version}/earcut.hpp-%{version}.tar.gz

Patch0:         0001-Include-cstdint-for-uint32_t.patch
Patch1:         0001-Use-a-range-for-CMake-minimum-versions-3.2.3.12-supp.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(opengl)

%description
A C++ port of earcut.js, a fast, header-only polygon triangulation library.

%package devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       %{name}-static = %{version}-%{release}

%description devel
Header files for earcut-hpp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n earcut.hpp-%{version}
sed --regexp-extended --in-place \
    's/(setprecision\()6(\))/\116\2/' test/test.cpp

%build
export CXXFLAGS="${CXXFLAGS-} -ffp-contract=off"
%cmake \
  -DEARCUT_BUILD_TESTS:BOOL=ON \
  -DEARCUT_BUILD_BENCH:BOOL=OFF \
  -DEARCUT_BUILD_VIZ:BOOL=OFF \
  -DEARCUT_WARNING_IS_ERROR:BOOL=OFF
%cmake_build

%install
install -D --preserve-timestamps --mode=0644 \
    --target-directory='%{buildroot}%{_includedir}/mapbox' \
    include/mapbox/earcut.hpp

%check
%{_vpath_builddir}/tests

%files devel
%license LICENSE
%doc CHANGELOG.md README.md
%dir %{_includedir}/mapbox
%{_includedir}/mapbox/earcut.hpp

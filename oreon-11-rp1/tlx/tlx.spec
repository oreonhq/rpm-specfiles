%global source0_hash 24dd1acf36dd43b8e0414420e3f9adc2e6bb0e75047e872a06167961aedad769
Name:           tlx
Version:        0.6.1
Release:        7%{?dist}
Summary:        Sophisticated C++ data structures, algorithms, and helpers
License:        BSL-1.0
URL:            https://panthema.net/tlx
Source0:        https://github.com/tlx/tlx/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
TLX is a collection of sophisticated C++ data structures, algorithms,
and miscellaneous helpers.  It contains:
- The fast tournament (loser) trees from MCSTL by Johannes Singler, with
  many fixes.
- A fast intrusive reference counter called CountingPtr, which has
  considerably less overhead than std::shared_ptr.
- Efficient and fast multiway merging algorithms from Johannes Singler,
  which were previously included with gcc.  The tlx version has many
  fixes and is available for clang and MSVC++.
- Many string manipulation algorithms for std::string.
- An improved version of the stx-btree implementation, which is
  basically always a better alternative to std::map (but not
  std::unordered_map).
- A copy of siphash for string hashing.
- Efficient sequential string sorting implementations such as radix sort
  and multikey quicksort.
- Much more; see the doxygen documentation.

%package       devel
Summary:       Headers and library links to build with tlx
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description   devel
Headers and library links to build with tlx.

%package       doc
License:       BSL-1.0 AND GPL-1.0-or-later AND MIT
Summary:       Doxygen documentation for tlx
BuildArch:     noarch
%description   doc
Doxygen documentation for tlx.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake \
  -DTLX_BUILD_SHARED_LIBS:BOOL=ON \
  -DTLX_BUILD_STATIC_LIBS:BOOL=OFF \
  -DTLX_BUILD_STRING_SORTING:BOOL=ON \
  -DTLX_BUILD_TESTS:BOOL=ON \
  %{nil}
%cmake_build
doxygen
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n tlx-devel -f %{oreon_filedir}/tlx-devel.list
%files -n tlx-doc -f %{oreon_filedir}/tlx-doc.list

%changelog

%autochangelog

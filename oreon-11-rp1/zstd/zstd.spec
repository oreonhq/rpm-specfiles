%global source0_hash 37d7284556b20954e56e1ca85b80226768902e2edabd3b649e9e72c0c9012ee3
%bcond_without asm
%bcond_without lz4
%bcond_without lzma
%bcond_without zlib
%bcond_without pzstd
%bcond gtest %[ !0%{?rhel} ]
Name:           zstd
Version:        1.5.7
Release:        1%{?dist}
Summary:        Zstd compression library
License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://github.com/facebook/zstd
Source0:        https://github.com/facebook/zstd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         man-pages-1.5.7.patch
%if %{with lz4}
%endif
%if %{with lzma}
%endif
%if %{with pzstd}
%endif
%if %{with zlib}
%endif
# oreon:deps
BuildRequires:  cmake
BuildRequires:  execstack
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  lz4-devel
BuildRequires:  make
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Zstd, short for Zstandard, is a fast lossless compression algorithm,
targeting real-time compression scenarios at zlib-level compression ratio.

%package -n lib%{name}
Summary:        Zstd shared library
%description -n lib%{name}
Zstandard compression shared library.

%package -n lib%{name}-devel
Summary:        Header files for Zstd library
Requires:       lib%{name}%{?_isa} = %{version}-%{release}
%package -n lib%{name}-static
Summary:        Static variant of the Zstd library
Requires:       lib%{name}-devel = %{version}-%{release}
%description -n lib%{name}-devel
Header files for Zstd library.

%description -n lib%{name}-static
Static variant of the Zstd library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
find -name .gitignore -delete
%patch 1 -p1

%build

%if !%{with asm}
export CPPFLAGS=-DZSTD_DISABLE_ASM
%endif
%global _vpath_srcdir build/cmake
%global _vpath_builddir build/shared
%cmake %{?with_pzstd:-DZSTD_BUILD_CONTRIB=ON} -DZSTD_BUILD_STATIC=NO -DZSTD_PROGRAMS_LINK_SHARED=YES
%cmake_build
%global _vpath_builddir build/static
%cmake %{?with_pzstd:-DZSTD_BUILD_CONTRIB=ON} -DZSTD_BUILD_SHARED=NO -DBUILD_TESTING=YES
%cmake_build
%install
%global _vpath_builddir build/static
%cmake_install
%global _vpath_builddir build/shared
%cmake_install
%if %{with pzstd}
install -D -m644 programs/%{name}.1 %{buildroot}%{_mandir}/man1/p%{name}.1
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*
%endif
%check

execstack %{_vpath_builddir}/lib/libzstd.so.1
%global _vpath_builddir build/static
%ctest --verbose
%if %{with pzstd} && %{with gtest}
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
make PZSTD_CXX_STD=-std=c++17 -C contrib/pzstd tests check
%endif
%files -f %{oreon_filedir}/main.list
%files -n libzstd -f %{oreon_filedir}/libzstd.list
%files -n libzstd-devel -f %{oreon_filedir}/libzstd-devel.list
%files -n libzstd-static -f %{oreon_filedir}/libzstd-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.7-5
- Prepare for Oreon 11 (RP1)

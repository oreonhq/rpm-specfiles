# enable asm implementations by default
%bcond_without asm

# enable .lz4 support by default
%bcond_without lz4

# enable .xz/.lzma support by default
%bcond_without lzma

# enable .gz support by default
%bcond_without zlib

# enable pzstd support by default
%bcond_without pzstd

# Disable gtest on RHEL
%bcond gtest %[ !0%{?rhel} ]

Name:           zstd
Version:        1.5.7
Release:        5%{?dist}
Summary:        Zstd compression library

License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://github.com/facebook/zstd
Source0:        https://github.com/facebook/zstd/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch1:         man-pages-1.5.7.patch

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc %{?with_gtest:gtest-devel}
%if %{with lz4}
BuildRequires:  lz4-devel
%endif
%if %{with lzma}
BuildRequires:  xz-devel
%endif
%if %{with pzstd}
BuildRequires:  gcc-c++
%endif
%if %{with zlib}
BuildRequires:  zlib-devel
%endif
BuildRequires:  execstack

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
# Install shared second so that cmake config files reference the shared library
%global _vpath_builddir build/shared
%cmake_install
%if %{with pzstd}
install -D -m644 programs/%{name}.1 %{buildroot}%{_mandir}/man1/p%{name}.1
%endif

%check
execstack %{_vpath_builddir}/lib/libzstd.so.1

%global _vpath_builddir build/static
%ctest --verbose
%if %{with pzstd} && %{with gtest}
# No pzstd tests with the cmake build at the moment
export CFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
make PZSTD_CXX_STD=-std=c++17 -C contrib/pzstd tests check
%endif

%files
%doc CHANGELOG README.md
%{_bindir}/%{name}
%if %{with pzstd}
%{_bindir}/p%{name}
%{_mandir}/man1/p%{name}.1*
%endif
%{_bindir}/%{name}mt
%{_bindir}/un%{name}
%{_bindir}/%{name}cat
%{_bindir}/%{name}grep
%{_bindir}/%{name}less
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/un%{name}.1*
%{_mandir}/man1/%{name}cat.1*
%{_mandir}/man1/%{name}grep.1*
%{_mandir}/man1/%{name}less.1*
%{_pkgdocdir}/zstd_manual.html
%license COPYING LICENSE

%files -n lib%{name}
%{_libdir}/libzstd.so.*
%license COPYING LICENSE

%files -n lib%{name}-devel
%{_includedir}/zdict.h
%{_includedir}/zstd.h
%{_includedir}/zstd_errors.h
%{_libdir}/pkgconfig/libzstd.pc
%{_libdir}/libzstd.so
%{_libdir}/cmake/zstd/

%files -n lib%{name}-static
%{_libdir}/libzstd.a

%ldconfig_scriptlets -n lib%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.7-5
- Prepare for Oreon 11 (RP1)

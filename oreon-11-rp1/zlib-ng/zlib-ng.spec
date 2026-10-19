%global source0_hash f9c65aa9c852eb8255b636fd9f07ce1c406f061ec19a2e7d508b318ca0c907d1
%bcond_without compat
%bcond_without sanitizers
%global soname libz-ng.so.2
%global compat_soname libz.so.1
%global zlib_ver 1.3.1
%global zlib_obsoletes 1.3
%global supported_abi_test aarch64 ppc64le x86_64
Name:		zlib-ng
Version:	2.3.3
Release:        1%{?dist}
Summary:        Zlib replacement with optimizations
License:	Zlib
Url:		https://github.com/zlib-ng/zlib-ng
Source0:        https://github.com/zlib-ng/zlib-ng/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch:		far.diff
Patch:		pr2152.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(GTest)
BuildRequires:  gcc-c++
BuildRequires:  libabigail
# /oreon:deps
%description
zlib-ng is a zlib replacement that provides optimizations for "next generation"
systems.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for developing
application that use %{name}.

%if %{with compat}

%package	compat
Summary:	Zlib implementation provided by %{name}
Provides:	zlib = %{zlib_ver}
Provides:	zlib%{?_isa} = %{zlib_ver}
Conflicts:	zlib%{?_isa}
Obsoletes:	zlib < %{zlib_obsoletes}
%description	compat
zlib-ng is a zlib replacement that provides optimizations for "next generation"
systems.
The %{name}-compat package contains the library that is API and binary
compatible with zlib.

%package	compat-devel
Summary:	Development files for %{name}-compat
Requires:	%{name}-compat%{?_isa} = %{version}-%{release}
Provides:	zlib-devel = %{zlib_ver}
Provides:	zlib-devel%{?_isa} = %{zlib_ver}
Conflicts:	zlib-devel%{?_isa}
Obsoletes:	zlib-devel < %{zlib_obsoletes}
%description	compat-devel
The %{name}-compat-devel package contains libraries and header files for
developing application that use zlib.

%package	compat-static
Summary:	Static libraries for %{name}-compat
Requires:	%{name}-compat-devel%{?_isa} = %{version}-%{release}
Provides:	zlib-static = %{zlib_ver}
Provides:	zlib-static%{?_isa} = %{zlib_ver}
Conflicts:	zlib-static%{?_isa}
Obsoletes:	zlib-static < %{zlib_obsoletes}
%description	compat-static
The %{name}-compat-static package contains static libraries needed for
developing applications that use zlib.

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

cat <<_EOF_
_EOF_
%global cmake_param %{?with_sanitizers:-DWITH_SANITIZER=ON}
%ifarch riscv64
%global cmake_param %cmake_param -DWITH_RVV=OFF
%endif
%ifarch s390x
%global cmake_param %cmake_param -DWITH_DFLTCC_DEFLATE=ON -DWITH_DFLTCC_INFLATE=ON
%endif
%global __cmake_builddir %{_vpath_builddir}
%cmake %{cmake_param}
%cmake_build
%if %{with compat}
cat <<_EOF_
_EOF_
%global __cmake_builddir %{_vpath_builddir}-compat
%undefine _cmake_shared_libs
%cmake %{cmake_param} -DZLIB_COMPAT=ON -DWITH_NEW_STRATEGIES=OFF -DCMAKE_POSITION_INDEPENDENT_CODE=ON
%cmake_build
%endif
%check

cat <<_EOF_
_EOF_
%global __cmake_builddir %{_vpath_builddir}
%ctest
%ifarch ppc64le
%global target_cpu powerpc64le
%else
%global target_cpu %{_target_cpu}
%endif
%ifarch x86_64
%global cpu_vendor pc
%else
%global cpu_vendor unknown
%endif
%ifarch %{supported_abi_test}
CHOST=%{target_cpu}-%{cpu_vendor}-linux-gnu sh test/abicheck.sh
%endif
%if %{with compat}
cat <<_EOF_
_EOF_
%global __cmake_builddir %{_vpath_builddir}-compat
%ctest
%ifarch %{supported_abi_test}
CHOST=%{target_cpu}-%{cpu_vendor}-linux-gnu sh test/abicheck.sh --zlib-compat
%endif
%endif
%install
%global __cmake_builddir %{_vpath_builddir}
%cmake_install
%if %{with compat}
%global __cmake_builddir %{_vpath_builddir}-compat
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n zlib-ng-devel -f %{oreon_filedir}/zlib-ng-devel.list
%files -n zlib-ng-compat -f %{oreon_filedir}/zlib-ng-compat.list
%files -n zlib-ng-compat-devel -f %{oreon_filedir}/zlib-ng-compat-devel.list
%files -n zlib-ng-compat-static -f %{oreon_filedir}/zlib-ng-compat-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.3-1
- Prepare for Oreon 11 (RP1)

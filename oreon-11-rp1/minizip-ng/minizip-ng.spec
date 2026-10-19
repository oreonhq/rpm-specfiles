%global source0_hash 71af7b9799856d8b03619df3949e9c1be9703f8de0795af71399ba283cb27aac
%bcond_without compat
%global compat_soname libminizip.so.1
%global minizip_ver 1.2.13
%global minizip_obsoletes 1.3
%global minizip_ng_ver 3.0.7
%global minizip_ng_obsoletes 3.0.7-5
Name:           minizip-ng
Version:        4.2.2
Release:        1%{?dist}
Summary:        Minizip-ng contrib in zlib-ng with the latest bug fixes and advanced features
License:        Zlib
URL:            https://github.com/nmoinvaz/%{name}
Source0:        https://github.com/nmoinvaz/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         minizip-ng-4.0.7-openssl_no_engine.patch
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libbsd-devel
BuildRequires:  libzstd-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Minizip-ng zlib-ng contribution that includes:
* AES encryption
* I/O buffering
* PKWARE disk splitting
It also has the latest bug fixes that having been found all over the internet.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   zlib-devel
%description devel
Development files for %{name} library.

%if %{with compat}

%package       compat
Summary:       Minizip implementation provided by %{name}
Provides:      minizip = %{minizip_ver}
Provides:      minizip-compat%{?_isa} = %{minizip_ver}
Obsoletes:     minizip-compat < %{minizip_obsoletes}
Provides:      minizip-ng = %{minizip_ng_ver}
Obsoletes:     minizip-ng < %{minizip_ng_obsoletes}
Provides: minizip <= %{version}-%{release}
Obsoletes: minizip < 3.0.3
%description   compat
minizip-ng is a minizip replacement that provides optimizations for "next generation"
systems.
The %{name}-compat package contains the library that is API and binary
compatible with minizip.

%package       compat-devel
Summary:       Development files for %{name}-compat
Requires:      %{name}-compat%{?_isa} = %{version}-%{release}
Provides:      minizip-compat-devel = %{minizip_ver}
Provides:      minizip-compat-devel%{?_isa} = %{minizip_ver}
Obsoletes:     minizip-compat-devel < %{minizip_obsoletes}
Provides:      minizip-ng-devel = %{minizip_ng_ver}
Obsoletes:     minizip-ng-devel < %{minizip_ng_obsoletes}
Provides: minizip-devel <= %{version}-%{release}
Obsoletes: minizip-devel < 3.0.3
%description   compat-devel
The %{name}-compat-devel package contains libraries and header files for
developing application that use minizip.

%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

cat <<_EOF_
_EOF_
%global __cmake_builddir %{_vpath_builddir}
%cmake \
  -DMZ_BUILD_TESTS:BOOL=OFF \
  -DSKIP_INSTALL_BINARIES:BOOL=ON \
  -DCMAKE_INSTALL_INCLUDEDIR=include \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DMZ_FORCE_FETCH_LIBS:BOOL=OFF \
  -DMZ_COMPAT:BOOL=OFF
%cmake_build
%if %{with compat}
cat <<_EOF_
_EOF_
%global __cmake_builddir %{_vpath_builddir}-compat
%cmake \
  -DMZ_BUILD_TESTS:BOOL=OFF \
  -DSKIP_INSTALL_BINARIES:BOOL=ON \
  -DCMAKE_INSTALL_INCLUDEDIR=include \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DMZ_FORCE_FETCH_LIBS:BOOL=OFF \
  -DMZ_COMPAT:BOOL=ON
%cmake_build
%endif
%install
%global __cmake_builddir %{_vpath_builddir}
%cmake_install
%if %{with compat}
%global __cmake_builddir %{_vpath_builddir}-compat
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n minizip-ng-devel -f %{oreon_filedir}/minizip-ng-devel.list
%files -n minizip-ng-compat -f %{oreon_filedir}/minizip-ng-compat.list
%files -n minizip-ng-compat-devel -f %{oreon_filedir}/minizip-ng-compat-devel.list

%changelog

%autochangelog

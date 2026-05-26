%bcond_without compat

%global compat_soname libminizip.so.1

# Compatible with the following minizip-compat version.
%global minizip_ver 1.2.13
# Obsoletes minizip versions less than.
%global minizip_obsoletes 1.3
# Old minizip-ng version before it was renamed to minizip-ng-compat
%global minizip_ng_ver 3.0.7
# Obsolete version of old minizip-ng
%global minizip_ng_obsoletes 3.0.7-5

Name:           minizip-ng
Version:        4.0.10
Release:        1%{?dist}
Summary:        Minizip-ng contrib in zlib-ng with the latest bug fixes and advanced features

License:        Zlib
URL:            https://github.com/nmoinvaz/%{name}
Source0:        https://github.com/nmoinvaz/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         minizip-ng-4.0.7-openssl_no_engine.patch
# oreon url source checksums begin
%global source0_sha256 c362e35ee973fa7be58cc5e38a4a6c23cc8f7e652555daf4f115a9eb2d3a6be7
%global source0_file minizip-ng-4.0.10.tar.gz
# oreon url source checksums end

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libbsd-devel
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: libzstd-devel
BuildRequires: xz-devel
%if ! (0%{?rhel} >= 10)
BuildRequires: openssl-devel-engine
%endif

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
# We need to Provide and Obsolete the old minizip-ng package before it was rename to minizip-ng-compat
Provides:      minizip-ng = %{minizip_ng_ver}
Obsoletes:     minizip-ng < %{minizip_ng_obsoletes}

# This part is mandatory for the renaming process
# It can be removed in Fedora 42
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
# We need to Provide and Obsolete the old minizip-ng package before it was rename to minizip-ng-compat
Provides:      minizip-ng-devel = %{minizip_ng_ver}
Obsoletes:     minizip-ng-devel < %{minizip_ng_obsoletes}

# This part is mandatory for the renaming process
# It can be removed in Fedora 42
Provides: minizip-devel <= %{version}-%{release}
Obsoletes: minizip-devel < 3.0.3

%description   compat-devel
The %{name}-compat-devel package contains libraries and header files for
developing application that use minizip.

%endif


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/minizip-ng-4.0.10.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "c362e35ee973fa7be58cc5e38a4a6c23cc8f7e652555daf4f115a9eb2d3a6be7" || { echo "oreon: Source0 SHA256 mismatch for minizip-ng-4.0.10.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p 1 -n %{name}-%{version}


%build

cat <<_EOF_
###########################################################################
#
# Build the default minizip-ng library
#
###########################################################################
_EOF_

%global __cmake_builddir %{_vpath_builddir}
%cmake \
  -DMZ_BUILD_TESTS:BOOL=ON \
  -DSKIP_INSTALL_BINARIES:BOOL=ON \
  -DCMAKE_INSTALL_INCLUDEDIR=include \
  -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
  -DMZ_FORCE_FETCH_LIBS:BOOL=OFF \
  -DMZ_COMPAT:BOOL=OFF

%cmake_build

%if %{with compat}
cat <<_EOF_
###########################################################################
#
# Build the compat mode library
#
###########################################################################
_EOF_

%global __cmake_builddir %{_vpath_builddir}-compat
%cmake \
  -DMZ_BUILD_TESTS:BOOL=ON \
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
%endif


%files
%license LICENSE
%doc README.md
%{_libdir}/libminizip-ng.so.4
%{_libdir}/libminizip-ng.so.4{,.*}


%files devel
%{_libdir}/libminizip-ng.so
%{_libdir}/pkgconfig/minizip-ng.pc
%{_libdir}/cmake/minizip-ng/
%{_includedir}/minizip-ng/mz*.h


# Compat files
%if %{with compat}

%files compat
%{_libdir}/%{compat_soname}
%{_libdir}/libminizip.so.4{,.*}

%files compat-devel
%{_libdir}/libminizip.so
%{_libdir}/pkgconfig/minizip.pc
%{_libdir}/cmake/minizip/
%{_includedir}/minizip/mz*.h
%{_includedir}/minizip/unzip.h
%{_includedir}/minizip/zip.h
%{_includedir}/minizip/ioapi.h

%endif


%changelog
* Mon Apr 20 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.10-1
- Import from Fedora 43 dist-git for Oreon 11 RP1

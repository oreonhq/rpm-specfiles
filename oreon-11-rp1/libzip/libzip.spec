%global source0_hash 8a247f57d1e3e6f6d11413b12a6f28a9d388de110adc0ec608d893180ed7097b

%bcond_without tests

Name:    libzip
Version: 1.11.4
Release: 3%{?dist}
Summary: C library for reading, creating, and modifying zip archives

License: BSD-3-Clause
URL:     https://libzip.org/
Source0:        https://libzip.org/download/libzip-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  openssl-devel
BuildRequires:  xz-devel
BuildRequires:  libzstd-devel >= 1.3.6
BuildRequires:  cmake >= 3.10
BuildRequires:  mandoc
%if %{with tests}
BuildRequires:  nihtest
%endif


%description
libzip is a C library for reading, creating, and modifying zip archives. Files
can be added from data buffers, files, or compressed data copied directly from 
other zip archives. Changes made without closing the archive can be reverted. 
The API is documented by man pages.


%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package tools
Summary:  Command line tools from %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
The %{name}-tools package provides command line tools split off %{name}:
- zipcmp
- zipmerge
- ziptool


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

# unwanted in package documentation
rm INSTALL.md

# drop skipped test which make test suite fails (cmake issue ?)
sed -e '/clone-fs-/d' \
    -i regress/CMakeLists.txt


%build
%cmake \
  -DENABLE_COMMONCRYPTO:BOOL=OFF \
  -DENABLE_GNUTLS:BOOL=OFF \
  -DENABLE_MBEDTLS:BOOL=OFF \
  -DENABLE_OPENSSL:BOOL=ON \
  -DENABLE_WINDOWS_CRYPTO:BOOL=OFF \
  -DENABLE_BZIP2:BOOL=ON \
  -DENABLE_LZMA:BOOL=ON \
  -DENABLE_ZSTD:BOOL=ON \
  -DBUILD_TOOLS:BOOL=ON \
  -DBUILD_REGRESS:BOOL=ON \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DBUILD_DOC:BOOL=ON

%cmake_build


%install
%cmake_install


%check
%if %{with tests}
%ctest
%else
: Test suite disabled
%endif


%ldconfig_scriptlets


%files
%license LICENSE
%{_libdir}/libzip.so.5*

%files tools
%{_bindir}/zipcmp
%{_bindir}/zipmerge
%{_bindir}/ziptool
%{_mandir}/man1/zip*

%files devel
%doc AUTHORS THANKS *.md
%{_includedir}/zip.h
%{_includedir}/zipconf*.h
%{_libdir}/libzip.so
%{_libdir}/pkgconfig/libzip.pc
%{_libdir}/cmake/libzip
%{_mandir}/man3/libzip*
%{_mandir}/man3/zip*
%{_mandir}/man3/ZIP*
%{_mandir}/man5/zip*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.11.4-3
- Prepare for Oreon 11 (RP1)

%global source0_hash cf85f373f09e9177c0b21dbfbb427efaedc02d035d2aade65eb58a3cbf9ad267
Name:           lzfse
Version:        1.0
Release:        1%{?dist}
Summary:        LZFSE compression library and command line tool
License:        BSD
URL:            https://github.com/lzfse/lzfse
Source0:        https://github.com/%{name}/%{name}/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.gz
Patch:          %{url}/pull/60.patch
ExcludeArch:    s390x
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
# /oreon:deps
%description
LZFSE is a Lempel-Ziv style data compression algorithm using Finite State
Entropy coding. It targets similar compression rates at higher compression
and decompression speed compared to deflate using zlib.

This package is a reference C implementation of the LZFSE compressor introduced
in the Compression library with OS X 10.11 and iOS 9.

%package        libs
Summary:        Shared libraries for %{name}
%description    libs
This package contains shared libraries for %{name}.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}-libs%{_isa} = %{version}-%{release}
%description    devel
This package contains development headers and libraries for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{name}-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n lzfse-libs -f %{oreon_filedir}/lzfse-libs.list
%files -n lzfse-devel -f %{oreon_filedir}/lzfse-devel.list

%changelog

%autochangelog

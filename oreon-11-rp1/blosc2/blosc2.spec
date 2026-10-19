%global source0_hash ae3a348fd960f29180e8ee97b9fa3dad1a6a592098f2a3eac82979082a5932d5
Name:           blosc2
Version:        3.3.5
Release:        1%{?dist}
Summary:        High performance compressor optimized for binary data
License:        BSD-3-Clause
URL:            https://www.blosc.org/
Source0:        https://github.com/Blosc/c-blosc2/archive/v%{version}/c-blosc2-%{version}.tar.gz
%define soversion 6
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libzstd-devel
BuildRequires:  lz4-devel
BuildRequires:  ninja-build
BuildRequires:  xxhash-devel
BuildRequires:  zlib-devel
BuildRequires:  zlib-ng-devel
# /oreon:deps
%description
Blosc is a high performance compressor optimized for binary data
(i.e. floating-point numbers, integers, and booleans, although it can handle
string data too). It has been designed to transmit data to the processor cache
faster than the traditional, non-compressed, direct memory fetch approach via a
memcpy() OS call. Blosc main goal is not just to reduce the size of large
datasets on-disk or in-memory, but also to accelerate memory-bound computations.

C-Blosc2 is the new major version of C-Blosc, and is backward compatible with
both the C-Blosc1 API and its in-memory format. However, the reverse thing is
generally not true for the format; buffers generated with C-Blosc2 are not
format-compatible with C-Blosc1.

%package devel
Summary:        Development headers for %{name}
Requires:       %{name}%{_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n c-blosc2-%{version} -p1

# https://github.com/Blosc/c-blosc2/issues/489
rm plugins/codecs/ndlz/xxhash.?
sed -r -i '/xxhash.c/d' plugins/codecs/ndlz/CMakeLists.txt

# let's do this to make it clear that we're not using those
rm -r internal-complibs/* internal-complibs

%build

OPTIONS=(
        -GNinja
        -DBUILD_STATIC:BOOL=OFF
        -DBUILD_FUZZERS:BOOL=OFF
        -DBUILD_EXAMPLES:BOOL=OFF
        -DPREFER_EXTERNAL_LZ4:BOOL=ON
        -DPREFER_EXTERNAL_ZLIB:BOOL=ON
        -DPREFER_EXTERNAL_ZSTD:BOOL=ON
        -DDEACTIVATE_AVX2:BOOL=ON
        -DCMAKE_C_FLAGS:STRING="$CFLAGS -Wno-unused-variable"
        )
%cmake "${OPTIONS[@]}"
%cmake_build
%install
%cmake_install
objdump -p %{buildroot}%{_libdir}/libblosc2.so.%{soversion} | grep SONAME
%oreon_autofiles blosc2-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch s390x
%global ignore_result || :
%endif
%ctest -j1 -E 'test_nthreads|bitshuffle' %{?ignore_result}
%files -f %{oreon_filedir}/main.list
%files -n blosc2-devel -f %{oreon_filedir}/blosc2-devel.list

%changelog

%autochangelog

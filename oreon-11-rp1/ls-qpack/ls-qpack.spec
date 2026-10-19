%global source0_hash 1c55c3ec956cdfcfa0b90b5e24dbeb41d35c83f8be823b3c0afb0c33967b6d4c
Name:           ls-qpack
Version:        2.7.0
Release:        1%{?dist}
Summary:        QPACK compression library for use with HTTP/3
License:        MIT
URL:            https://github.com/litespeedtech/ls-qpack
Source0:        https://github.com/litespeedtech/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  perl
BuildRequires:  pkgconfig(libxxhash)
# /oreon:deps
%description
ls-qpack is a full-featured, tested, and fast QPACK library. The QPACK
encoder produces excellent compression results based on an innovative
mnemonic technique. It boasts the fastest Huffman encoder and decoder.

The library is production quality. It is used in OpenLiteSpeed,
LiteSpeed Web Server, and LiteSpeed Web ADC.

The library is robust:
* The encoder does not assume anything about usual HTTP headers
such as Server or User-Agent. Instead, it uses its mnemonic compression
technique to achieve good compression results for any input.
* The decoder uses modulo arithmetic to track dynamic table insertions. This
is in contrast to all other QPACK implementations, which use an integer
counter, meaning that at some point, the decoder will break.
* The decoder processes input in streaming fashion. The caller does not have
to buffer the contents of HTTP/3 HEADERS frame. Instead, the decoder can be
supplied input byte-by-byte.

%package devel
Summary:   QPACK compression library for use with HTTP/3
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  xxhash-devel
%description devel
Development files for ls-qpack

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# remove failing test
# https://github.com/litespeedtech/ls-qpack/issues/51
#sed -i '/dyn_table_cap_mismatch/d' test/CMakeLists.txt
# Do not want rpath
sed -i 's/PRIVATE ls-qpack/PUBLIC ls-qpack/g' bin/CMakeLists.txt
# Remove bundled xxhash
rm -r deps/xxhash

%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
export CFLAGS="%{optflags} -lm"
export LDFLAGS="%{__global_ldflags} -lm"
%cmake -DLSQPACK_TESTS=ON \
       -DLSQPACK_XXH=OFF \
       -DLSQPACK_BIN=ON \
       -DCMAKE_SKIP_INSTALL_RPATH=TRUE
%cmake_build
%install
%cmake_install
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/encode-int
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/fuzz-decode
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/interop-decode
chrpath --delete $RPM_BUILD_ROOT%{_bindir}/interop-encode
chmod 755 $RPM_BUILD_ROOT%{_bindir}/encode-int
chmod 755 $RPM_BUILD_ROOT%{_bindir}/fuzz-decode
chmod 755 $RPM_BUILD_ROOT%{_bindir}/interop-decode
chmod 755 $RPM_BUILD_ROOT%{_bindir}/interop-encode
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n ls-qpack-devel -f %{oreon_filedir}/ls-qpack-devel.list

%changelog

%autochangelog

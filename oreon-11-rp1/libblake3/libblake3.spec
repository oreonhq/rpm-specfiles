# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c6782a28842b1c0478524ac06a4f2ede784038ee298d6e2162c0b089c4306a3c

Name: libblake3
Version: 1.8.7
Release: 1%{?dist}
Summary: C implementation of the BLAKE3 hash function
License: Apache-2.0 OR CC0-1.0
URL: https://github.com/BLAKE3-team/BLAKE3
Source0: %{url}/archive/refs/tags/%{version}.tar.gz#/BLAKE3-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
Libblake3 is the official C implementation of the BLAKE3 cryptographic
hash function.

%package devel
Summary: Development files for libblake3
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libblake3) = %{version}

%description devel
Headers and build metadata for applications using libblake3.

%prep
%oreon_sha256
%autosetup -n BLAKE3-%{version}

%build
%cmake -S c \
  -G Ninja \
  -DBUILD_SHARED_LIBS=ON
%cmake_build

%install
%cmake_install

%check
cat > blake3-smoke.c <<'EOF'
#include <stdio.h>
#include <blake3.h>
int main(void) {
    unsigned char out[BLAKE3_OUT_LEN];
    blake3_hasher hasher;
    blake3_hasher_init(&hasher);
    blake3_hasher_finalize(&hasher, out, sizeof(out));
    for (size_t i = 0; i < sizeof(out); i++)
        printf("%02x", out[i]);
    putchar('\n');
    return 0;
}
EOF
gcc blake3-smoke.c -I%{buildroot}%{_includedir} \
  -L%{buildroot}%{_libdir} -Wl,-rpath,%{buildroot}%{_libdir} \
  -lblake3 -o blake3-smoke
test "$(./blake3-smoke)" = \
  af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262

%ldconfig_scriptlets

%files
%license LICENSE_A2 LICENSE_CC0
%{_libdir}/libblake3.so.0*

%files devel
%doc c/README.md
%{_includedir}/blake3.h
%{_libdir}/libblake3.so
%{_libdir}/pkgconfig/libblake3.pc
%{_libdir}/cmake/blake3/

%changelog
%autochangelog

%global source3_hash c4f73492e038b6c0830cd82d0c37a4e61523cb30a800be0b1f6dbca4e48f971d
%global source2_hash 7dc3219b00ab2d33d5108a6cfb1b6d11c1476f882493acdf0be5bcc9a181336b
%global source1_hash beb27610d5279942b572f2abe0523d2b7db867cee417a90f4b56fb784ee46420
%global source0_hash 8072f6ad42c0e3bbfca88ed09bf8f1106ce207a39129af920f70081b8f2fe286
%global debug_package %{nil}
%global _lto_cflags %nil
%global _warning_options %_warning_options -Wformat
Name:           micropython
Version:        1.29.0
Release:        1%{?dist}
Summary:        Implementation of Python 3 with very low memory footprint
License:        MIT AND BSD-4-Clause-UC AND Apache-2.0
URL:            http://micropython.org/
Source0:        https://github.com/micropython/micropython/archive/v%{version}.tar.gz
%global berkley_commit 0f3bb6947c2f57233916dccd7bb425d7bf86e5a6
Source1:       https://github.com/pfalcon/berkeley-db-1.xx/archive/%{berkley_commit}/berkeley-db-1.xx-%{berkley_commit}.tar.gz
%global mbedtls_commit 107ea89daaefb9867ea9121002fbbdf926780e98
Source2:       https://github.com/Mbed-TLS/mbedtls/archive/%{mbedtls_commit}/mbedtls-%{mbedtls_commit}.tar.gz
%global micropython_lib_commit 6ae440a8a144233e6e703f6759b7e7a0afaa37a4
Source3: https://github.com/micropython/micropython-lib/archive/%{micropython_lib_commit}/micropython-lib-%{micropython_lib_commit}.tar.gz
ExclusiveArch:  %{arm} aarch64 x86_64 riscv64
%global cpython_version_tests 3.13
Provides:       bundled(mbedtls) = 3.6.2
Provides:       bundled(libdb) = 1.85
Provides:       bundled(micropython-lib) = %{version}
# oreon:deps
BuildRequires:  /usr/bin/python3.13
BuildRequires:  execstack
BuildRequires:  gcc
BuildRequires:  libffi-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
Implementation of Python 3 with very low memory footprint

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

# git submodules
rmdir lib/berkeley-db-1.xx
tar -xf %{SOURCE1}
mv berkeley-db-1.xx-%{berkley_commit} lib/berkeley-db-1.xx

head -n 32 lib/berkeley-db-1.xx/db/db.c > LICENSE.libdb

rmdir lib/mbedtls
tar -xf %{SOURCE2}
mv mbedtls-%{mbedtls_commit} lib/mbedtls

mv lib/mbedtls/LICENSE LICENSE.mbedtls

rmdir lib/micropython-lib
tar -xf %{SOURCE3}
mv micropython-lib-%{micropython_lib_commit}/ lib/micropython-lib

# Fix shebangs
files=$(grep -rl '#!/usr/bin/env python')
%py3_shebang_fix $files

# Removing pre-built binary; not required for build
rm ports/cc3200/bootmgr/relocator/relocator.bin

%build

%make_build -C mpy-cross
%make_build -C ports/unix PYTHON=%{python3} V=1
execstack -c ports/unix/build-standard/micropython
%check

%ifarch riscv64
rm tests/float/float_parse.py tests/float/float_parse_doubleprec.py
%endif
pushd ports/unix
export MICROPY_CPYTHON3=python%{cpython_version_tests}
make PYTHON=%{python3} V=1 test
popd
%install
mkdir -p %{buildroot}%{_bindir}
install -pm 755 ports/unix/build-standard/micropython %{buildroot}%{_bindir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

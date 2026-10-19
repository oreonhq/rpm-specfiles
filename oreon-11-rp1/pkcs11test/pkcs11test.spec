%global source0_hash 23a50e410ea5180febfb3e1a253edeccf783b812ee49fd515fce5befdce0043c
%bcond check 1
%global date 20230418
%global commit 2cbe462c62bacf537b9a9a427a1c053d8c2e4760
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           pkcs11test
Version:        0~%{date}git%{shortcommit}
Release:        1%{?dist}
Summary:        PKCS#11 Test Suite
License:        Apache-2.0 AND LicenseRef-RSA
URL:            https://github.com/google/pkcs11test
Source0:        https://github.com/google/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Patch:          %{url}/pull/74.patch
%if %{with check}
%endif
Provides:       bundled(pkcs11-headers) = 1.4
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  make
BuildRequires:  opencryptoki-libs
BuildRequires:  sed
# /oreon:deps
%description
This package provides a test suite for PKCS#11.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1

# Build system fixes
# * Replace bundled gtest with the system one
# * Switch to C++17 as now required by the system gtest package
# * Fix library path for opencryptoki
rm -r gtest-1.10.0
sed -i makefile \
  -e 's:libgtest.a::' \
  -e 's:-std=c++0x:-std=c++17:' \
  -e 's:-lpthread:-lpthread -lgtest %{build_ldflags}:' \
  -e 's:/usr/lib/opencryptoki:%{_libdir}/opencryptoki:g'

# Rename license for bundled pkcs11 headers
mv third_party/pkcs11/LICENSE third_party/pkcs11/LICENSE.pkcs11

%build

%if 0%{?el9}
%set_build_flags
%endif
%make_build \
  GTEST_INC="-isystem %{_includedir}/gtest" \
  GTEST_DIR="%{_includedir}/gtest"
%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}
%oreon_autofiles main
%if %{with check}
%check

%make_build test_opencryptoki
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

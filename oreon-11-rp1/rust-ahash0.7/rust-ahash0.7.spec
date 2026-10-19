%global source0_hash 891477e0c6a8957309ee5c45a6368af3ae14bb510732d2684ffa19af310920f9
%bcond check 0
%global debug_package %{nil}
%global crate ahash
Name:           rust-ahash0.7
Version:        0.7.8
Release:        1%{?dist}
Summary:        Non-cryptographic hash function using AES-NI for high performance
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ahash
Source0:        https://static.crates.io/crates/ahash/ahash-%{version}.crate
Patch:          ahash-fix-metadata-auto.diff
Patch:          ahash-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+atomic-polyfill-devel
Summary:        Non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+atomic-polyfill-devel

This package contains library source intended for building other packages which
use the "atomic-polyfill" feature of the "%{crate}" crate.

%package     -n %{name}+compile-time-rng-devel
Summary:        Non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+compile-time-rng-devel

This package contains library source intended for building other packages which
use the "compile-time-rng" feature of the "%{crate}" crate.

%package     -n %{name}+const-random-devel
Summary:        Non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+const-random-devel

This package contains library source intended for building other packages which
use the "const-random" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm tests/{bench.rs,map_tests.rs}
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-ahash0.7-devel -f %{oreon_filedir}/rust-ahash0.7-devel.list

%changelog

%autochangelog

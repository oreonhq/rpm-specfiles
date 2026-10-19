%global source0_hash 5a15f179cd60c4584b8a8c596927aadc462e27f2ca70c04e0071964a73ba7a75
%bcond check 0
%global debug_package %{nil}
%global crate ahash
Name:           rust-ahash0.8
Version:        0.8.12
Release:        2%{?dist}
Summary:        A non-cryptographic hash function using AES-NI for high performance
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ahash
Source0:        https://static.crates.io/crates/ahash/ahash-%{version}.crate
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
Summary:        A non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+atomic-polyfill-devel
Summary:        A non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+atomic-polyfill-devel

This package contains library source intended for building other packages which
use the "atomic-polyfill" feature of the "%{crate}" crate.

%package     -n %{name}+compile-time-rng-devel
Summary:        A non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+compile-time-rng-devel

This package contains library source intended for building other packages which
use the "compile-time-rng" feature of the "%{crate}" crate.

%package     -n %{name}+const-random-devel
Summary:        A non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+const-random-devel

This package contains library source intended for building other packages which
use the "const-random" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        A non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-arm-aes-devel
Summary:        A non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+nightly-arm-aes-devel

This package contains library source intended for building other packages which
use the "nightly-arm-aes" feature of the "%{crate}" crate.

%package     -n %{name}+no-rng-devel
Summary:        A non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+no-rng-devel

This package contains library source intended for building other packages which
use the "no-rng" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-rng-devel
Summary:        A non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+runtime-rng-devel

This package contains library source intended for building other packages which
use the "runtime-rng" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A non-cryptographic hash function using AES-NI for high performance
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
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
%files -n rust-ahash0.8-devel -f %{oreon_filedir}/rust-ahash0.8-devel.list

%changelog

%autochangelog

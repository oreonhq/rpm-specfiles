%global source0_hash e661dda6640fad38e827a6d4a310ff4763082116fe217f279885c97f511bb0b7
%bcond check 0
%global debug_package %{nil}
%global crate num-bigint-dig
Name:           rust-num-bigint-dig
Version:        0.8.6
Release:        1%{?dist}
Summary:        Big integer implementation for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/num-bigint-dig
Source0:        https://static.crates.io/crates/num-bigint-dig/num-bigint-dig-%{version}.crate
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
Summary:        Big integer implementation for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Big integer implementation for Rust
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+fuzz-devel
Summary:        Big integer implementation for Rust
BuildArch:      noarch
%description -n %{name}+fuzz-devel

This package contains library source intended for building other packages which
use the "fuzz" feature of the "%{crate}" crate.

%package     -n %{name}+i128-devel
Summary:        Big integer implementation for Rust
BuildArch:      noarch
%description -n %{name}+i128-devel

This package contains library source intended for building other packages which
use the "i128" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        Big integer implementation for Rust
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

%package     -n %{name}+prime-devel
Summary:        Big integer implementation for Rust
BuildArch:      noarch
%description -n %{name}+prime-devel

This package contains library source intended for building other packages which
use the "prime" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Big integer implementation for Rust
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Big integer implementation for Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Big integer implementation for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+u64_digit-devel
Summary:        Big integer implementation for Rust
BuildArch:      noarch
%description -n %{name}+u64_digit-devel

This package contains library source intended for building other packages which
use the "u64_digit" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Big integer implementation for Rust
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-num-bigint-dig-devel -f %{oreon_filedir}/rust-num-bigint-dig-devel.list

%changelog

%autochangelog

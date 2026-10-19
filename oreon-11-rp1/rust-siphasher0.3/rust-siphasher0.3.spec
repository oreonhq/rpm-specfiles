%global source0_hash 38b58827f4464d87d377d175e90bf58eb00fd8716ff0a62f80356b5e61555d0d
%bcond check 0
%global debug_package %{nil}
%global crate siphasher
Name:           rust-siphasher0.3
Version:        0.3.11
Release:        1%{?dist}
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/siphasher
Source0:        https://static.crates.io/crates/siphasher/siphasher-%{version}.crate
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
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+serde_no_std-devel
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust
BuildArch:      noarch
%description -n %{name}+serde_no_std-devel

This package contains library source intended for building other packages which
use the "serde_no_std" feature of the "%{crate}" crate.

%package     -n %{name}+serde_std-devel
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust
BuildArch:      noarch
%description -n %{name}+serde_std-devel

This package contains library source intended for building other packages which
use the "serde_std" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        SipHash-2-4, SipHash-1-3 and 128-bit variants in pure Rust
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
%files -n rust-siphasher0.3-devel -f %{oreon_filedir}/rust-siphasher0.3-devel.list

%changelog

%autochangelog

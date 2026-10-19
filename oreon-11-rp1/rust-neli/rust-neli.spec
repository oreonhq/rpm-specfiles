%global source0_hash 6a41d34e46954bbc11a4ebe77e0698f7c02a7f64b2f60da4a3c3431a44ce6704
%bcond check 1
%global debug_package %{nil}
%global crate neli
%global crate_version 0.7.0-rc3
%global supported_arches i686 x86_64 aarch64 ppc64le
Name:           rust-neli
Version:        0.7.0~rc3
Release:        1%{?dist}
Summary:        Type safe netlink library written in Rust
License:        BSD-3-Clause
URL:            https://crates.io/crates/neli
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          neli-fix-metadata.diff
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
Summary:        Type safe netlink library written in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        Type safe netlink library written in Rust
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+netfilter-devel
Summary:        Type safe netlink library written in Rust
BuildArch:      noarch
%description -n %{name}+netfilter-devel

This package contains library source intended for building other packages which
use the "netfilter" feature of the "%{crate}" crate.

%package     -n %{name}+parking_lot-devel
Summary:        Type safe netlink library written in Rust
BuildArch:      noarch
%description -n %{name}+parking_lot-devel

This package contains library source intended for building other packages which
use the "parking_lot" feature of the "%{crate}" crate.

%package     -n %{name}+sync-devel
Summary:        Type safe netlink library written in Rust
BuildArch:      noarch
%description -n %{name}+sync-devel

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Type safe netlink library written in Rust
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
%oreon_vendor_cargo
%build

%ifarch %{supported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifarch %{supported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-neli-devel -f %{oreon_filedir}/rust-neli-devel.list

%changelog

%autochangelog

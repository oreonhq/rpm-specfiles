%global source0_hash 02c3eaab3ac0ede60ffa41add21970a7df7d91772c03383aac6c2c3d53cc716b
%bcond check 0
%global debug_package %{nil}
%global crate ipnetwork
Name:           rust-ipnetwork0.17
Version:        0.17.0
Release:        1%{?dist}
Summary:        Library to work with IP CIDRs in Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ipnetwork
Source0:        https://static.crates.io/crates/ipnetwork/ipnetwork-%{version}.crate
Patch:          ipnetwork-fix-metadata.diff
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
Summary:        Library to work with IP CIDRs in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Library to work with IP CIDRs in Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-ipnetwork0.17-devel -f %{oreon_filedir}/rust-ipnetwork0.17-devel.list

%changelog

%autochangelog

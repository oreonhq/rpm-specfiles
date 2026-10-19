%global source0_hash 7e98097f62769f92dbf95fb51f71c0a68ec18a4ee2e70e0d3e4f47ac005d63e9
%bcond check 1
%global debug_package %{nil}
%global crate rust-netrc
Name:           rust-rust-netrc
Version:        0.1.2
Release:        1%{?dist}
Summary:        Netrc support for Rust with support for reqwest
License:        MIT
URL:            https://crates.io/crates/rust-netrc
Source0:        https://static.crates.io/crates/rust-netrc/rust-netrc-%{version}.crate
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
Summary:        Netrc support for Rust with support for reqwest
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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

export RUST_TEST_THREADS=1
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rust-netrc-devel -f %{oreon_filedir}/rust-rust-netrc-devel.list

%changelog

%autochangelog

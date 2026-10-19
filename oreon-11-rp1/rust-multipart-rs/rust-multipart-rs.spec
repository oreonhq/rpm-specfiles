%global source0_hash 7161f77c3118271d59b61f0f3b7e8cf0c97c6217b33b36f33b6b64a38c9e466a
%bcond check 1
%global debug_package %{nil}
%global crate multipart-rs
Name:           rust-multipart-rs
Version:        0.2.3
Release:        1%{?dist}
Summary:        Simple, zero-allocation, streaming, async multipart reader & writer for Rust
License:        MIT
URL:            https://crates.io/crates/multipart-rs
Source0:        https://static.crates.io/crates/multipart-rs/multipart-rs-%{version}.crate
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
Summary:        Simple, zero-allocation, streaming, async multipart reader & writer for Rust
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-multipart-rs-devel -f %{oreon_filedir}/rust-multipart-rs-devel.list

%changelog

%autochangelog

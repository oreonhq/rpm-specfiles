%global source0_hash a157657054ffe556d8858504af8a672a054a6e0bd9e8ee531059100c0fa11bb2
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate rust-fuzzy-search
Name:           rust-rust-fuzzy-search
Version:        0.1.1
Release:        1%{?dist}
Summary:        Fuzzy Search with trigrams implemented in Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rust-fuzzy-search
Source0:        https://static.crates.io/crates/rust-fuzzy-search/rust-fuzzy-search-%{version}.crate
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
Summary:        Fuzzy Search with trigrams implemented in Rust
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
%files -n rust-rust-fuzzy-search-devel -f %{oreon_filedir}/rust-rust-fuzzy-search-devel.list

%changelog

%autochangelog

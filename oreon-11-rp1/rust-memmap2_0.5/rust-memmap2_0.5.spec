%global source0_hash 83faa42c0a078c393f6b29d5db232d8be22776a891f8f56e5284faee4a20b327
%bcond check 0
%global debug_package %{nil}
%global crate memmap2
Name:           rust-memmap2_0.5
Version:        0.5.10
Release:        1%{?dist}
Summary:        Cross-platform Rust API for memory-mapped file IO
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/memmap2
Source0:        https://static.crates.io/crates/memmap2/memmap2-%{version}.crate
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
Summary:        Cross-platform Rust API for memory-mapped file IO
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+stable_deref_trait-devel
Summary:        Cross-platform Rust API for memory-mapped file IO
BuildArch:      noarch
%description -n %{name}+stable_deref_trait-devel

This package contains library source intended for building other packages which
use the "stable_deref_trait" feature of the "%{crate}" crate.

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
%files -n rust-memmap2_0.5-devel -f %{oreon_filedir}/rust-memmap2_0.5-devel.list

%changelog

%autochangelog

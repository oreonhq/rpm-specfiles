%global source0_hash e08eebf4c7afb1dbb5a68ece983498cf17a788cc076321d9fcc8a3f86da36493
%bcond check 0
%global debug_package %{nil}
%global crate gat-std
Name:           rust-gat-std
Version:        0.1.1
Release:        1%{?dist}
Summary:        Variants of Rust std traits that use GATs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gat-std
Source0:        https://static.crates.io/crates/gat-std/gat-std-%{version}.crate
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
Summary:        Variants of Rust std traits that use GATs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Variants of Rust std traits that use GATs
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

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
%files -n rust-gat-std-devel -f %{oreon_filedir}/rust-gat-std-devel.list

%changelog

%autochangelog

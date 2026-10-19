%global source0_hash 0dde43e75fd43e8a1bf86103336bc699aa8d17ad1be60c76c0bdfd4828e19b78
%bcond check 0
%global debug_package %{nil}
%global crate autocfg
Name:           rust-autocfg0.1
Version:        0.1.8
Release:        1%{?dist}
Summary:        Automatic cfg for Rust compiler features
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/autocfg
Source0:        https://static.crates.io/crates/autocfg/autocfg-%{version}.crate
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
Summary:        Automatic cfg for Rust compiler features
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
%files -n rust-autocfg0.1-devel -f %{oreon_filedir}/rust-autocfg0.1-devel.list

%changelog

%autochangelog

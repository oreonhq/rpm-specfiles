%global source0_hash fa4f8080344d4671fb4e831a13ad1e68092748387dfc4f55e356242fae12ce3e
%bcond check 1
%global debug_package %{nil}
%global crate zerocopy-derive
Name:           rust-zerocopy-derive0.7
Version:        0.7.35
Release:        1%{?dist}
Summary:        Custom derive for traits from the zerocopy crate
License:        BSD-2-Clause OR Apache-2.0 OR MIT
URL:            https://crates.io/crates/zerocopy-derive
Source0:        https://static.crates.io/crates/zerocopy-derive/zerocopy-derive-%{version}.crate
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
Summary:        Custom derive for traits from the zerocopy crate
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
%files -n rust-zerocopy-derive0.7-devel -f %{oreon_filedir}/rust-zerocopy-derive0.7-devel.list

%changelog

%autochangelog

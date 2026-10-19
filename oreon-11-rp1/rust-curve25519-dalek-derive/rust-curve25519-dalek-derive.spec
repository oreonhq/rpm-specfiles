%global source0_hash f46882e17999c6cc590af592290432be3bce0428cb0d5f8b6715e4dc7b383eb3
%bcond check 0
%global debug_package %{nil}
%global crate curve25519-dalek-derive
Name:           rust-curve25519-dalek-derive
Version:        0.1.1
Release:        1%{?dist}
Summary:        curve25519-dalek Derives
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/curve25519-dalek-derive
Source0:        https://static.crates.io/crates/curve25519-dalek-derive/curve25519-dalek-derive-%{version}.crate
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
Summary:        curve25519-dalek Derives
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
%files -n rust-curve25519-dalek-derive-devel -f %{oreon_filedir}/rust-curve25519-dalek-derive-devel.list

%changelog

%autochangelog

%global source0_hash 1557010476e0595c9b568d16dcfb81b93cdeb157612726f5170d31aa707bed27
%bcond check 0
%global debug_package %{nil}
%global crate parity-scale-codec-derive
Name:           rust-parity-scale-codec-derive
Version:        2.3.1
Release:        1%{?dist}
Summary:        Serialization and deserialization derive macro for Parity SCALE Codec
License:        Apache-2.0
URL:            https://crates.io/crates/parity-scale-codec-derive
Source0:        https://static.crates.io/crates/parity-scale-codec-derive/parity-scale-codec-derive-%{version}.crate
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

%package     -n %{name}+max-encoded-len-devel
Summary:        Serialization and deserialization derive macro for Parity SCALE Codec
BuildArch:      noarch
%description -n %{name}+max-encoded-len-devel

This package contains library source intended for building other packages which
use the "max-encoded-len" feature of the "%{crate}" crate.

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
%files -n rust-parity-scale-codec-derive-devel -f %{oreon_filedir}/rust-parity-scale-codec-derive-devel.list

%changelog

%autochangelog

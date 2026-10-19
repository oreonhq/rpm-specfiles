%global source2_hash 0fd830000a45d0c472e06b2a3718b070c902ee9a71a6abc1647ce66920de2eb5
%global source1_hash 2f1947dc952374ef4bf326c7c576a0287fb10a8c069dc6bdef981a7ea0a0cf1a
%global source0_hash 440f724eba9f6996b75d63681b0a92b06947f1457076d503a4d2e2c8f56442b8
%bcond check 1
%global debug_package %{nil}
%global crate prometheus-client-derive-encode
Name:           rust-prometheus-client-derive-encode
Version:        0.4.2
Release:        1%{?dist}
Summary:        Auxiliary crate to derive Encode trait from prometheus-client
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/prometheus-client-derive-encode
Source0:        https://static.crates.io/crates/prometheus-client-derive-encode/prometheus-client-derive-encode-%{version}.crate
Source1:        https://github.com/prometheus/client_rust/raw/v0.19.0/LICENSE-APACHE
Source2:        https://github.com/prometheus/client_rust/raw/v0.19.0/LICENSE-MIT
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
Summary:        Auxiliary crate to derive Encode trait from prometheus-client
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} %{SOURCE2} .
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
%files -n rust-prometheus-client-derive-encode-devel -f %{oreon_filedir}/rust-prometheus-client-derive-encode-devel.list

%changelog

%autochangelog

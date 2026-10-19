%global source0_hash 12b92608f679a6fa515dd1d15c1ff89443026e391200a2c840c7afcba482893d
%bcond check 0
%global debug_package %{nil}
%global crate hickory-proto
Name:           rust-hickory-proto
Version:        0.26.3
Release:        1%{?dist}
Summary:        Hickory DNS is a safe and secure DNS library. This is the foundationa...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hickory-proto
Source0:        https://static.crates.io/crates/hickory-proto/hickory-proto-%{version}.crate
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
Summary:        Hickory DNS is a safe and secure DNS library. This is the foundationa...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dnssec-ring-devel
Summary:        Hickory DNS is a safe and secure DNS library. This is the foundationa...
BuildArch:      noarch
%description -n %{name}+dnssec-ring-devel

This package contains library source intended for building other packages which
use the "dnssec-ring" feature of the "%{crate}" crate.

%package     -n %{name}+mdns-devel
Summary:        Hickory DNS is a safe and secure DNS library. This is the foundationa...
BuildArch:      noarch
%description -n %{name}+mdns-devel

This package contains library source intended for building other packages which
use the "mdns" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Hickory DNS is a safe and secure DNS library. This is the foundationa...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+testing-devel
Summary:        Hickory DNS is a safe and secure DNS library. This is the foundationa...
BuildArch:      noarch
%description -n %{name}+testing-devel

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-bindgen-devel
Summary:        Hickory DNS is a safe and secure DNS library. This is the foundationa...
BuildArch:      noarch
%description -n %{name}+wasm-bindgen-devel

This package contains library source intended for building other packages which
use the "wasm-bindgen" feature of the "%{crate}" crate.

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
%files -n rust-hickory-proto-devel -f %{oreon_filedir}/rust-hickory-proto-devel.list

%changelog

%autochangelog

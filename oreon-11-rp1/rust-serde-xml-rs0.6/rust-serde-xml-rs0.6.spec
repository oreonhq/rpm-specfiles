%global source0_hash fb3aa78ecda1ebc9ec9847d5d3aba7d618823446a049ba2491940506da6e2782
%bcond check 0
%global debug_package %{nil}
%global crate serde-xml-rs
Name:           rust-serde-xml-rs0.6
Version:        0.6.0
Release:        1%{?dist}
Summary:        Xml-rs based deserializer for Serde (compatible with 0.9+)
License:        MIT
URL:            https://crates.io/crates/serde-xml-rs
Source0:        https://static.crates.io/crates/serde-xml-rs/serde-xml-rs-%{version}.crate
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
Summary:        Xml-rs based deserializer for Serde (compatible with 0.9+)
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
%files -n rust-serde-xml-rs0.6-devel -f %{oreon_filedir}/rust-serde-xml-rs0.6-devel.list

%changelog

%autochangelog

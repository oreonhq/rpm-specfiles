%global source0_hash cc2215ce3e6a77550b80a1c37251b7d294febaf42e36e21b7b411e0bf54d540d
%bcond check 0
%global debug_package %{nil}
%global crate serde-xml-rs
Name:           rust-serde-xml-rs
Version:        0.8.2
Release:        1%{?dist}
Summary:        xml-rs based deserializer for Serde (compatible with 1.0)
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
Summary:        xml-rs based deserializer for Serde (compatible with 1.0)
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
%files -n rust-serde-xml-rs-devel -f %{oreon_filedir}/rust-serde-xml-rs-devel.list

%changelog

%autochangelog

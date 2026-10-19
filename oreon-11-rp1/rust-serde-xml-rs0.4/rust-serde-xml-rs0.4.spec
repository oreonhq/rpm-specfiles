%global source0_hash f0bf1ba0696ccf0872866277143ff1fd14d22eec235d2b23702f95e6660f7dfa
%bcond check 0
%global debug_package %{nil}
%global crate serde-xml-rs
Name:           rust-serde-xml-rs0.4
Version:        0.4.1
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
rm tests/readme.rs
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- --lib -- --skip test_doctype_fail
%cargo_test -- --doc -- --skip test_doctype_fail
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-serde-xml-rs0.4-devel -f %{oreon_filedir}/rust-serde-xml-rs0.4-devel.list

%changelog

%autochangelog

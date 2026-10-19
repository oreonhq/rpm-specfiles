%global source0_hash 46262ca4393669799a8df4852e81672ddea46657e73294b1a846f0d5c71509ed
%bcond check 0
%global debug_package %{nil}
%global crate cargo-util-schemas
Name:           rust-cargo-util-schemas
Version:        0.14.2
Release:        1%{?dist}
Summary:        Deserialization schemas for Cargo
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cargo-util-schemas
Source0:        https://static.crates.io/crates/cargo-util-schemas/cargo-util-schemas-%{version}.crate
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

%package     -n %{name}+unstable-schema-devel
Summary:        Deserialization schemas for Cargo
BuildArch:      noarch
%description -n %{name}+unstable-schema-devel

This package contains library source intended for building other packages which
use the "unstable-schema" feature of the "%{crate}" crate.

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
%files -n rust-cargo-util-schemas-devel -f %{oreon_filedir}/rust-cargo-util-schemas-devel.list

%changelog

%autochangelog

%global source1_hash 92d82b247046525130b278df9c1d3d985f78cce81eb93722bd3d9dd9094185c2
%global source0_hash fb959fed63a69baa2e3ae57224d885e686bc3f56c9bb3b03406969980ea57a44
%bcond check 1
%global debug_package %{nil}
%global crate qapi-codegen
Name:           rust-qapi-codegen
Version:        0.11.3
Release:        1%{?dist}
Summary:        QEMU QAPI codegen helper
License:        MIT
URL:            https://crates.io/crates/qapi-codegen
Source0:        https://static.crates.io/crates/qapi-codegen/qapi-codegen-%{version}.crate
Source1:        https://raw.githubusercontent.com/arcnmx/qapi-rs/refs/heads/main/COPYING
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
Summary:        QEMU QAPI codegen helper
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} .
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
%files -n rust-qapi-codegen-devel -f %{oreon_filedir}/rust-qapi-codegen-devel.list

%changelog

%autochangelog

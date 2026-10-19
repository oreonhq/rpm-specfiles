%global source0_hash d8f347189c62a579b8cd5f80714efa178f52e461dc2e6d701d264f5ff22e566c
%bcond check 0
%global debug_package %{nil}
%global crate borsh-derive
Name:           rust-borsh-derive
Version:        1.8.0
Release:        1%{?dist}
Summary:        Binary Object Representation Serializer for Hashing
License:        Apache-2.0
URL:            https://crates.io/crates/borsh-derive
Source0:        https://static.crates.io/crates/borsh-derive/borsh-derive-%{version}.crate
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
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+force_exhaustive_checks-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+force_exhaustive_checks-devel

This package contains library source intended for building other packages which
use the "force_exhaustive_checks" feature of the "%{crate}" crate.

%package     -n %{name}+schema-devel
Summary:        Binary Object Representation Serializer for Hashing
BuildArch:      noarch
%description -n %{name}+schema-devel

This package contains library source intended for building other packages which
use the "schema" feature of the "%{crate}" crate.

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
%files -n rust-borsh-derive-devel -f %{oreon_filedir}/rust-borsh-derive-devel.list

%changelog

%autochangelog

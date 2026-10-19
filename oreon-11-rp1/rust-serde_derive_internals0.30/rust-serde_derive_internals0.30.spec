%global source0_hash f852137cce035d6a4df67ccce505ff6b3e9fd3a10e3e52b24dc71e650bb1a9bd
%bcond check 1
%global debug_package %{nil}
%global crate serde_derive_internals
Name:           rust-serde_derive_internals0.30
Version:        0.30.0
Release:        1%{?dist}
Summary:        AST representation used by Serde derive macros. Unstable
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_derive_internals
Source0:        https://static.crates.io/crates/serde_derive_internals/serde_derive_internals-%{version}.crate
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
Summary:        AST representation used by Serde derive macros. Unstable
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
%files -n rust-serde_derive_internals0.30-devel -f %{oreon_filedir}/rust-serde_derive_internals0.30-devel.list

%changelog

%autochangelog

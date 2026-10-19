%global source0_hash 2d5bcf7b024d6835cfb3d473887cd966994907effbe9227e8c8219824d06c4e8
%bcond check 1
%global debug_package %{nil}
%global crate derive_builder_core
Name:           rust-derive_builder_core
Version:        0.20.2
Release:        1%{?dist}
Summary:        Internal helper library for the derive_builder crate.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/derive_builder_core
Source0:        https://static.crates.io/crates/derive_builder_core/derive_builder_core-%{version}.crate
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
Summary:        Internal helper library for the derive_builder crate.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Internal helper library for the derive_builder crate.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+clippy-devel
Summary:        Internal helper library for the derive_builder crate.
BuildArch:      noarch
%description -n %{name}+clippy-devel

This package contains library source intended for building other packages which
use the "clippy" feature of the "%{crate}" crate.

%package     -n %{name}+lib_has_std-devel
Summary:        Internal helper library for the derive_builder crate.
BuildArch:      noarch
%description -n %{name}+lib_has_std-devel

This package contains library source intended for building other packages which
use the "lib_has_std" feature of the "%{crate}" crate.

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
%files -n rust-derive_builder_core-devel -f %{oreon_filedir}/rust-derive_builder_core-devel.list

%changelog

%autochangelog

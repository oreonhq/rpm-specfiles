%global source0_hash d08889ec5408683408db66ad89e0e1f93dff55c73a4ccc71c427d5b277ee47e6
%bcond check 0
%global debug_package %{nil}
%global crate str_indices
Name:           rust-str_indices
Version:        0.4.4
Release:        1%{?dist}
Summary:        Count and convert between indexing schemes on string slices
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/str_indices
Source0:        https://static.crates.io/crates/str_indices/str_indices-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  tomcli
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Count and convert between indexing schemes on string slices
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        Count and convert between indexing schemes on string slices
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tomcli-set Cargo.toml del 'dev-dependencies.criterion'
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
%files -n rust-str_indices-devel -f %{oreon_filedir}/rust-str_indices-devel.list

%changelog

%autochangelog

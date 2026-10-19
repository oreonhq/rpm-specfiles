%global source0_hash 2e369bee1b05d510a7b4ed645f5faa90619e05437111783ea5848f28d97d3c2e
%bcond check 0
%global debug_package %{nil}
%global crate vte_generate_state_changes
Name:           rust-vte_generate_state_changes
Version:        0.1.2
Release:        1%{?dist}
Summary:        Proc macro for generating VTE state changes
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/vte_generate_state_changes
Source0:        https://static.crates.io/crates/vte_generate_state_changes/vte_generate_state_changes-%{version}.crate
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
Summary:        Proc macro for generating VTE state changes
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
%files -n rust-vte_generate_state_changes-devel -f %{oreon_filedir}/rust-vte_generate_state_changes-devel.list

%changelog

%autochangelog

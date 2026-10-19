%global source0_hash f079e83a288787bcd14a6aea84cee5c87a67c5a3e660c30f557a3d24761b3527
%bcond check 0
%global debug_package %{nil}
%global crate cfg_aliases
Name:           rust-cfg_aliases
Version:        0.2.2
Release:        1%{?dist}
Summary:        A tiny utility to help save you a lot of effort with long winded `#[c...
License:        MIT
URL:            https://crates.io/crates/cfg_aliases
Source0:        https://static.crates.io/crates/cfg_aliases/cfg_aliases-%{version}.crate
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
Summary:        A tiny utility to help save you a lot of effort with long winded `#[c...
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
%files -n rust-cfg_aliases-devel -f %{oreon_filedir}/rust-cfg_aliases-devel.list

%changelog

%autochangelog

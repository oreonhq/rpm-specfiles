%global source0_hash ac0fb996b5acdd543c8b8ff723c719715d437fdce607ac1fda01c977f568020d
%bcond check 0
%global debug_package %{nil}
%global crate clap-cargo
Name:           rust-clap-cargo
Version:        0.19.0
Release:        1%{?dist}
Summary:        Re-usable CLI flags for `cargo` plugins
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/clap-cargo
Source0:        https://static.crates.io/crates/clap-cargo/clap-cargo-%{version}.crate
Patch:          clap-cargo-fix-metadata-auto.diff
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
Summary:        Re-usable CLI flags for `cargo` plugins
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cargo_metadata-devel
Summary:        Re-usable CLI flags for `cargo` plugins
BuildArch:      noarch
%description -n %{name}+cargo_metadata-devel

This package contains library source intended for building other packages which
use the "cargo_metadata" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        Re-usable CLI flags for `cargo` plugins
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

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
%files -n rust-clap-cargo-devel -f %{oreon_filedir}/rust-clap-cargo-devel.list

%changelog

%autochangelog

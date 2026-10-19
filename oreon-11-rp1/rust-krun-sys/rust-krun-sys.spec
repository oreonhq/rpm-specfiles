%global source0_hash 68484a58251533786a3c2aca3361664af68ac6240bf25c29f463f990b2e8238d
%bcond check 1
%global debug_package %{nil}
%global crate krun-sys
Name:           rust-krun-sys
Version:        1.10.1
Release:        1%{?dist}
Summary:        Rust bindings for libkrun
License:        Apache-2.0
URL:            https://crates.io/crates/krun-sys
Source0:        https://static.crates.io/crates/krun-sys/krun-sys-%{version}.crate
Patch:          krun-sys-fix-metadata.diff
ExclusiveArch:  x86_64 aarch64
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  libkrun-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       libkrun-devel
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust bindings for libkrun
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
%files -n rust-krun-sys-devel -f %{oreon_filedir}/rust-krun-sys-devel.list

%changelog

%autochangelog

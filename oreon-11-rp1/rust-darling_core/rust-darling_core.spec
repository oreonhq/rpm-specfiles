%global source0_hash 6837e2cf7485aaae18f86181d2f0e9a7ed297a025e220aeabf63fdebd3a2ddff
%bcond check 0
%global debug_package %{nil}
%global crate darling_core
Name:           rust-darling_core
Version:        0.24.1
Release:        2%{?dist}
Summary:        Helper crate for proc-macro library for reading attributes into struc...
License:        MIT
URL:            https://crates.io/crates/darling_core
Source0:        https://static.crates.io/crates/darling_core/darling_core-%{version}.crate
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

%package     -n %{name}+diagnostics-devel
Summary:        Helper crate for proc-macro library for reading attributes into struc...
BuildArch:      noarch
%description -n %{name}+diagnostics-devel

This package contains library source intended for building other packages which
use the "diagnostics" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Helper crate for proc-macro library for reading attributes into struc...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+strsim-devel
Summary:        Helper crate for proc-macro library for reading attributes into struc...
BuildArch:      noarch
%description -n %{name}+strsim-devel

This package contains library source intended for building other packages which
use the "strsim" feature of the "%{crate}" crate.

%package     -n %{name}+suggestions-devel
Summary:        Helper crate for proc-macro library for reading attributes into struc...
BuildArch:      noarch
%description -n %{name}+suggestions-devel

This package contains library source intended for building other packages which
use the "suggestions" feature of the "%{crate}" crate.

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
%files -n rust-darling_core-devel -f %{oreon_filedir}/rust-darling_core-devel.list

%changelog

%autochangelog

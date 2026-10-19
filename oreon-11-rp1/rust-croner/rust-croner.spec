%global source0_hash a59ed87528b2ee2b6d2b14d6767f6dbe41867dfc581433fc23a7c0fae847467a
%bcond check 1
%global debug_package %{nil}
%global crate croner
Name:           rust-croner
Version:        4.0.0
Release:        1%{?dist}
Summary:        Rust library designed for parsing and evaluating cron patterns
License:        MIT
URL:            https://crates.io/crates/croner
Source0:        https://static.crates.io/crates/croner/croner-%{version}.crate
Patch:          croner-fix-metadata.diff
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
Summary:        Rust library designed for parsing and evaluating cron patterns
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Rust library designed for parsing and evaluating cron patterns
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-croner-devel -f %{oreon_filedir}/rust-croner-devel.list

%changelog

%autochangelog

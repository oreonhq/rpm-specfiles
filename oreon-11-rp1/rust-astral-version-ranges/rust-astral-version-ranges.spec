%global source0_hash 31979bc305610246d78ac01d63467a12d8454c6e3b8b22b5811d343a1198dfbb
%bcond check 1
%global debug_package %{nil}
%global crate astral-version-ranges
Name:           rust-astral-version-ranges
Version:        0.1.4
Release:        1%{?dist}
Summary:        Performance-optimized type for generic version ranges and operations on them
License:        MPL-2.0
URL:            https://crates.io/crates/astral-version-ranges
Source0:        https://static.crates.io/crates/astral-version-ranges/astral-version-ranges-%{version}.crate
Patch:          astral-version-ranges-fix-metadata.diff
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
Summary:        Performance-optimized type for generic version ranges and operations on them
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+proptest-devel
Summary:        Performance-optimized type for generic version ranges and operations on them
BuildArch:      noarch
%description -n %{name}+proptest-devel

This package contains library source intended for building other packages which
use the "proptest" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Performance-optimized type for generic version ranges and operations on them
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
%files -n rust-astral-version-ranges-devel -f %{oreon_filedir}/rust-astral-version-ranges-devel.list

%changelog

%autochangelog

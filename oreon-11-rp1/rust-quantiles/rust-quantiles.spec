%global source0_hash c10fa813fb26fb6c321a6f3085b5ade4cb4730d08d0b9e70a3759136940957f2
%bcond check 0
%global debug_package %{nil}
%global crate quantiles
Name:           rust-quantiles
Version:        0.7.1
Release:        1%{?dist}
Summary:        Collection of approximate quantile algorithms
License:        MIT
URL:            https://crates.io/crates/quantiles
Source0:        https://static.crates.io/crates/quantiles/quantiles-%{version}.crate
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
Summary:        Collection of approximate quantile algorithms
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Collection of approximate quantile algorithms
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_derive-devel
Summary:        Collection of approximate quantile algorithms
BuildArch:      noarch
%description -n %{name}+serde_derive-devel

This package contains library source intended for building other packages which
use the "serde_derive" feature of the "%{crate}" crate.

%package     -n %{name}+serde_support-devel
Summary:        Collection of approximate quantile algorithms
BuildArch:      noarch
%description -n %{name}+serde_support-devel

This package contains library source intended for building other packages which
use the "serde_support" feature of the "%{crate}" crate.

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
%files -n rust-quantiles-devel -f %{oreon_filedir}/rust-quantiles-devel.list

%changelog

%autochangelog

%global source0_hash cab112f0a86d568ea0e627cc1d6be74a1e9cd55214684db5561995f6dad897c6
%bcond check 0
%global debug_package %{nil}
%global crate approx
Name:           rust-approx0.5
Version:        0.5.1
Release:        1%{?dist}
Summary:        Approximate floating point equality comparisons and assertions.
License:        Apache-2.0
URL:            https://crates.io/crates/approx
Source0:        https://static.crates.io/crates/approx/approx-%{version}.crate
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
Summary:        Approximate floating point equality comparisons and assertions.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+num-complex-devel
Summary:        Approximate floating point equality comparisons and assertions.
BuildArch:      noarch
%description -n %{name}+num-complex-devel

This package contains library source intended for building other packages which
use the "num-complex" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Approximate floating point equality comparisons and assertions.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-approx0.5-devel -f %{oreon_filedir}/rust-approx0.5-devel.list

%changelog

%autochangelog

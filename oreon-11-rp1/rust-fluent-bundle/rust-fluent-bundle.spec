%global source0_hash 01203cb8918f5711e73891b347816d932046f95f54207710bda99beaeb423bf4
%bcond check 1
%global debug_package %{nil}
%global crate fluent-bundle
Name:           rust-fluent-bundle
Version:        0.16.0
Release:        1%{?dist}
Summary:        Localization system that unleashes the power of natural language translations
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/fluent-bundle
Source0:        https://static.crates.io/crates/fluent-bundle/fluent-bundle-%{version}.crate
Patch:          fluent-bundle-fix-metadata.diff
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
Summary:        Localization system that unleashes the power of natural language translations
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-benchmarks-devel
Summary:        Localization system that unleashes the power of natural language translations
BuildArch:      noarch
%description -n %{name}+all-benchmarks-devel

This package contains library source intended for building other packages which
use the "all-benchmarks" feature of the "%{crate}" crate.

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
%files -n rust-fluent-bundle-devel -f %{oreon_filedir}/rust-fluent-bundle-devel.list

%changelog

%autochangelog

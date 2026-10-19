%global source0_hash b35a062dbadac17a42e0fc64c27f419b25d6fae98572eb43c8814c9e873d7721
%bcond check 1
%global debug_package %{nil}
%global crate statrs
Name:           rust-statrs
Version:        0.16.1
Release:        1%{?dist}
Summary:        Statistical computing library for Rust
License:        MIT
URL:            https://crates.io/crates/statrs
Source0:        https://static.crates.io/crates/statrs/statrs-%{version}.crate
Patch:          statrs-fix-metadata.diff
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
Summary:        Statistical computing library for Rust
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

%{cargo_test -- -- --exact %{shrink:
    --skip statistics::iter_statistics::tests::test_covariance_consistent_with_variance
    --skip statistics::iter_statistics::tests::test_covariance_is_symmetric
    --skip statistics::iter_statistics::tests::test_mean
    --skip statistics::iter_statistics::tests::test_pop_covar_consistent_with_pop_var
    --skip statistics::iter_statistics::tests::test_std_dev
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-statrs-devel -f %{oreon_filedir}/rust-statrs-devel.list

%changelog

%autochangelog

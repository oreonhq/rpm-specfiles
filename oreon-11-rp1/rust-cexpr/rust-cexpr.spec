%global source0_hash 6fac387a98bb7c37292057cffc56d62ecb629900026402633ae9160df93a8766
%bcond_with check
%global debug_package %{nil}
%global crate cexpr
Name:           rust-cexpr
Version:        0.6.0
Release:        1%{?dist}
Summary:        C expression parser and evaluator
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/cexpr
Source0:        https://static.crates.io/crates/cexpr/cexpr-%{version}.crate
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
Summary:        C expression parser and evaluator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version_no_tilde} -p1
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
%files -n rust-cexpr-devel -f %{oreon_filedir}/rust-cexpr-devel.list

%changelog

%autochangelog

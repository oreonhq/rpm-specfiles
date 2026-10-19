%global source0_hash 7655c9839580ee829dfacba1d1278c2b7883e50a277ff7541299489d6bdfdc45
%bcond check 0
%global debug_package %{nil}
%global crate is_ci
Name:           rust-is_ci
Version:        1.2.0
Release:        1%{?dist}
Summary:        Super lightweight CI environment checker. Just tells you if you're in...
License:        ISC
URL:            https://crates.io/crates/is_ci
Source0:        https://static.crates.io/crates/is_ci/is_ci-%{version}.crate
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
Summary:        Super lightweight CI environment checker. Just tells you if you're in...
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
rm -f %{buildroot}%{_bindir}/is_ci
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-is_ci-devel -f %{oreon_filedir}/rust-is_ci-devel.list

%changelog

%autochangelog

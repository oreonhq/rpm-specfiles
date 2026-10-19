%global source0_hash 830b246a0e5f20af87141b25c173cd1b609bd7779a4617d6ec582abaf90870f3
%bcond check 0
%global debug_package %{nil}
%global crate number_prefix
Name:           rust-number_prefix
Version:        0.4.0
Release:        1%{?dist}
Summary:        Library for numeric prefixes (kilo, giga, kibi).
License:        MIT
URL:            https://crates.io/crates/number_prefix
Source0:        https://static.crates.io/crates/number_prefix/number_prefix-%{version}.crate
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
Summary:        Library for numeric prefixes (kilo, giga, kibi).
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Library for numeric prefixes (kilo, giga, kibi).
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
%files -n rust-number_prefix-devel -f %{oreon_filedir}/rust-number_prefix-devel.list

%changelog

%autochangelog

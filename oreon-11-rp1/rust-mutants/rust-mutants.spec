%global source0_hash add0ac067452ff1aca8c5002111bd6b1c895baee6e45fcbc44e0193aea17be56
%bcond check 1
%global debug_package %{nil}
%global crate mutants
Name:           rust-mutants
Version:        0.0.4
Release:        1%{?dist}
Summary:        Decorator attributes to be used with cargo-mutants
License:        MIT
URL:            https://crates.io/crates/mutants
Source0:        https://static.crates.io/crates/mutants/mutants-%{version}.crate
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
Summary:        Decorator attributes to be used with cargo-mutants
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-mutants-devel -f %{oreon_filedir}/rust-mutants-devel.list

%changelog

%autochangelog

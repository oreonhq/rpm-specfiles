%global source0_hash 5262af4c94921c2646c5ac6ff7900c2af9cbb08dc26a797e18130a7019c039d4
%bcond check 1
%global debug_package %{nil}
%global crate nucleo
Name:           rust-nucleo
Version:        0.5.0
Release:        1%{?dist}
Summary:        Plug and play high performance fuzzy matcher
License:        MPL-2.0
URL:            https://crates.io/crates/nucleo
Source0:        https://static.crates.io/crates/nucleo/nucleo-%{version}.crate
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
Summary:        Plug and play high performance fuzzy matcher
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
%files -n rust-nucleo-devel -f %{oreon_filedir}/rust-nucleo-devel.list

%changelog

%autochangelog

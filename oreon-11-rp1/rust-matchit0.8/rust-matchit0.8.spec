%global source0_hash 2f926ade0c4e170215ae43342bf13b9310a437609c81f29f86c5df6657582ef9
%bcond check 0
%global debug_package %{nil}
%global crate matchit
Name:           rust-matchit0.8
Version:        0.8.6
Release:        1%{?dist}
Summary:        High performance, zero-copy URL router
License:        MIT AND BSD-3-Clause
URL:            https://crates.io/crates/matchit
Source0:        https://static.crates.io/crates/matchit/matchit-%{version}.crate
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
Summary:        High performance, zero-copy URL router
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
%files -n rust-matchit0.8-devel -f %{oreon_filedir}/rust-matchit0.8-devel.list

%changelog

%autochangelog

%global source0_hash 140a09c9305e6d5e557e2ed7cbc68e05765a7d4213975b87cb04920689cc6219
%bcond check 0
%global debug_package %{nil}
%global crate human-sort
Name:           rust-human-sort
Version:        0.2.2
Release:        1%{?dist}
Summary:        Human sort (natural sort) implementation
License:        MIT
URL:            https://crates.io/crates/human-sort
Source0:        https://static.crates.io/crates/human-sort/human-sort-%{version}.crate
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
Summary:        Human sort (natural sort) implementation
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
%files -n rust-human-sort-devel -f %{oreon_filedir}/rust-human-sort-devel.list

%changelog

%autochangelog

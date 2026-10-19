%global source0_hash 0688c2a7f92e427f44895cd63841bff7b29f8d7a1648b9e7e07a4a365b2e1257
%bcond check 1
%global debug_package %{nil}
%global crate dlv-list
Name:           rust-dlv-list0.3
Version:        0.3.0
Release:        1%{?dist}
Summary:        Semi-doubly linked list implemented using a vector
License:        MIT
URL:            https://crates.io/crates/dlv-list
Source0:        https://static.crates.io/crates/dlv-list/dlv-list-%{version}.crate
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
Summary:        Semi-doubly linked list implemented using a vector
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
%files -n rust-dlv-list0.3-devel -f %{oreon_filedir}/rust-dlv-list0.3-devel.list

%changelog

%autochangelog

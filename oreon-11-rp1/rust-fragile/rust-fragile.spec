%global source0_hash fdb2ef9571de3fe79fb6b3b7f0567ddcce6b6c9cefdbc76af63895cf97b54649
%bcond check 1
%global debug_package %{nil}
%global crate fragile
Name:           rust-fragile
Version:        3.0.0
Release:        1%{?dist}
Summary:        Wrapper types for sending non-send values to other threads
License:        Apache-2.0
URL:            https://crates.io/crates/fragile
Source0:        https://static.crates.io/crates/fragile/fragile-%{version}.crate
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
Summary:        Wrapper types for sending non-send values to other threads
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+slab-devel
Summary:        Wrapper types for sending non-send values to other threads
BuildArch:      noarch
%description -n %{name}+slab-devel

This package contains library source intended for building other packages which
use the "slab" feature of the "%{crate}" crate.

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
%files -n rust-fragile-devel -f %{oreon_filedir}/rust-fragile-devel.list

%changelog

%autochangelog

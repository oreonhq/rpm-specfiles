%global source0_hash 479ca8adacdd7ce8f1fb39ce9ecccbfe93a3f1344b3d0d97f20bc0196208f62b
%bcond check 1
%global debug_package %{nil}
%global crate prettyplease
Name:           rust-prettyplease
Version:        0.2.37
Release:        2%{?dist}
Summary:        Minimal syn syntax tree pretty-printer
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/prettyplease
Source0:        https://static.crates.io/crates/prettyplease/prettyplease-%{version}.crate
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
Summary:        Minimal syn syntax tree pretty-printer
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+verbatim-devel
Summary:        Minimal syn syntax tree pretty-printer
BuildArch:      noarch
%description -n %{name}+verbatim-devel

This package contains library source intended for building other packages which
use the "verbatim" feature of the "%{crate}" crate.

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
%files -n rust-prettyplease-devel -f %{oreon_filedir}/rust-prettyplease-devel.list

%changelog

%autochangelog

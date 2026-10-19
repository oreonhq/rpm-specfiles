%global source0_hash ec8ebde2db3681e8c9980cc27822030e68752690ddfa9473e739aeb4dbde6d71
%bcond check 0
%global debug_package %{nil}
%global crate yoke-derive
Name:           rust-yoke-derive
Version:        0.8.4
Release:        1%{?dist}
Summary:        Custom derive for the yoke crate
License:        Unicode-3.0
URL:            https://crates.io/crates/yoke-derive
Source0:        https://static.crates.io/crates/yoke-derive/yoke-derive-%{version}.crate
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
Summary:        Custom derive for the yoke crate
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
%files -n rust-yoke-derive-devel -f %{oreon_filedir}/rust-yoke-derive-devel.list

%changelog

%autochangelog

%global source0_hash 3af92c55d7d839293953fcd0fda5ecfe93297cfde6ffbdec13b41d99c0ba6607
%bcond check 0
%global debug_package %{nil}
%global crate libredox
Name:           rust-libredox
Version:        0.0.2
Release:        1%{?dist}
Summary:        Redox OS bindings
License:        MIT
URL:            https://crates.io/crates/libredox
Source0:        https://static.crates.io/crates/libredox/libredox-%{version}.crate
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
use the "libredox" crate.

%package     -n %{name}+default-devel
Summary:        Redox OS bindings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-libredox-devel -f %{oreon_filedir}/rust-libredox-devel.list

%changelog

%autochangelog

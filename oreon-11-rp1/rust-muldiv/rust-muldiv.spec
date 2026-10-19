%global source0_hash 956787520e75e9bd233246045d19f42fb73242759cc57fba9611d940ae96d4b0
%bcond check 0
%global debug_package %{nil}
%global crate muldiv
Name:           rust-muldiv
Version:        1.0.1
Release:        1%{?dist}
Summary:        Combined multiplication and division with overflow protection
License:        MIT
URL:            https://crates.io/crates/muldiv
Source0:        https://static.crates.io/crates/muldiv/muldiv-%{version}.crate
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
Summary:        Combined multiplication and division with overflow protection
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
%files -n rust-muldiv-devel -f %{oreon_filedir}/rust-muldiv-devel.list

%changelog

%autochangelog

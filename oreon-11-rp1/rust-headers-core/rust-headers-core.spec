%global source0_hash 54b4a22553d4242c49fddb9ba998a99962b5cc6f22cb5a3482bec22522403ce4
%bcond check 0
%global debug_package %{nil}
%global crate headers-core
Name:           rust-headers-core
Version:        0.3.0
Release:        1%{?dist}
Summary:        Typed HTTP headers core trait
License:        MIT
URL:            https://crates.io/crates/headers-core
Source0:        https://static.crates.io/crates/headers-core/headers-core-%{version}.crate
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
Summary:        Typed HTTP headers core trait
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
%files -n rust-headers-core-devel -f %{oreon_filedir}/rust-headers-core-devel.list

%changelog

%autochangelog

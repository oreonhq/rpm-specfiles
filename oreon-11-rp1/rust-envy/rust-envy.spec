%global source0_hash 3f47e0157f2cb54f5ae1bd371b30a2ae4311e1c028f575cd4e81de7353215965
%bcond check 0
%global debug_package %{nil}
%global crate envy
Name:           rust-envy
Version:        0.4.2
Release:        1%{?dist}
Summary:        Deserialize env vars into typesafe structs
License:        MIT
URL:            https://crates.io/crates/envy
Source0:        https://static.crates.io/crates/envy/envy-%{version}.crate
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
Summary:        Deserialize env vars into typesafe structs
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
%files -n rust-envy-devel -f %{oreon_filedir}/rust-envy-devel.list

%changelog

%autochangelog

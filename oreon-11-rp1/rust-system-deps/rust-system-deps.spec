%global source0_hash 396a35feb67335377e0251fcbc1092fc85c484bd4e3a7a54319399da127796e7
%bcond check 0
%global debug_package %{nil}
%global crate system-deps
Name:           rust-system-deps
Version:        7.0.8
Release:        1%{?dist}
Summary:        Discover and configure system dependencies from declarative dependenc...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/system-deps
Source0:        https://static.crates.io/crates/system-deps/system-deps-%{version}.crate
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
Summary:        Discover and configure system dependencies from declarative dependenc...
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
%files -n rust-system-deps-devel -f %{oreon_filedir}/rust-system-deps-devel.list

%changelog

%autochangelog

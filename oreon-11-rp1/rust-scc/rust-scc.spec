%global source0_hash 5d5f8ca67c4f6208caf824037a6a9df0211b4e0937fccc4f543441f294d04511
%bcond check 0
%global debug_package %{nil}
%global crate scc
Name:           rust-scc
Version:        3.8.8
Release:        1%{?dist}
Summary:        High-performance containers and utilities for concurrent and asynchro...
License:        Apache-2.0
URL:            https://crates.io/crates/scc
Source0:        https://static.crates.io/crates/scc/scc-%{version}.crate
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

%package     -n %{name}+equivalent-devel
Summary:        High-performance containers and utilities for concurrent and asynchro...
BuildArch:      noarch
%description -n %{name}+equivalent-devel

This package contains library source intended for building other packages which
use the "equivalent" feature of the "%{crate}" crate.

%package     -n %{name}+loom-devel
Summary:        High-performance containers and utilities for concurrent and asynchro...
BuildArch:      noarch
%description -n %{name}+loom-devel

This package contains library source intended for building other packages which
use the "loom" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        High-performance containers and utilities for concurrent and asynchro...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%files -n rust-scc-devel -f %{oreon_filedir}/rust-scc-devel.list

%changelog

%autochangelog

%global source0_hash 4ba1fd955270ca6f8bd8624ec0c4ee1a251dd3cc0cc18e1e2665ca8f5acb1501
%bcond check 0
%global debug_package %{nil}
%global crate perfcnt
Name:           rust-perfcnt
Version:        0.8.0
Release:        1%{?dist}
Summary:        Library to configure and read hardware performance counters in rust.
License:        MIT
URL:            https://crates.io/crates/perfcnt
Source0:        https://static.crates.io/crates/perfcnt/perfcnt-%{version}.crate
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
Summary:        Library to configure and read hardware performance counters in rust.
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
%files -n rust-perfcnt-devel -f %{oreon_filedir}/rust-perfcnt-devel.list

%changelog

%autochangelog

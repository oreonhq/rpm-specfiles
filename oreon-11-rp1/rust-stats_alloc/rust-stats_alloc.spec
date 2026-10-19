%global source0_hash 5c0e04424e733e69714ca1bbb9204c1a57f09f5493439520f9f68c132ad25eec
%bcond check 0
%global debug_package %{nil}
%global crate stats_alloc
Name:           rust-stats_alloc
Version:        0.1.10
Release:        1%{?dist}
Summary:        Allocator wrapper that allows for instrumenting global allocators
License:        MIT
URL:            https://crates.io/crates/stats_alloc
Source0:        https://static.crates.io/crates/stats_alloc/stats_alloc-%{version}.crate
Patch:          https://github.com/neoeinstein/stats_alloc/pull/7.patch#/stats_alloc-add-license.diff
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
Summary:        Allocator wrapper that allows for instrumenting global allocators
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
%files -n rust-stats_alloc-devel -f %{oreon_filedir}/rust-stats_alloc-devel.list

%changelog

%autochangelog

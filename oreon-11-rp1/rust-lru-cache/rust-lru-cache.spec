%global source0_hash 31e24f1ad8321ca0e8a1e0ac13f23cb668e6f5466c2c57319f6a5cf1cc8e3b1c
%bcond check 0
%global debug_package %{nil}
%global crate lru-cache
Name:           rust-lru-cache
Version:        0.1.2
Release:        1%{?dist}
Summary:        A cache that holds a limited number of key-value pairs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lru-cache
Source0:        https://static.crates.io/crates/lru-cache/lru-cache-%{version}.crate
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

%package     -n %{name}+heapsize-devel
Summary:        A cache that holds a limited number of key-value pairs
BuildArch:      noarch
%description -n %{name}+heapsize-devel

This package contains library source intended for building other packages which
use the "heapsize" feature of the "%{crate}" crate.

%package     -n %{name}+heapsize_impl-devel
Summary:        A cache that holds a limited number of key-value pairs
BuildArch:      noarch
%description -n %{name}+heapsize_impl-devel

This package contains library source intended for building other packages which
use the "heapsize_impl" feature of the "%{crate}" crate.

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
%files -n rust-lru-cache-devel -f %{oreon_filedir}/rust-lru-cache-devel.list

%changelog

%autochangelog

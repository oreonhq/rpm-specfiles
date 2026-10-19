%global source0_hash 8b1e3a325bc115f096c8b77bbf027a7c2592230e70be2d985be950d3d5e60ebe
%bcond check 0
%global debug_package %{nil}
%global crate dary_heap
Name:           rust-dary_heap
Version:        0.3.9
Release:        1%{?dist}
Summary:        A d-ary heap
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/dary_heap
Source0:        https://static.crates.io/crates/dary_heap/dary_heap-%{version}.crate
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

%package     -n %{name}+extra-devel
Summary:        A d-ary heap
BuildArch:      noarch
%description -n %{name}+extra-devel

This package contains library source intended for building other packages which
use the "extra" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A d-ary heap
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        A d-ary heap
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_nightly-devel
Summary:        A d-ary heap
BuildArch:      noarch
%description -n %{name}+unstable_nightly-devel

This package contains library source intended for building other packages which
use the "unstable_nightly" feature of the "%{crate}" crate.

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
%files -n rust-dary_heap-devel -f %{oreon_filedir}/rust-dary_heap-devel.list

%changelog

%autochangelog

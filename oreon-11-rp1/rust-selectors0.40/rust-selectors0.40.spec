%global source0_hash eeee001a77567bb05e71652718d3ff76d8697c151ac523e68e9513194eb2b75a
%bcond check 1
%global debug_package %{nil}
%global crate selectors
Name:           rust-selectors0.40
Version:        0.40.0
Release:        1%{?dist}
Summary:        CSS Selectors matching for Rust
License:        MPL-2.0
URL:            https://crates.io/crates/selectors
Source0:        https://static.crates.io/crates/selectors/selectors-%{version}.crate
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
Summary:        CSS Selectors matching for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bench-devel
Summary:        CSS Selectors matching for Rust
BuildArch:      noarch
%description -n %{name}+bench-devel

This package contains library source intended for building other packages which
use the "bench" feature of the "%{crate}" crate.

%package     -n %{name}+to_shmem-devel
Summary:        CSS Selectors matching for Rust
BuildArch:      noarch
%description -n %{name}+to_shmem-devel

This package contains library source intended for building other packages which
use the "to_shmem" feature of the "%{crate}" crate.

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
%files -n rust-selectors0.40-devel -f %{oreon_filedir}/rust-selectors0.40-devel.list

%changelog

%autochangelog

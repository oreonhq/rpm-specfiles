%global source0_hash 1c25ef604ac7dd839d44d64648952ea23c97866f124ff671b0ed2cf3ad9bb06e
%bcond check 0
%global debug_package %{nil}
%global crate rkyv_derive
Name:           rust-rkyv_derive0.8
Version:        0.8.18
Release:        1%{?dist}
Summary:        Derive macro for rkyv
License:        MIT
URL:            https://crates.io/crates/rkyv_derive
Source0:        https://static.crates.io/crates/rkyv_derive/rkyv_derive-%{version}.crate
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
Summary:        Derive macro for rkyv
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytecheck-devel
Summary:        Derive macro for rkyv
BuildArch:      noarch
%description -n %{name}+bytecheck-devel

This package contains library source intended for building other packages which
use the "bytecheck" feature of the "%{crate}" crate.

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
%files -n rust-rkyv_derive0.8-devel -f %{oreon_filedir}/rust-rkyv_derive0.8-devel.list

%changelog

%autochangelog

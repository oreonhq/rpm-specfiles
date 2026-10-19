%global source0_hash 279cf904654eeebfa37ac9bb1598880884924aab82e290aa65c9e77a0e142e06
%bcond check 1
%global debug_package %{nil}
%global crate async-fs
Name:           rust-async-fs1
Version:        1.6.0
Release:        1%{?dist}
Summary:        Async filesystem primitives
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/async-fs
Source0:        https://static.crates.io/crates/async-fs/async-fs-%{version}.crate
Patch:          async-fs-fix-metadata-auto.diff
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
Summary:        Async filesystem primitives
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
%files -n rust-async-fs1-devel -f %{oreon_filedir}/rust-async-fs1-devel.list

%changelog

%autochangelog

%global source1_hash db6d163be642e3b568c5fb2104013da632316ecd4e75935df1613af8b0b37933
%global source0_hash d5b392838cfe8858e86fac37cf97a0e8c55cc60ba0a18365cadc33092f128ce9
%bcond check 0
%global debug_package %{nil}
%global crate lmdb-sys
Name:           rust-lmdb-sys
Version:        0.8.0
Release:        1%{?dist}
Summary:        Rust bindings for liblmdb
License:        Apache-2.0
URL:            https://crates.io/crates/lmdb-sys
Source0:        https://static.crates.io/crates/lmdb-sys/lmdb-sys-%{version}.crate
Source1:        https://github.com/danburkert/lmdb-rs/raw/%{version}/LICENSE
Patch:          lmdb-sys-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(lmdb)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(lmdb)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust bindings for liblmdb
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -rv lmdb/
sed -i -e "/pkg_config/s/liblmdb/lmdb/" build.rs
cp -pav %{SOURCE1} .
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
%files -n rust-lmdb-sys-devel -f %{oreon_filedir}/rust-lmdb-sys-devel.list

%changelog

%autochangelog

%global source0_hash faeaa693e5a727975a79211b8f35c0cb09b031fdb6eaa4a788bc6713d01488ca
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate cbindgen
Name:           rust-cbindgen0.25
Version:        0.25.0
Release:        1%{?dist}
Summary:        Tool for generating C bindings to Rust code
License:        MPL-2.0
URL:            https://crates.io/crates/cbindgen
Source0:        https://static.crates.io/crates/cbindgen/cbindgen-%{version}.crate
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
Summary:        Tool for generating C bindings to Rust code
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        Tool for generating C bindings to Rust code
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

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
%files -n rust-cbindgen0.25-devel -f %{oreon_filedir}/rust-cbindgen0.25-devel.list

%changelog

%autochangelog

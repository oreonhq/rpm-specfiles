%global source0_hash da6bc11b07529f16944307272d5bd9b22530bc7d05751717c9d416586cedab49
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate cbindgen
Name:           rust-cbindgen0.26
Version:        0.26.0
Release:        1%{?dist}
Summary:        Tool for generating C bindings to Rust code
License:        MPL-2.0
URL:            https://crates.io/crates/cbindgen
Source0:        https://static.crates.io/crates/cbindgen/cbindgen-%{version}.crate
Patch:          cbindgen-fix-metadata.diff
%if %{with check}
%endif
# oreon:deps
BuildRequires:  /usr/bin/cython
BuildRequires:  /usr/bin/g++
BuildRequires:  /usr/bin/gcc
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
%files -n rust-cbindgen0.26-devel -f %{oreon_filedir}/rust-cbindgen0.26-devel.list

%changelog

%autochangelog

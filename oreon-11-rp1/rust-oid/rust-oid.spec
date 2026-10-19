%global source0_hash 33a7fe45463ee4732d4875f0e354d894895fad6fc8f5c7b3684addb2fe7b658c
%bcond check 0
%global debug_package %{nil}
%global crate oid
Name:           rust-oid
Version:        0.3.0
Release:        1%{?dist}
Summary:        Rust-native library for building, parsing, and formating Object Ident...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/oid
Source0:        https://static.crates.io/crates/oid/oid-%{version}.crate
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
Summary:        Rust-native library for building, parsing, and formating Object Ident...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Rust-native library for building, parsing, and formating Object Ident...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rust-native library for building, parsing, and formating Object Ident...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+u32-devel
Summary:        Rust-native library for building, parsing, and formating Object Ident...
BuildArch:      noarch
%description -n %{name}+u32-devel

This package contains library source intended for building other packages which
use the "u32" feature of the "%{crate}" crate.

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
%files -n rust-oid-devel -f %{oreon_filedir}/rust-oid-devel.list

%changelog

%autochangelog

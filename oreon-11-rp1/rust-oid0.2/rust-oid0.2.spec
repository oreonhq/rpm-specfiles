%global source0_hash 9c19903c598813dba001b53beeae59bb77ad4892c5c1b9b3500ce4293a0d06c2
%bcond check 1
%global debug_package %{nil}
%global crate oid
Name:           rust-oid0.2
Version:        0.2.1
Release:        1%{?dist}
Summary:        Rust-native library for building, parsing, and formating Object Identifiers
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
Summary:        Rust-native library for building, parsing, and formating Object Identifiers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Rust-native library for building, parsing, and formating Object Identifiers
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_support-devel
Summary:        Rust-native library for building, parsing, and formating Object Identifiers
BuildArch:      noarch
%description -n %{name}+serde_support-devel

This package contains library source intended for building other packages which
use the "serde_support" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rust-native library for building, parsing, and formating Object Identifiers
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+u32-devel
Summary:        Rust-native library for building, parsing, and formating Object Identifiers
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
%files -n rust-oid0.2-devel -f %{oreon_filedir}/rust-oid0.2-devel.list

%changelog

%autochangelog

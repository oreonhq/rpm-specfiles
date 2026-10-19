%global source0_hash 2d8ff746c5b65d4bfb3a50f630b85cfb6a9d59f18720126e3ebd6bc98527fa51
%bcond check 1
%global crate varlink_generator
Name:           rust-varlink_generator
Version:        10.1.0
Release:        1%{?dist}
Summary:        Rust code generator for the varlink protocol
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/varlink_generator
Source0:        https://static.crates.io/crates/varlink_generator/varlink_generator-%{version}.crate
Source1:        LICENSE.dependencies
ExclusiveArch:  %{rust_arches}
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Rust code generator for the varlink protocol
License:        MIT
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust code generator for the varlink protocol
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp %{SOURCE1} .
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n varlink_generator -f %{oreon_filedir}/varlink_generator.list
%files -n rust-varlink_generator-devel -f %{oreon_filedir}/rust-varlink_generator-devel.list

%changelog

%autochangelog

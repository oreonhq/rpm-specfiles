%global source0_hash b3b854b0e584ead1a33f18b2fcad7cf7be18b3875c78816b753639aa501513ae
%bcond check 0
%global debug_package %{nil}
%global crate generator
Name:           rust-generator
Version:        0.8.9
Release:        1%{?dist}
Summary:        Stackfull Generator Library in Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/generator
Source0:        https://static.crates.io/crates/generator/generator-%{version}.crate
Patch:          generator-fix-metadata-auto.diff
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
Summary:        Stackfull Generator Library in Rust
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
%files -n rust-generator-devel -f %{oreon_filedir}/rust-generator-devel.list

%changelog

%autochangelog

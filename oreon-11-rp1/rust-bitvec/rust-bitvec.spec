%global source0_hash ddcec3d12c579d40898fe0a9a358a803c23e9c52ca3c425707f81c9436211837
%bcond check 0
%global debug_package %{nil}
%global crate bitvec
Name:           rust-bitvec
Version:        1.1.1
Release:        1%{?dist}
Summary:        Addresses memory by bits, for packed collections and bitfields
License:        MIT
URL:            https://crates.io/crates/bitvec
Source0:        https://static.crates.io/crates/bitvec/bitvec-%{version}.crate
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
Summary:        Addresses memory by bits, for packed collections and bitfields
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Addresses memory by bits, for packed collections and bitfields
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+atomic-devel
Summary:        Addresses memory by bits, for packed collections and bitfields
BuildArch:      noarch
%description -n %{name}+atomic-devel

This package contains library source intended for building other packages which
use the "atomic" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Addresses memory by bits, for packed collections and bitfields
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Addresses memory by bits, for packed collections and bitfields
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+testing-devel
Summary:        Addresses memory by bits, for packed collections and bitfields
BuildArch:      noarch
%description -n %{name}+testing-devel

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

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
%files -n rust-bitvec-devel -f %{oreon_filedir}/rust-bitvec-devel.list

%changelog

%autochangelog

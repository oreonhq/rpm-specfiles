%global source0_hash 7575182f7272186991736b70173b0ea045398f984bf5ebbb3804736ce1330c9d
%bcond check 0
%global debug_package %{nil}
%global crate byte-slice-cast
Name:           rust-byte-slice-cast
Version:        1.2.3
Release:        1%{?dist}
Summary:        Safely cast bytes slices from/to slices of built-in fundamental numer...
License:        MIT
URL:            https://crates.io/crates/byte-slice-cast
Source0:        https://static.crates.io/crates/byte-slice-cast/byte-slice-cast-%{version}.crate
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
Summary:        Safely cast bytes slices from/to slices of built-in fundamental numer...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Safely cast bytes slices from/to slices of built-in fundamental numer...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-byte-slice-cast-devel -f %{oreon_filedir}/rust-byte-slice-cast-devel.list

%changelog

%autochangelog

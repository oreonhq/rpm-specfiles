%global source0_hash 869b0adbda23651a9c5c0c3d270aac9fcb52e8622a8f2b17e57802d7791962f2
%bcond check 0
%global debug_package %{nil}
%global crate endian-type
Name:           rust-endian-type
Version:        0.2.0
Release:        1%{?dist}
Summary:        Type safe wrappers for types with a defined byte order
License:        MIT
URL:            https://crates.io/crates/endian-type
Source0:        https://static.crates.io/crates/endian-type/endian-type-%{version}.crate
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
Summary:        Type safe wrappers for types with a defined byte order
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
%files -n rust-endian-type-devel -f %{oreon_filedir}/rust-endian-type-devel.list

%changelog

%autochangelog

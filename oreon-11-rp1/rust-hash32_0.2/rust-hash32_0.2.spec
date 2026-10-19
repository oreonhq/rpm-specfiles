%global source0_hash 8e4e11d13d42fc8d55326b323c63978c75721fbbb695a6e6686765bcb8b33917
%bcond check 0
%global debug_package %{nil}
%global crate hash32
Name:           rust-hash32_0.2
Version:        1.0.0
Release:        1%{?dist}
Summary:        32-bit hashing machinery
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hash32
Source0:        https://static.crates.io/crates/hash32/hash32-%{version}.crate
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
Summary:        32-bit hashing machinery
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
%files -n rust-hash32_0.2-devel -f %{oreon_filedir}/rust-hash32_0.2-devel.list

%changelog

%autochangelog

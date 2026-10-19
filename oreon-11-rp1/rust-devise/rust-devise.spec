%global source0_hash f1d90b0c4c777a2cad215e3c7be59ac7c15adf45cf76317009b7d096d46f651d
%bcond check 0
%global debug_package %{nil}
%global crate devise
Name:           rust-devise
Version:        0.4.2
Release:        1%{?dist}
Summary:        A library for devising derives and other procedural macros.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/devise
Source0:        https://static.crates.io/crates/devise/devise-%{version}.crate
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
Summary:        A library for devising derives and other procedural macros.
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
%files -n rust-devise-devel -f %{oreon_filedir}/rust-devise-devel.list

%changelog

%autochangelog

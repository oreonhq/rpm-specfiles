%global source0_hash 643f8f41a8ebc4c5dc4515c82bb8abd397b527fc20fd681b7c011c2aee5d44fb
%bcond check 0
%global debug_package %{nil}
%global crate radium
Name:           rust-radium0.6
Version:        0.6.2
Release:        1%{?dist}
Summary:        Portable interfaces for maybe-atomic types
License:        MIT
URL:            https://crates.io/crates/radium
Source0:        https://static.crates.io/crates/radium/radium-%{version}.crate
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
Summary:        Portable interfaces for maybe-atomic types
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
%files -n rust-radium0.6-devel -f %{oreon_filedir}/rust-radium0.6-devel.list

%changelog

%autochangelog

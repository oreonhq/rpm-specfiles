%global source0_hash f4987bdc12753382e0bec4a65c50738ffaabc998b9cdd1f952fb5f39b0048a96
%bcond check 1
%global debug_package %{nil}
%global crate universal-hash
Name:           rust-universal-hash0.6
Version:        0.6.1
Release:        1%{?dist}
Summary:        Traits which describe the functionality of universal hash functions
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/universal-hash
Source0:        https://static.crates.io/crates/universal-hash/universal-hash-%{version}.crate
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
Summary:        Traits which describe the functionality of universal hash functions
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
%files -n rust-universal-hash0.6-devel -f %{oreon_filedir}/rust-universal-hash0.6-devel.list

%changelog

%autochangelog

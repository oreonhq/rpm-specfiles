%global source0_hash bba18ee93d577a8428902687bcc2b6b45a56b1981a1f6d779731c86cc4c5db18
%bcond check 0
%global debug_package %{nil}
%global crate claims
Name:           rust-claims
Version:        0.8.0
Release:        1%{?dist}
Summary:        Additional assertion macros for testing
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/claims
Source0:        https://static.crates.io/crates/claims/claims-%{version}.crate
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
Summary:        Additional assertion macros for testing
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
%files -n rust-claims-devel -f %{oreon_filedir}/rust-claims-devel.list

%changelog

%autochangelog

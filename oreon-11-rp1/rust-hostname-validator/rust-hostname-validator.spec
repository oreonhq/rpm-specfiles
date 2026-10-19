%global source0_hash f558a64ac9af88b5ba400d99b579451af0d39c6d360980045b91aac966d705e2
%bcond check 0
%global debug_package %{nil}
%global crate hostname-validator
Name:           rust-hostname-validator
Version:        1.1.1
Release:        1%{?dist}
Summary:        Validate hostnames according to IETF RFC 1123
License:        MIT
URL:            https://crates.io/crates/hostname-validator
Source0:        https://static.crates.io/crates/hostname-validator/hostname-validator-%{version}.crate
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
Summary:        Validate hostnames according to IETF RFC 1123
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
%files -n rust-hostname-validator-devel -f %{oreon_filedir}/rust-hostname-validator-devel.list

%changelog

%autochangelog

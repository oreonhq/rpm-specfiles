%global source0_hash 35fb9f3c1e8ccb33cdb6c84a4477ef3f3884ce6f4b70514ef1fbf7686eae921e
%bcond check 0
%global debug_package %{nil}
%global crate varlink_parser
Name:           rust-varlink_parser
Version:        4.2.0
Release:        1%{?dist}
Summary:        Crate for parsing varlink interface definition files
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/varlink_parser
Source0:        https://static.crates.io/crates/varlink_parser/varlink_parser-%{version}.crate
ExclusiveArch:  %{rust_arches}
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
Summary:        Crate for parsing varlink interface definition files
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
%files -n rust-varlink_parser-devel -f %{oreon_filedir}/rust-varlink_parser-devel.list

%changelog

%autochangelog

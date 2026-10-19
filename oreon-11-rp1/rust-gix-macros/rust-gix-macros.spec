%global source0_hash d3836b4b051393464a753c5a08fe19c7ce0d8b77574a92bd558972941d4553cb
%bcond check 0
%global debug_package %{nil}
%global crate gix-macros
Name:           rust-gix-macros
Version:        0.1.6
Release:        1%{?dist}
Summary:        Proc-macro utilities for gix
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-macros
Source0:        https://static.crates.io/crates/gix-macros/gix-macros-%{version}.crate
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
Summary:        Proc-macro utilities for gix
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
%files -n rust-gix-macros-devel -f %{oreon_filedir}/rust-gix-macros-devel.list

%changelog

%autochangelog

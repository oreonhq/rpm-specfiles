%global source0_hash 136d3e02915a2cea4d74caa8681e2d44b1c3254bdbf17d11d41d587ff858832c
%bcond check 1
%global debug_package %{nil}
%global crate constcat
Name:           rust-constcat
Version:        0.6.1
Release:        1%{?dist}
Summary:        Concat! with support for const variables and expressions
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/constcat
Source0:        https://static.crates.io/crates/constcat/constcat-%{version}.crate
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
Summary:        Concat! with support for const variables and expressions
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
%files -n rust-constcat-devel -f %{oreon_filedir}/rust-constcat-devel.list

%changelog

%autochangelog

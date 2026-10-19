%global source0_hash 3f8ebf5827e4ac4fd5946560e6a99776ea73b596d80898f357007317a7141e47
%bcond check 1
%global debug_package %{nil}
%global crate argparse
Name:           rust-argparse
Version:        0.2.2
Release:        1%{?dist}
Summary:        Powerful command-line argument parsing library
License:        MIT
URL:            https://crates.io/crates/argparse
Source0:        https://static.crates.io/crates/argparse/argparse-%{version}.crate
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
Summary:        Powerful command-line argument parsing library
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
%files -n rust-argparse-devel -f %{oreon_filedir}/rust-argparse-devel.list

%changelog

%autochangelog

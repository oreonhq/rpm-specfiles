%global source0_hash 219e3ce6f2611d83b51ec2098a12702112c29e57203a6b0a0929b2cddb486608
%bcond check 0
%global debug_package %{nil}
%global crate ansi-width
Name:           rust-ansi-width
Version:        0.1.0
Release:        1%{?dist}
Summary:        Calculate the width of a string when printed to the terminal
License:        MIT
URL:            https://crates.io/crates/ansi-width
Source0:        https://static.crates.io/crates/ansi-width/ansi-width-%{version}.crate
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
Summary:        Calculate the width of a string when printed to the terminal
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
%files -n rust-ansi-width-devel -f %{oreon_filedir}/rust-ansi-width-devel.list

%changelog

%autochangelog

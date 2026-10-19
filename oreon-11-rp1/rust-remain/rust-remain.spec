%global source0_hash d7ef12e84481ab4006cb942f8682bba28ece7270743e649442027c5db87df126
%bcond check 1
%global debug_package %{nil}
%global crate remain
Name:           rust-remain
Version:        0.2.15
Release:        1%{?dist}
Summary:        Compile-time checks that an enum, struct, or match is written in sorted order
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/remain
Source0:        https://static.crates.io/crates/remain/remain-%{version}.crate
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
Summary:        Compile-time checks that an enum, struct, or match is written in sorted order
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
%files -n rust-remain-devel -f %{oreon_filedir}/rust-remain-devel.list

%changelog

%autochangelog

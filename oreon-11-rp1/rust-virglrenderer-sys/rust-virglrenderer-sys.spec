%global source0_hash 5e1cd0732acd1881433c4689bb2d359d64b9a64ddf64ab7231d9db35edbd181a
%bcond check 1
%global debug_package %{nil}
%global crate virglrenderer-sys
Name:           rust-virglrenderer-sys
Version:        0.1.3
Release:        1%{?dist}
Summary:        Raw FFI bindings for the virglrenderer C library
License:        MIT
URL:            https://crates.io/crates/virglrenderer-sys
Source0:        https://static.crates.io/crates/virglrenderer-sys/virglrenderer-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(virglrenderer)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(virglrenderer) >= 0.10
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Raw FFI bindings for the virglrenderer C library
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
%files -n rust-virglrenderer-sys-devel -f %{oreon_filedir}/rust-virglrenderer-sys-devel.list

%changelog

%autochangelog

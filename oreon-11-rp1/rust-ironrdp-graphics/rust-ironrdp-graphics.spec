%global source0_hash 2e4e16e0158fc71e20c59d955793dc8563a1274102ee9f82c234d8f95d569b4d
%bcond check 0
%global debug_package %{nil}
%global crate ironrdp-graphics
Name:           rust-ironrdp-graphics
Version:        0.4.1
Release:        1%{?dist}
Summary:        RDP image processing primitives
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp-graphics
Source0:        https://static.crates.io/crates/ironrdp-graphics/ironrdp-graphics-%{version}.crate
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
Summary:        RDP image processing primitives
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
%files -n rust-ironrdp-graphics-devel -f %{oreon_filedir}/rust-ironrdp-graphics-devel.list

%changelog

%autochangelog

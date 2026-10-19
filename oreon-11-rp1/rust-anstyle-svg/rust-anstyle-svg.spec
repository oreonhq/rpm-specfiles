%global source0_hash ab68e0b71ea68eb6b399ffe1957f26330aeed91f5e578d442a1c2f3df69f6ec1
%bcond check 1
%global debug_package %{nil}
%global crate anstyle-svg
Name:           rust-anstyle-svg
Version:        1.1.1
Release:        1%{?dist}
Summary:        Convert ANSI escape codes to SVG
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/anstyle-svg
Source0:        https://static.crates.io/crates/anstyle-svg/anstyle-svg-%{version}.crate
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
Summary:        Convert ANSI escape codes to SVG
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
%files -n rust-anstyle-svg-devel -f %{oreon_filedir}/rust-anstyle-svg-devel.list

%changelog

%autochangelog

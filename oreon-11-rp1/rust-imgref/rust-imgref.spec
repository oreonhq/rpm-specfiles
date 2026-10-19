%global source0_hash 6e44b0a4eaa4c82f441d50a963f2d5f05a787240aeee097597033e72accfd22f
%bcond check 0
%global debug_package %{nil}
%global crate imgref
Name:           rust-imgref
Version:        1.12.3
Release:        1%{?dist}
Summary:        A basic 2-dimensional slice for safe and convenient handling of pixel...
License:        CC0-1.0 OR Apache-2.0
URL:            https://crates.io/crates/imgref
Source0:        https://static.crates.io/crates/imgref/imgref-%{version}.crate
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
Summary:        A basic 2-dimensional slice for safe and convenient handling of pixel...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+deprecated-devel
Summary:        A basic 2-dimensional slice for safe and convenient handling of pixel...
BuildArch:      noarch
%description -n %{name}+deprecated-devel

This package contains library source intended for building other packages which
use the "deprecated" feature of the "%{crate}" crate.

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
%files -n rust-imgref-devel -f %{oreon_filedir}/rust-imgref-devel.list

%changelog

%autochangelog

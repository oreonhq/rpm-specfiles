%global source0_hash 2d3a81ed245bfb62592b1e2bc153e77656d94ee6a0497683a65a12ccaf2438d0
%bcond check 0
%global debug_package %{nil}
%global crate tracing-journald
Name:           rust-tracing-journald
Version:        0.3.2
Release:        1%{?dist}
Summary:        Rich journald subscriber for tracing
License:        MIT
URL:            https://crates.io/crates/tracing-journald
Source0:        https://static.crates.io/crates/tracing-journald/tracing-journald-%{version}.crate
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
Summary:        Rich journald subscriber for tracing
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
%files -n rust-tracing-journald-devel -f %{oreon_filedir}/rust-tracing-journald-devel.list

%changelog

%autochangelog

%global source0_hash 9171a2ea8a68358193d15dd5d70c1c10a2afc3e7e4c5bc92bc9f025cebd7359c
%bcond check 0
%global debug_package %{nil}
%global crate http-range-header
Name:           rust-http-range-header
Version:        0.4.2
Release:        1%{?dist}
Summary:        No-dep range header parser
License:        MIT
URL:            https://crates.io/crates/http-range-header
Source0:        https://static.crates.io/crates/http-range-header/http-range-header-%{version}.crate
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
Summary:        No-dep range header parser
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
%files -n rust-http-range-header-devel -f %{oreon_filedir}/rust-http-range-header-devel.list

%changelog

%autochangelog

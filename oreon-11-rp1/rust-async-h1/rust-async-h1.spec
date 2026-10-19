%global source0_hash 5d1d1dae8cb2c4258a79d6ed088b7fb9b4763bf4e9b22d040779761e046a2971
%bcond check 0
%global debug_package %{nil}
%global crate async-h1
Name:           rust-async-h1
Version:        2.3.4
Release:        1%{?dist}
Summary:        Asynchronous HTTP 1.1 parser.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/async-h1
Source0:        https://static.crates.io/crates/async-h1/async-h1-%{version}.crate
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
Summary:        Asynchronous HTTP 1.1 parser.
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
%files -n rust-async-h1-devel -f %{oreon_filedir}/rust-async-h1-devel.list

%changelog

%autochangelog

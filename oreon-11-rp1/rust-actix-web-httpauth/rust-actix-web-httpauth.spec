%global source0_hash 456348ed9dcd72a13a1f4a660449fafdecee9ac8205552e286809eb5b0b29bd3
%bcond check 0
%global debug_package %{nil}
%global crate actix-web-httpauth
Name:           rust-actix-web-httpauth
Version:        0.8.2
Release:        1%{?dist}
Summary:        HTTP authentication schemes for Actix Web
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-web-httpauth
Source0:        https://static.crates.io/crates/actix-web-httpauth/actix-web-httpauth-%{version}.crate
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
Summary:        HTTP authentication schemes for Actix Web
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
%files -n rust-actix-web-httpauth-devel -f %{oreon_filedir}/rust-actix-web-httpauth-devel.list

%changelog

%autochangelog

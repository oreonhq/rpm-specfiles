%global source0_hash 7a467a31a9f439b5262fa99c17084537bff57f24703d5a09a2b5c9657ec73a61
%bcond check 1
%global debug_package %{nil}
%global crate ini_core
Name:           rust-ini_core
Version:        0.2.0
Release:        1%{?dist}
Summary:        Implements a pretty bare-bones streaming INI parser
License:        MIT
URL:            https://crates.io/crates/ini_core
Source0:        https://static.crates.io/crates/ini_core/ini_core-%{version}.crate
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
Summary:        Implements a pretty bare-bones streaming INI parser
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
%files -n rust-ini_core-devel -f %{oreon_filedir}/rust-ini_core-devel.list

%changelog

%autochangelog

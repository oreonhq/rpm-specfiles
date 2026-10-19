%global source0_hash 94b0131ea5e4b75d6f8f79b82658a99ab9133d6877994288bbab9d0a01bbbe4e
%bcond check 1
%global debug_package %{nil}
%global crate sequoia-wot
Name:           rust-sequoia-wot0.15
Version:        0.15.3
Release:        1%{?dist}
Summary:        Implementation of OpenPGP's web of trust
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-wot
Source0:        https://static.crates.io/crates/sequoia-wot/sequoia-wot-%{version}.crate
Patch:          sequoia-wot-fix-metadata-auto.diff
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
Summary:        Implementation of OpenPGP's web of trust
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
%files -n rust-sequoia-wot0.15-devel -f %{oreon_filedir}/rust-sequoia-wot0.15-devel.list

%changelog

%autochangelog

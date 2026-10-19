%global source0_hash 54ecc2eeefc0ccbba225e6e57ef1cde9df78e55b315e71fd95ebebc5bd1dbbb6
%bcond check 0
%global debug_package %{nil}
%global crate sequoia-policy-config
Name:           rust-sequoia-policy-config
Version:        0.8.2
Release:        1%{?dist}
Summary:        Configure Sequoia using a configuration file.
License:        LGPL-2.0-or-later
URL:            https://crates.io/crates/sequoia-policy-config
Source0:        https://static.crates.io/crates/sequoia-policy-config/sequoia-policy-config-%{version}.crate
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
Summary:        Configure Sequoia using a configuration file.
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
%files -n rust-sequoia-policy-config-devel -f %{oreon_filedir}/rust-sequoia-policy-config-devel.list

%changelog

%autochangelog

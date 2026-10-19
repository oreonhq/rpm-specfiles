%global source0_hash 62d6408d1406657be2f9d1701fbae379331d30d2f6e92050710edb0d34eeb480
%global debug_package %{nil}
%bcond check 1
%global crate test-strategy
Name:           rust-test-strategy0.2
Version:        0.2.1
Release:        1%{?dist}
Summary:        Procedural macro to easily write higher-order strategies in proptest
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/test-strategy
Source0:        https://static.crates.io/crates/test-strategy/test-strategy-%{version}.crate
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
Summary:        Procedural macro to easily write higher-order strategies in proptest
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-test-strategy0.2-devel -f %{oreon_filedir}/rust-test-strategy0.2-devel.list

%changelog

%autochangelog

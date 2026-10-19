%global source0_hash 9224be3459a0c1d6e9b0f42ab0e76e98b29aef5aba33c0487dfcf47ea08b5150
%bcond check 1
%global debug_package %{nil}
%global crate ntest_timeout
Name:           rust-ntest_timeout
Version:        0.9.5
Release:        1%{?dist}
Summary:        Timeout attribute for the ntest framework
License:        MIT
URL:            https://crates.io/crates/ntest_timeout
Source0:        https://static.crates.io/crates/ntest_timeout/ntest_timeout-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Timeout attribute for the ntest framework
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
dos2unix --keepdate README.md LICENSE src/lib.rs tests/timeout.rs
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
%files -n rust-ntest_timeout-devel -f %{oreon_filedir}/rust-ntest_timeout-devel.list

%changelog

%autochangelog

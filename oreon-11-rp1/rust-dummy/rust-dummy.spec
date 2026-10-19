%global source0_hash 6d2a69babd8861dbe09217678b4e8ee461869f9af8a57021e16479628dbd83bd
%bcond check 1
%global debug_package %{nil}
%global crate dummy
Name:           rust-dummy
Version:        0.12.0
Release:        1%{?dist}
Summary:        Macros implementation of #[derive(Dummy)]
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/dummy
Source0:        https://static.crates.io/crates/dummy/dummy-%{version}.crate
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
Summary:        Macros implementation of #[derive(Dummy)]
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
dos2unix --keepdate README.md src/lib.rs
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
%files -n rust-dummy-devel -f %{oreon_filedir}/rust-dummy-devel.list

%changelog

%autochangelog

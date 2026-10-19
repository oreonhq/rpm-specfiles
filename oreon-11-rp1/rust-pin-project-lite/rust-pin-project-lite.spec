%global source0_hash a89322df9ebe1c1578d689c92318e070967d1042b512afbe49518723f4e6d5cd
%bcond check 0
%global debug_package %{nil}
%global crate pin-project-lite
Name:           rust-pin-project-lite
Version:        0.2.17
Release:        1%{?dist}
Summary:        Lightweight version of pin-project written with declarative macros
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/pin-project-lite
Source0:        https://static.crates.io/crates/pin-project-lite/pin-project-lite-%{version}.crate
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
Summary:        Lightweight version of pin-project written with declarative macros
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
%files -n rust-pin-project-lite-devel -f %{oreon_filedir}/rust-pin-project-lite-devel.list

%changelog

%autochangelog

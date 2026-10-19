%global source0_hash 3a449064fee414fcc201356a3e6c1510f6c8829ed28bb06b91c54ebe208ce065
%bcond check 1
%global debug_package %{nil}
%global crate version
Name:           rust-version
Version:        3.0.0
Release:        1%{?dist}
Summary:        Very simple library who's job is to return the version of your crate if you're building with Cargo
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/version
Source0:        https://static.crates.io/crates/version/version-%{version}.crate
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
Summary:        Very simple library who's job is to return the version of your crate if you're building with Cargo
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
%files -n rust-version-devel -f %{oreon_filedir}/rust-version-devel.list

%changelog

%autochangelog

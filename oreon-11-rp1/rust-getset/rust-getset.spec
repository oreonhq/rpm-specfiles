%global source0_hash 6cf442baaabe4213ce7d1239afc26c039180b6456da2cededa316ae2c8a77a77
%bcond check 1
%global debug_package %{nil}
%global crate getset
Name:           rust-getset
Version:        0.1.7
Release:        1%{?dist}
Summary:        Procedural macro for generating the most basic getters and setters on fields
License:        MIT
URL:            https://crates.io/crates/getset
Source0:        https://static.crates.io/crates/getset/getset-%{version}.crate
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
Summary:        Procedural macro for generating the most basic getters and setters on fields
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
%files -n rust-getset-devel -f %{oreon_filedir}/rust-getset-devel.list

%changelog

%autochangelog

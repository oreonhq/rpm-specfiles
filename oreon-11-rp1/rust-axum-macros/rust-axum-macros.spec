%global source0_hash 7aa268c23bfbbd2c4363b9cd302a4f504fb2a9dfe7e3451d66f35dd392e20aca
%bcond check 0
%global debug_package %{nil}
%global crate axum-macros
Name:           rust-axum-macros
Version:        0.5.1
Release:        1%{?dist}
Summary:        Macros for axum
License:        MIT
URL:            https://crates.io/crates/axum-macros
Source0:        https://static.crates.io/crates/axum-macros/axum-macros-%{version}.crate
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
Summary:        Macros for axum
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__private-devel
Summary:        Macros for axum
BuildArch:      noarch
%description -n %{name}+__private-devel

This package contains library source intended for building other packages which
use the "__private" feature of the "%{crate}" crate.

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
%files -n rust-axum-macros-devel -f %{oreon_filedir}/rust-axum-macros-devel.list

%changelog

%autochangelog

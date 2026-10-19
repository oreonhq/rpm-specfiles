%global source0_hash e44da00bfc73a25f814cd8d7e57a68a5c31b74b3152a0a1d1f590c97ed06265a
%bcond check 0
%global debug_package %{nil}
%global crate tokio-macros
Name:           rust-tokio-macros0.2
Version:        0.2.6
Release:        1%{?dist}
Summary:        Tokio's proc macros.
License:        MIT
URL:            https://crates.io/crates/tokio-macros
Source0:        https://static.crates.io/crates/tokio-macros/tokio-macros-%{version}.crate
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
Summary:        Tokio's proc macros.
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
%files -n rust-tokio-macros0.2-devel -f %{oreon_filedir}/rust-tokio-macros0.2-devel.list

%changelog

%autochangelog

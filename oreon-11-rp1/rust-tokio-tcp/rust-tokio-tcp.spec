%global source0_hash 98df18ed66e3b72e742f185882a9e201892407957e45fbff8da17ae7a7c51f72
%bcond check 0
%global debug_package %{nil}
%global crate tokio-tcp
Name:           rust-tokio-tcp
Version:        0.1.4
Release:        1%{?dist}
Summary:        TCP bindings for tokio.
License:        MIT
URL:            https://crates.io/crates/tokio-tcp
Source0:        https://static.crates.io/crates/tokio-tcp/tokio-tcp-%{version}.crate
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
Summary:        TCP bindings for tokio.
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
%files -n rust-tokio-tcp-devel -f %{oreon_filedir}/rust-tokio-tcp-devel.list

%changelog

%autochangelog

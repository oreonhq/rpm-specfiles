%global source0_hash 19c97a761fc86953c5b885422b22c891dbf5bcb9dcc99d0110d6ce4c052759f0
%bcond check 0
%global debug_package %{nil}
%global crate libsystemd
Name:           rust-libsystemd
Version:        0.7.2
Release:        1%{?dist}
Summary:        A pure-Rust client library to interact with systemd
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/libsystemd
Source0:        https://static.crates.io/crates/libsystemd/libsystemd-%{version}.crate
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
Summary:        A pure-Rust client library to interact with systemd
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
%files -n rust-libsystemd-devel -f %{oreon_filedir}/rust-libsystemd-devel.list

%changelog

%autochangelog

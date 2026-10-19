%global source0_hash 9b3a41ce106832b4da1c065baa4c31cf640cf965fa1483816402b7f6b96f0a64
%bcond check 1
%global debug_package %{nil}
%global crate z85
Name:           rust-z85
Version:        3.0.6
Release:        1%{?dist}
Summary:        Rust implementation of ZeroMQ's Z85 encoding mechanism with padding
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/z85
Source0:        https://static.crates.io/crates/z85/z85-%{version}.crate
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
Summary:        Rust implementation of ZeroMQ's Z85 encoding mechanism with padding
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
%files -n rust-z85-devel -f %{oreon_filedir}/rust-z85-devel.list

%changelog

%autochangelog

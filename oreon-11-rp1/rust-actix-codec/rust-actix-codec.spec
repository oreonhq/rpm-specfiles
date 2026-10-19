%global source0_hash 5f7b0a21988c1bf877cf4759ef5ddaac04c1c9fe808c9142ecb78ba97d97a28a
%bcond check 1
%global debug_package %{nil}
%global crate actix-codec
Name:           rust-actix-codec
Version:        0.5.2
Release:        1%{?dist}
Summary:        Codec utilities for working with framed protocols
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-codec
Source0:        https://static.crates.io/crates/actix-codec/actix-codec-%{version}.crate
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
Summary:        Codec utilities for working with framed protocols
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
%files -n rust-actix-codec-devel -f %{oreon_filedir}/rust-actix-codec-devel.list

%changelog

%autochangelog

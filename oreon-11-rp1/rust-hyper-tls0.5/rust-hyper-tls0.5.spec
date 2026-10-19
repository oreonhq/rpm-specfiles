%global source0_hash d6183ddfa99b85da61a140bea0efc93fdf56ceaa041b37d553518030827f9905
%bcond check 0
%global debug_package %{nil}
%global crate hyper-tls
Name:           rust-hyper-tls0.5
Version:        0.5.0
Release:        1%{?dist}
Summary:        Default TLS implementation for use with hyper
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hyper-tls
Source0:        https://static.crates.io/crates/hyper-tls/hyper-tls-%{version}.crate
Patch:          hyper-tls-fix-metadata.diff
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
Summary:        Default TLS implementation for use with hyper
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
%files -n rust-hyper-tls0.5-devel -f %{oreon_filedir}/rust-hyper-tls0.5-devel.list

%changelog

%autochangelog

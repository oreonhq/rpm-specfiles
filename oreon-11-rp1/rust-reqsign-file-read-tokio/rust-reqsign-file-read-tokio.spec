%global source0_hash e2d89295b3d17abea31851cc8de55d843d89c52132c864963c38d41920613dc5
%bcond check 1
%global debug_package %{nil}
%global crate reqsign-file-read-tokio
Name:           rust-reqsign-file-read-tokio
Version:        3.0.0
Release:        1%{?dist}
Summary:        Tokio-based file reader implementation for reqsign
License:        Apache-2.0
URL:            https://crates.io/crates/reqsign-file-read-tokio
Source0:        https://static.crates.io/crates/reqsign-file-read-tokio/reqsign-file-read-tokio-%{version}.crate
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
Summary:        Tokio-based file reader implementation for reqsign
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
%files -n rust-reqsign-file-read-tokio-devel -f %{oreon_filedir}/rust-reqsign-file-read-tokio-devel.list

%changelog

%autochangelog

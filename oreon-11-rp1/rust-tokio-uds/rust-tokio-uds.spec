%global source0_hash 65ae5d255ce739e8537221ed2942e0445f4b3b813daebac1c0050ddaaa3587f9
%bcond check 0
%global debug_package %{nil}
%global crate tokio-uds
Name:           rust-tokio-uds
Version:        0.1.7
Release:        1%{?dist}
Summary:        Unix Domain sockets for Tokio
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tokio-uds
Source0:        https://static.crates.io/crates/tokio-uds/tokio-uds-%{version}.crate
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
Summary:        Unix Domain sockets for Tokio
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
%files -n rust-tokio-uds-devel -f %{oreon_filedir}/rust-tokio-uds-devel.list

%changelog

%autochangelog

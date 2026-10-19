%global source0_hash 8b2e732c8d91a74731663ac8479ab505042fbf547b9a207213ab7fbcbfc4f8b4
%bcond check 0
%global debug_package %{nil}
%global crate h3-quinn
Name:           rust-h3-quinn
Version:        0.0.10
Release:        1%{?dist}
Summary:        QUIC transport implementation based on Quinn.
License:        MIT
URL:            https://crates.io/crates/h3-quinn
Source0:        https://static.crates.io/crates/h3-quinn/h3-quinn-%{version}.crate
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
Summary:        QUIC transport implementation based on Quinn.
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
%files -n rust-h3-quinn-devel -f %{oreon_filedir}/rust-h3-quinn-devel.list

%changelog

%autochangelog

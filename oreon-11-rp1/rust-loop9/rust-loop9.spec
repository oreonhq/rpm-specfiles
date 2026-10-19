%global source0_hash 0fae87c125b03c1d2c0150c90365d7d6bcc53fb73a9acaef207d2d065860f062
%bcond check 0
%global debug_package %{nil}
%global crate loop9
Name:           rust-loop9
Version:        0.1.5
Release:        1%{?dist}
Summary:        Tiny helper function to visit every pixel in the image together with...
License:        MIT
URL:            https://crates.io/crates/loop9
Source0:        https://static.crates.io/crates/loop9/loop9-%{version}.crate
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
Summary:        Tiny helper function to visit every pixel in the image together with...
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
%files -n rust-loop9-devel -f %{oreon_filedir}/rust-loop9-devel.list

%changelog

%autochangelog

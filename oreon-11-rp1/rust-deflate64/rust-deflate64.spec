%global source0_hash ac6b926516df9c60bfa16e107b21086399f8285a44ca9711344b9e553c5146e2
%bcond check 1
%global debug_package %{nil}
%global crate deflate64
Name:           rust-deflate64
Version:        0.1.12
Release:        1%{?dist}
Summary:        Deflate64 implementation based on .NET's implementation
License:        MIT
URL:            https://crates.io/crates/deflate64
Source0:        https://static.crates.io/crates/deflate64/deflate64-%{version}.crate
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
Summary:        Deflate64 implementation based on .NET's implementation
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
%files -n rust-deflate64-devel -f %{oreon_filedir}/rust-deflate64-devel.list

%changelog

%autochangelog

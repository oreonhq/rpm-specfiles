%global source0_hash 284b60557f2c4a2e72ad3f2d34d42685a2fa4a6a61d0d2a10c0ae2a5e916c2cf
%bcond check 0
%global debug_package %{nil}
%global crate pest_derive
Name:           rust-pest_derive
Version:        2.9.2
Release:        1%{?dist}
Summary:        pest's derive macro
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pest_derive
Source0:        https://static.crates.io/crates/pest_derive/pest_derive-%{version}.crate
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
Summary:        pest's derive macro
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+grammar-extras-devel
Summary:        pest's derive macro
BuildArch:      noarch
%description -n %{name}+grammar-extras-devel

This package contains library source intended for building other packages which
use the "grammar-extras" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        pest's derive macro
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-pest_derive-devel -f %{oreon_filedir}/rust-pest_derive-devel.list

%changelog

%autochangelog

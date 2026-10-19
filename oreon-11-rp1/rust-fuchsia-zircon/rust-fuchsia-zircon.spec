%global source0_hash 2e9763c69ebaae630ba35f74888db465e49e259ba1bc0eda7d06f4a067615d82
%bcond check 0
%global debug_package %{nil}
%global crate fuchsia-zircon
Name:           rust-fuchsia-zircon
Version:        0.3.3
Release:        1%{?dist}
Summary:        Rust bindings for the Zircon kernel
License:        BSD-3-Clause
URL:            https://crates.io/crates/fuchsia-zircon
Source0:        https://static.crates.io/crates/fuchsia-zircon/fuchsia-zircon-%{version}.crate
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
Summary:        Rust bindings for the Zircon kernel
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
%files -n rust-fuchsia-zircon-devel -f %{oreon_filedir}/rust-fuchsia-zircon-devel.list

%changelog

%autochangelog

%global source0_hash aa68f1b12764fab894d2755d2518754e71b4fd80ecfb822714a1206c2aab39bf
%bcond check 0
%global debug_package %{nil}
%global crate errno-dragonfly
Name:           rust-errno-dragonfly
Version:        0.1.2
Release:        1%{?dist}
Summary:        Exposes errno functionality to stable Rust on DragonFlyBSD
License:        MIT
URL:            https://crates.io/crates/errno-dragonfly
Source0:        https://static.crates.io/crates/errno-dragonfly/errno-dragonfly-%{version}.crate
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
Summary:        Exposes errno functionality to stable Rust on DragonFlyBSD
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
%files -n rust-errno-dragonfly-devel -f %{oreon_filedir}/rust-errno-dragonfly-devel.list

%changelog

%autochangelog

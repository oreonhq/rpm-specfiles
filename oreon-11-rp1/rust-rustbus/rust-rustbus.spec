%global source0_hash 4054c51e241d0c6d57fab9fecda2223b7bdc7621be67f0d70568d94a6762f281
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate rustbus
Name:           rust-rustbus
Version:        0.19.3
Release:        1%{?dist}
Summary:        Implementation of the dbus protocol
License:        MIT
URL:            https://crates.io/crates/rustbus
Source0:        https://static.crates.io/crates/rustbus/rustbus-%{version}.crate
Patch:          rustbus-fix-metadata.diff
Patch2:         0001-port-to-nix-0.24.patch
Patch3:         0002-port-to-nix-0.26.patch
Patch4:         0003-port-to-nix-0.27.patch
Patch5:         0004-port-to-nix-0.28.patch
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
Summary:        Implementation of the dbus protocol
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

%cargo_test -- -- --exact --skip tests::fdpassing::test_fd_passing
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rustbus-devel -f %{oreon_filedir}/rust-rustbus-devel.list

%changelog

%autochangelog

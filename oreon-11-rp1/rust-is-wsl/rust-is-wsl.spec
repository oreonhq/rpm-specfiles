%global source0_hash 173609498df190136aa7dea1a91db051746d339e18476eed5ca40521f02d7aa5
%bcond check 0
%global debug_package %{nil}
%global crate is-wsl
Name:           rust-is-wsl
Version:        0.4.0
Release:        1%{?dist}
Summary:        Checks if the process is running inside Windows Subsystem for Linux
License:        MIT
URL:            https://crates.io/crates/is-wsl
Source0:        https://static.crates.io/crates/is-wsl/is-wsl-%{version}.crate
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
Summary:        Checks if the process is running inside Windows Subsystem for Linux
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
%files -n rust-is-wsl-devel -f %{oreon_filedir}/rust-is-wsl-devel.list

%changelog

%autochangelog

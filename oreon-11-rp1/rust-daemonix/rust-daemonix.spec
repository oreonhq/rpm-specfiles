%global source0_hash f0b747381562a10fd2104e9333ad72fe5158d79de81b64426fc9e229c6d3fb38
%bcond check 1
%global debug_package %{nil}
%global crate daemonix
Name:           rust-daemonix
Version:        0.1.0
Release:        1%{?dist}
Summary:        Spawn daemon processes on Unix-like systems
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/daemonix
Source0:        https://static.crates.io/crates/daemonix/daemonix-%{version}.crate
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
Summary:        Spawn daemon processes on Unix-like systems
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
%files -n rust-daemonix-devel -f %{oreon_filedir}/rust-daemonix-devel.list

%changelog

%autochangelog

%global source2_hash 6416b712a750e20d54b4a3248f627b4531d79a64048e97bfb3e17fee1a5215a4
%global source1_hash 502ea0f4d4fbd69d5fcea01c811c700d25008e4b4116eed1d9907706f61243fb
%global source0_hash ab8bfdaacb3c887a54d41bdf48d3af8873b3f5566469f8ba21b92057509f116e
%bcond check 0
%global debug_package %{nil}
%global crate daemonize
Name:           rust-daemonize
Version:        0.5.0
Release:        1%{?dist}
Summary:        Library to enable your code run as a daemon process on Unix-like systems
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/daemonize
Source0:        https://static.crates.io/crates/daemonize/daemonize-%{version}.crate
Source1:        https://github.com/knsd/daemonize/raw/%{version}/LICENSE-APACHE
Source2:        https://github.com/knsd/daemonize/raw/%{version}/LICENSE-MIT
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
Summary:        Library to enable your code run as a daemon process on Unix-like systems
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} %{SOURCE2} .
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
%files -n rust-daemonize-devel -f %{oreon_filedir}/rust-daemonize-devel.list

%changelog

%autochangelog

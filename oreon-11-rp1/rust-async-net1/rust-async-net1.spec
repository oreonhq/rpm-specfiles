%global source0_hash 0434b1ed18ce1cf5769b8ac540e33f01fa9471058b5e89da9e06f3c882a8c12f
%bcond check 1
%global debug_package %{nil}
%global crate async-net
Name:           rust-async-net1
Version:        1.8.0
Release:        1%{?dist}
Summary:        Async networking primitives for TCP/UDP/Unix communication
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/async-net
Source0:        https://static.crates.io/crates/async-net/async-net-%{version}.crate
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
Summary:        Async networking primitives for TCP/UDP/Unix communication
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
%files -n rust-async-net1-devel -f %{oreon_filedir}/rust-async-net1-devel.list

%changelog

%autochangelog

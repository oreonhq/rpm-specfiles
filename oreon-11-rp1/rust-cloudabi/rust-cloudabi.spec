%global source0_hash 4344512281c643ae7638bbabc3af17a11307803ec8f0fcad9fae512a8bf36467
%bcond check 0
%global debug_package %{nil}
%global crate cloudabi
Name:           rust-cloudabi
Version:        0.1.0
Release:        1%{?dist}
Summary:        Low level interface to CloudABI. Contains all syscalls and related ty...
License:        BSD-2-Clause
URL:            https://crates.io/crates/cloudabi
Source0:        https://static.crates.io/crates/cloudabi/cloudabi-%{version}.crate
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
Summary:        Low level interface to CloudABI. Contains all syscalls and related ty...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bitflags-devel
Summary:        Low level interface to CloudABI. Contains all syscalls and related ty...
BuildArch:      noarch
%description -n %{name}+bitflags-devel

This package contains library source intended for building other packages which
use the "bitflags" feature of the "%{crate}" crate.

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
%files -n rust-cloudabi-devel -f %{oreon_filedir}/rust-cloudabi-devel.list

%changelog

%autochangelog

%global source0_hash 82f29ae2f71b53ec19cc23385f8e4f3d90975195aa3d09171ba3bef7159bec27
%bcond check 0
%global debug_package %{nil}
%global crate os-release
Name:           rust-os-release
Version:        0.1.0
Release:        1%{?dist}
Summary:        Parse /etc/os-release files on Linux distributions
License:        MIT
URL:            https://crates.io/crates/os-release
Source0:        https://static.crates.io/crates/os-release/os-release-%{version}.crate
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
Summary:        Parse /etc/os-release files on Linux distributions
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
%files -n rust-os-release-devel -f %{oreon_filedir}/rust-os-release-devel.list

%changelog

%autochangelog

%global source0_hash 7576a42b06b4d1d4005aac27f93b848bda3d80b6c80a6f1aa0f494b957351b81
%bcond check 0
%global debug_package %{nil}
%global crate bootc-internal-utils
Name:           rust-bootc-internal-utils
Version:        0.0.0
Release:        1%{?dist}
Summary:        Internal implementation component of bootc; do not use
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bootc-internal-utils
Source0:        https://static.crates.io/crates/bootc-internal-utils/bootc-internal-utils-%{version}.crate
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
Summary:        Internal implementation component of bootc; do not use
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
%files -n rust-bootc-internal-utils-devel -f %{oreon_filedir}/rust-bootc-internal-utils-devel.list

%changelog

%autochangelog

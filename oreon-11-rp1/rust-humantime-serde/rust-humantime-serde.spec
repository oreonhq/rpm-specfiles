%global source0_hash 57a3db5ea5923d99402c94e9feb261dc5ee9b4efa158b0315f788cf549cc200c
%bcond check 0
%global debug_package %{nil}
%global crate humantime-serde
Name:           rust-humantime-serde
Version:        1.1.1
Release:        1%{?dist}
Summary:        Serde support for the `humantime` crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/humantime-serde
Source0:        https://static.crates.io/crates/humantime-serde/humantime-serde-%{version}.crate
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
Summary:        Serde support for the `humantime` crate
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
%files -n rust-humantime-serde-devel -f %{oreon_filedir}/rust-humantime-serde-devel.list

%changelog

%autochangelog

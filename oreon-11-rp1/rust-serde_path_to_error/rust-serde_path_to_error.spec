%global source0_hash 10a9ff822e371bb5403e391ecd83e182e0e77ba7f6fe0160b795797109d1b457
%bcond check 0
%global debug_package %{nil}
%global crate serde_path_to_error
Name:           rust-serde_path_to_error
Version:        0.1.20
Release:        1%{?dist}
Summary:        Path to the element that failed to deserialize
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_path_to_error
Source0:        https://static.crates.io/crates/serde_path_to_error/serde_path_to_error-%{version}.crate
Patch:          serde_path_to_error-fix-metadata-auto.diff
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
Summary:        Path to the element that failed to deserialize
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
%files -n rust-serde_path_to_error-devel -f %{oreon_filedir}/rust-serde_path_to_error-devel.list

%changelog

%autochangelog

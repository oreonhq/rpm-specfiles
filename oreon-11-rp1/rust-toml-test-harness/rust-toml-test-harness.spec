%global source0_hash 4e7cab3ec24fa74e8e65688f22ceb3950beed839e59c631146a8053fb0d33ab2
%bcond check 0
%global debug_package %{nil}
%global crate toml-test-harness
Name:           rust-toml-test-harness
Version:        1.14.1
Release:        1%{?dist}
Summary:        Cargo test harness for verifying TOML parsers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/toml-test-harness
Source0:        https://static.crates.io/crates/toml-test-harness/toml-test-harness-%{version}.crate
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

%package     -n %{name}+snapshot-devel
Summary:        Cargo test harness for verifying TOML parsers
BuildArch:      noarch
%description -n %{name}+snapshot-devel

This package contains library source intended for building other packages which
use the "snapshot" feature of the "%{crate}" crate.

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
%files -n rust-toml-test-harness-devel -f %{oreon_filedir}/rust-toml-test-harness-devel.list

%changelog

%autochangelog

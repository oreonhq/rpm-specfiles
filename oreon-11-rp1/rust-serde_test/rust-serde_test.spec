%global source0_hash 7f901ee573cab6b3060453d2d5f0bae4e6d628c23c0a962ff9b5f1d7c8d4f1ed
%bcond_with check
%global debug_package %{nil}
%global crate serde_test
Name:           rust-serde_test
Version:        1.0.177
Release:        1%{?dist}
Summary:        Token De/Serializer for testing De/Serialize implementations
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_test
Source0:        https://static.crates.io/crates/serde_test/serde_test-%{version}.crate
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
Summary:        Token De/Serializer for testing De/Serialize implementations
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
%files -n rust-serde_test-devel -f %{oreon_filedir}/rust-serde_test-devel.list

%changelog

%autochangelog

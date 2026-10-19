%global source0_hash 61eac17e797075f82dc4f2ca6c2b807abcb7f2b101f1fd1f627c5f1cde27b0d5
%bcond check 0
%global debug_package %{nil}
%global crate crates-io
Name:           rust-crates-io
Version:        0.41.1
Release:        1%{?dist}
Summary:        Helpers for interacting with crates.io
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/crates-io
Source0:        https://static.crates.io/crates/crates-io/crates-io-%{version}.crate
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
Summary:        Helpers for interacting with crates.io
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
%files -n rust-crates-io-devel -f %{oreon_filedir}/rust-crates-io-devel.list

%changelog

%autochangelog

%global source0_hash 1a6ceddfe3ce334925e96bf420fdb2dcee5bed6c632a168ece622676dadeaf8a
%bcond check 0
%global debug_package %{nil}
%global crate mockall
Name:           rust-mockall
Version:        0.15.0
Release:        1%{?dist}
Summary:        Powerful mock object library for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/mockall
Source0:        https://static.crates.io/crates/mockall/mockall-%{version}.crate
Patch:          mockall-fix-metadata.diff
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
Summary:        Powerful mock object library for Rust
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
%files -n rust-mockall-devel -f %{oreon_filedir}/rust-mockall-devel.list

%changelog

%autochangelog

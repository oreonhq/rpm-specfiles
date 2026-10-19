%global source0_hash b1fc3bff63c208d4a14301c6cb807af2d1a0760052584ce3f9a737b55fb85498
%bcond check 0
%global debug_package %{nil}
%global crate mbrman
Name:           rust-mbrman
Version:        0.5.4
Release:        1%{?dist}
Summary:        MBR Partition Management in Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/mbrman
Source0:        https://static.crates.io/crates/mbrman/mbrman-%{version}.crate
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
Summary:        MBR Partition Management in Rust
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
%files -n rust-mbrman-devel -f %{oreon_filedir}/rust-mbrman-devel.list

%changelog

%autochangelog

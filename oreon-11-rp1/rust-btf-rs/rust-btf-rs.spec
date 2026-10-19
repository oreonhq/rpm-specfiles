%global source0_hash fe86bb5e4b3b6428b947ecfd9bef6c504c000c0174200dc52a2df432d5fd88fc
%bcond check 0
%global debug_package %{nil}
%global crate btf-rs
Name:           rust-btf-rs
Version:        1.1.1
Release:        1%{?dist}
Summary:        Library for the BPF type format (BTF)
License:        LGPL-2.1-or-later
URL:            https://crates.io/crates/btf-rs
Source0:        https://static.crates.io/crates/btf-rs/btf-rs-%{version}.crate
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
Summary:        Library for the BPF type format (BTF)
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
%files -n rust-btf-rs-devel -f %{oreon_filedir}/rust-btf-rs-devel.list

%changelog

%autochangelog

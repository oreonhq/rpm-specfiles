%global source0_hash 62b602caaaa7782b416e6f819fe721822045a9163aa03083e6309c260f1ce9b3
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate lddtree
Name:           rust-lddtree
Version:        0.5.1
Release:        1%{?dist}
Summary:        Read the ELF dependency tree
License:        MIT
URL:            https://crates.io/crates/lddtree
Source0:        https://static.crates.io/crates/lddtree/lddtree-%{version}.crate
Patch:          lddtree-fix-metadata.diff
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
Summary:        Read the ELF dependency tree
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

%ifarch aarch64
%cargo_test -- -- --exact --skip test_lddtree
%else
%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-lddtree-devel -f %{oreon_filedir}/rust-lddtree-devel.list

%changelog

%autochangelog

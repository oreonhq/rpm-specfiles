%global source0_hash 547a362ad16dead8837d5b30402a81b05bb57c352044389f8748f4f2dbd51914
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate lddtree
Name:           rust-lddtree0.3
Version:        0.3.8
Release:        1%{?dist}
Summary:        Read the ELF dependency tree
License:        MIT
URL:            https://crates.io/crates/lddtree
Source0:        https://static.crates.io/crates/lddtree/lddtree-%{version}.crate
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-lddtree0.3-devel -f %{oreon_filedir}/rust-lddtree0.3-devel.list

%changelog

%autochangelog

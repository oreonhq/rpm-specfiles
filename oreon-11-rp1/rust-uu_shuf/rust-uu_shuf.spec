%global source0_hash 6c2e5663694fde672961884c94c8afd3cd5859969878594eda6a25059621cd97
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_shuf
Name:           rust-uu_shuf
Version:        0.7.0
Release:        1%{?dist}
Summary:        shuf ~ (uutils) display random permutations of input lines
License:        MIT
URL:            https://crates.io/crates/uu_shuf
Source0:        https://static.crates.io/crates/uu_shuf/uu_shuf-%{version}.crate
Patch:          uu_shuf-fix-metadata.diff
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
Summary:        shuf ~ (uutils) display random permutations of input lines
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
%files -n rust-uu_shuf-devel -f %{oreon_filedir}/rust-uu_shuf-devel.list

%changelog

%autochangelog

%global source0_hash 6d910bedd62c24733263d0bed247460853c9d22e8956bd4cd964302095e04e90
%bcond check 0
%global debug_package %{nil}
%global crate cedarwood
Name:           rust-cedarwood
Version:        0.4.6
Release:        1%{?dist}
Summary:        Efficiently-updatable double-array trie in Rust (ported from cedar)
License:        BSD-2-Clause
URL:            https://crates.io/crates/cedarwood
Source0:        https://static.crates.io/crates/cedarwood/cedarwood-%{version}.crate
Patch:          cedarwood-fix-metadata.diff
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
Summary:        Efficiently-updatable double-array trie in Rust (ported from cedar)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+reduced-trie-devel
Summary:        Efficiently-updatable double-array trie in Rust (ported from cedar)
BuildArch:      noarch
%description -n %{name}+reduced-trie-devel

This package contains library source intended for building other packages which
use the "reduced-trie" feature of the "%{crate}" crate.

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
%files -n rust-cedarwood-devel -f %{oreon_filedir}/rust-cedarwood-devel.list

%changelog

%autochangelog

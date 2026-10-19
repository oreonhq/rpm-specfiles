%global source0_hash 951b4e7b10349d32b7b7a26c15bd0f9cf42790b59531093d474f6964f5cba971
%bcond check 0
%global debug_package %{nil}
%global crate lv2-atom
Name:           rust-lv2-atom
Version:        2.0.0
Release:        1%{?dist}
Summary:        Rust-lv2's Atom handling library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lv2-atom
Source0:        https://static.crates.io/crates/lv2-atom/lv2-atom-%{version}.crate
ExcludeArch:    ppc64le s390x
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
Summary:        Rust-lv2's Atom handling library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+lv2-core-devel
Summary:        Rust-lv2's Atom handling library
BuildArch:      noarch
%description -n %{name}+lv2-core-devel

This package contains library source intended for building other packages which
use the "lv2-core" feature of the "%{crate}" crate.

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
rm tests/atom_integration.rs
%endif
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-lv2-atom-devel -f %{oreon_filedir}/rust-lv2-atom-devel.list

%changelog

%autochangelog

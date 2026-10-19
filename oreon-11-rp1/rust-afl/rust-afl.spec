%global source0_hash 445e8f1abdb7a5f0f9ad37c50268799568c6031537773fbe775c657cde462a95
%bcond check 0
%global debug_package %{nil}
%global crate afl
Name:           rust-afl
Version:        0.16.0
Release:        1%{?dist}
Summary:        Fuzzing Rust code with american-fuzzy-lop
License:        Apache-2.0
URL:            https://crates.io/crates/afl
Source0:        https://static.crates.io/crates/afl/afl-%{version}.crate
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

%package     -n %{name}+no_cfg_fuzzing-devel
Summary:        Fuzzing Rust code with american-fuzzy-lop
BuildArch:      noarch
%description -n %{name}+no_cfg_fuzzing-devel

This package contains library source intended for building other packages which
use the "no_cfg_fuzzing" feature of the "%{crate}" crate.

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
%files -n rust-afl-devel -f %{oreon_filedir}/rust-afl-devel.list

%changelog

%autochangelog

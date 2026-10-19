%global source0_hash b39abd59bf32521c7f2301b52d05a6a2c975b6003521cbd0c6dc1582f0a22104
%bcond check 0
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate unsafe-libyaml-norway
Name:           rust-unsafe-libyaml-norway
Version:        0.2.15
Release:        1%{?dist}
Summary:        Libyaml transpiled to rust by c2rust
License:        MIT
URL:            https://crates.io/crates/unsafe-libyaml-norway
Source0:        https://static.crates.io/crates/unsafe-libyaml-norway/unsafe-libyaml-norway-%{version}.crate
Patch2:         0001-Starting-with-Rust-1.89-2025-08-07-the-lint-dangerou.patch
Patch3:         0002-Fixed-wrong-library-name-in-README.md.patch
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
Summary:        Libyaml transpiled to rust by c2rust
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
%files -n rust-unsafe-libyaml-norway-devel -f %{oreon_filedir}/rust-unsafe-libyaml-norway-devel.list

%changelog

%autochangelog

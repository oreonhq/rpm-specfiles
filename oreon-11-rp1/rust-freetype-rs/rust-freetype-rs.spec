%global source0_hash 6d228d6de56c90dd7585341f341849441b3490180c62d27133e525eb726809b4
%bcond check 0
%global debug_package %{nil}
%global crate freetype-rs
Name:           rust-freetype-rs
Version:        0.38.0
Release:        1%{?dist}
Summary:        Bindings for FreeType font library
License:        MIT
URL:            https://crates.io/crates/freetype-rs
Source0:        https://static.crates.io/crates/freetype-rs/freetype-rs-%{version}.crate
Patch:          freetype-rs-fix-metadata.diff
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
Summary:        Bindings for FreeType font library
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
%files -n rust-freetype-rs-devel -f %{oreon_filedir}/rust-freetype-rs-devel.list

%changelog

%autochangelog

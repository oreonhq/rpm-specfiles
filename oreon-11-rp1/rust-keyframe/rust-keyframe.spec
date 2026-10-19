%global source0_hash 60708bf7981518d09095d6f5673ce5cf6a64f1e0d9708b554f670e6d9d2bd9a9
%bcond check 0
%global debug_package %{nil}
%global crate keyframe
Name:           rust-keyframe
Version:        1.1.1
Release:        1%{?dist}
Summary:        Simple library for animation in Rust
License:        MIT
URL:            https://crates.io/crates/keyframe
Source0:        https://static.crates.io/crates/keyframe/keyframe-%{version}.crate
Patch:          keyframe-fix-metadata.diff
Patch:          keyframe-remove-test.diff
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
Summary:        Simple library for animation in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Simple library for animation in Rust
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+mint-devel
Summary:        Simple library for animation in Rust
BuildArch:      noarch
%description -n %{name}+mint-devel

This package contains library source intended for building other packages which
use the "mint" feature of the "%{crate}" crate.

%package     -n %{name}+mint_types-devel
Summary:        Simple library for animation in Rust
BuildArch:      noarch
%description -n %{name}+mint_types-devel

This package contains library source intended for building other packages which
use the "mint_types" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -rf examples
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
%files -n rust-keyframe-devel -f %{oreon_filedir}/rust-keyframe-devel.list

%changelog

%autochangelog

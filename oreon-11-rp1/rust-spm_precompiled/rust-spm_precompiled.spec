%global source0_hash 5851699c4033c63636f7ea4cf7b7c1f1bf06d0cc03cfb42e711de5a5c46cf326
%bcond check 1
%global debug_package %{nil}
%global crate spm_precompiled
Name:           rust-spm_precompiled
Version:        0.1.4
Release:        1%{?dist}
Summary:        SentencePiece's DoubleArray and its Normalizer, implemented in Rust
License:        Apache-2.0
URL:            https://crates.io/crates/spm_precompiled
Source0:        https://static.crates.io/crates/spm_precompiled/spm_precompiled-%{version}.crate
Patch:          spm_precompiled-fix-metadata.diff
Patch2:         a0a1806b09f6146d433957c2e09f9f90c9b2c3da.diff
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
Summary:        SentencePiece's DoubleArray and its Normalizer, implemented in Rust
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
%files -n rust-spm_precompiled-devel -f %{oreon_filedir}/rust-spm_precompiled-devel.list

%changelog

%autochangelog

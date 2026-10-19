%global source0_hash 61c41af27dd6d1e27b1b16b489db798443478cef1f06a660c96db617ba5de3b1
%bcond check 0
%global debug_package %{nil}
%global crate target-lexicon
Name:           rust-target-lexicon0.12
Version:        0.12.16
Release:        1%{?dist}
Summary:        Targeting utilities for compilers and related tools
License:        Apache-2.0 WITH LLVM-exception
URL:            https://crates.io/crates/target-lexicon
Source0:        https://static.crates.io/crates/target-lexicon/target-lexicon-%{version}.crate
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
Summary:        Targeting utilities for compilers and related tools
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arch_zkasm-devel
Summary:        Targeting utilities for compilers and related tools
BuildArch:      noarch
%description -n %{name}+arch_zkasm-devel

This package contains library source intended for building other packages which
use the "arch_zkasm" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Targeting utilities for compilers and related tools
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_support-devel
Summary:        Targeting utilities for compilers and related tools
BuildArch:      noarch
%description -n %{name}+serde_support-devel

This package contains library source intended for building other packages which
use the "serde_support" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Targeting utilities for compilers and related tools
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-target-lexicon0.12-devel -f %{oreon_filedir}/rust-target-lexicon0.12-devel.list

%changelog

%autochangelog

%global source0_hash 1d1435039746e20da4f8d507a72ee1b916f7b4b05af7a91c093d2c6561934ede
%bcond check 0
%global debug_package %{nil}
%global crate vmm-sys-util
Name:           rust-vmm-sys-util0.12
Version:        0.12.1
Release:        1%{?dist}
Summary:        System utility set
License:        BSD-3-Clause
URL:            https://crates.io/crates/vmm-sys-util
Source0:        https://static.crates.io/crates/vmm-sys-util/vmm-sys-util-%{version}.crate
Patch:          vmm-sys-util-fix-metadata.diff
Patch:          vmm-sys-util-omit-ioctl-tests.diff
Patch:          vmm-sys-util-omit-timestamp-test.diff
Patch:          vmm-sys-util-omit-pseudo_rng-test.diff
ExclusiveArch:  x86_64 aarch64 ppc64le riscv64
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
Summary:        System utility set
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        System utility set
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_derive-devel
Summary:        System utility set
BuildArch:      noarch
%description -n %{name}+serde_derive-devel

This package contains library source intended for building other packages which
use the "serde_derive" feature of the "%{crate}" crate.

%package     -n %{name}+with-serde-devel
Summary:        System utility set
BuildArch:      noarch
%description -n %{name}+with-serde-devel

This package contains library source intended for building other packages which
use the "with-serde" feature of the "%{crate}" crate.

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
%files -n rust-vmm-sys-util0.12-devel -f %{oreon_filedir}/rust-vmm-sys-util0.12-devel.list

%changelog

%autochangelog

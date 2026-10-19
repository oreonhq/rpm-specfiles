%global source0_hash 08bba4685ca07397f02bc1119a67f1972aa13fb872d912351ae667663fd8202f
%bcond check 1
%global debug_package %{nil}
%global crate scx_utils
Name:           rust-scx_utils
Version:        0.6.0
Release:        1%{?dist}
Summary:        Utilities for sched_ext schedulers
License:        GPL-2.0-only
URL:            https://crates.io/crates/scx_utils
Source0:        https://static.crates.io/crates/scx_utils/scx_utils-%{version}.crate
Patch:          scx_utils-fix-metadata.diff
Patch:          0001-add-i686-to-ARCH_MAP.patch
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
Summary:        Utilities for sched_ext schedulers
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

%cargo_test -- -- --skip bpf_builder::tests::test_vmlinux_h_ver_sha1
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-scx_utils-devel -f %{oreon_filedir}/rust-scx_utils-devel.list

%changelog

%autochangelog

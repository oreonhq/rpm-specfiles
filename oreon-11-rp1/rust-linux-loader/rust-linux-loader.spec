%global source0_hash de72cb02c55ecffcf75fe78295926f872eb6eb0a58d629c58a8c324dc26380f6
%bcond check 1
%global debug_package %{nil}
%global crate linux-loader
%global supported_arches aarch64 riscv64 x86_64
Name:           rust-linux-loader
Version:        0.13.2
Release:        1%{?dist}
Summary:        Linux kernel image loading crate
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://crates.io/crates/linux-loader
Source0:        https://static.crates.io/crates/linux-loader/linux-loader-%{version}.crate
Patch:          linux-loader-fix-metadata.diff
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
Summary:        Linux kernel image loading crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bzimage-devel
Summary:        Linux kernel image loading crate
BuildArch:      noarch
%description -n %{name}+bzimage-devel

This package contains library source intended for building other packages which
use the "bzimage" feature of the "%{crate}" crate.

%package     -n %{name}+elf-devel
Summary:        Linux kernel image loading crate
BuildArch:      noarch
%description -n %{name}+elf-devel

This package contains library source intended for building other packages which
use the "elf" feature of the "%{crate}" crate.

%package     -n %{name}+pe-devel
Summary:        Linux kernel image loading crate
BuildArch:      noarch
%description -n %{name}+pe-devel

This package contains library source intended for building other packages which
use the "pe" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifarch %{supported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifarch %{supported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-linux-loader-devel -f %{oreon_filedir}/rust-linux-loader-devel.list

%changelog

%autochangelog

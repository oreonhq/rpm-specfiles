%global source0_hash 0bb44936d800fea8f016d7f2311c6a4f97aebd5dc86f09906139ec848cf3a46f
%bcond check 0
%global debug_package %{nil}
%global crate ash
%global upstream_version 0.38.0+1.3.281
Name:           rust-ash
Version:        0.38.0
Release:        1%{?dist}
Summary:        Vulkan bindings for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ash
Source0:        https://crates.io/api/v1/crates/%{crate}/%{upstream_version}/download#/%{crate}-%{upstream_version}.crate
Patch:          ash-fix-metadata-auto.diff
ExcludeArch:    %{ix86}
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
Summary:        Vulkan bindings for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Vulkan bindings for Rust
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+libloading-devel
Summary:        Vulkan bindings for Rust
BuildArch:      noarch
%description -n %{name}+libloading-devel

This package contains library source intended for building other packages which
use the "libloading" feature of the "%{crate}" crate.

%package     -n %{name}+linked-devel
Summary:        Vulkan bindings for Rust
BuildArch:      noarch
%description -n %{name}+linked-devel

This package contains library source intended for building other packages which
use the "linked" feature of the "%{crate}" crate.

%package     -n %{name}+loaded-devel
Summary:        Vulkan bindings for Rust
BuildArch:      noarch
%description -n %{name}+loaded-devel

This package contains library source intended for building other packages which
use the "loaded" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Vulkan bindings for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{upstream_version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- --lib
%cargo_test -- --tests
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-ash-devel -f %{oreon_filedir}/rust-ash-devel.list

%changelog

%autochangelog

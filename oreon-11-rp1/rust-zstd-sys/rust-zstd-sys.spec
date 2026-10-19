%global source0_hash 91e19ebc2adc8f83e43039e79776e3fda8ca919132d68a1fed6a5faca2683748
%bcond check 1
%global debug_package %{nil}
%global crate zstd-sys
%global crate_version 2.0.16+zstd.1.5.7
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-zstd-sys
Version:        2.0.16
Release:        1%{?dist}
Summary:        Low-level bindings for the zstd compression library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/zstd-sys
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          zstd-sys-fix-metadata-auto.diff
Patch:          zstd-sys-fix-metadata.diff
Patch10:        0001-unconditionally-use-bindgen-and-pkg-config-to-link-a.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libzstd)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+bindgen-devel

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+experimental-devel

This package contains library source intended for building other packages which
use the "experimental" feature of the "%{crate}" crate.

%package     -n %{name}+fat-lto-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+fat-lto-devel

This package contains library source intended for building other packages which
use the "fat-lto" feature of the "%{crate}" crate.

%package     -n %{name}+legacy-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+legacy-devel

This package contains library source intended for building other packages which
use the "legacy" feature of the "%{crate}" crate.

%package     -n %{name}+no_asm-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+no_asm-devel

This package contains library source intended for building other packages which
use the "no_asm" feature of the "%{crate}" crate.

%package     -n %{name}+non-cargo-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+non-cargo-devel

This package contains library source intended for building other packages which
use the "non-cargo" feature of the "%{crate}" crate.

%package     -n %{name}+pkg-config-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+pkg-config-devel

This package contains library source intended for building other packages which
use the "pkg-config" feature of the "%{crate}" crate.

%package     -n %{name}+seekable-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+seekable-devel

This package contains library source intended for building other packages which
use the "seekable" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+thin-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+thin-devel

This package contains library source intended for building other packages which
use the "thin" feature of the "%{crate}" crate.

%package     -n %{name}+thin-lto-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+thin-lto-devel

This package contains library source intended for building other packages which
use the "thin-lto" feature of the "%{crate}" crate.

%package     -n %{name}+zdict_builder-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+zdict_builder-devel

This package contains library source intended for building other packages which
use the "zdict_builder" feature of the "%{crate}" crate.

%package     -n %{name}+zstdmt-devel
Summary:        Low-level bindings for the zstd compression library
BuildArch:      noarch
%description -n %{name}+zstdmt-devel

This package contains library source intended for building other packages which
use the "zstdmt" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
rm -vr zstd/
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
%files -n rust-zstd-sys-devel -f %{oreon_filedir}/rust-zstd-sys-devel.list

%changelog

%autochangelog

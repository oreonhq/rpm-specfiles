%global source0_hash 1d2a5585e04f9eea4b2a3d1eca508c4dee9592a89ef6f450c11719da0726f4db
%bcond check 0
%global debug_package %{nil}
%global crate zstd-safe
%global crate_version 5.0.2+zstd.1.5.2
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-zstd-safe5
Version:        5.0.2
Release:        1%{?dist}
Summary:        Safe low-level bindings for the zstd compression library.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/zstd-safe
Source0:        https://static.crates.io/crates/zstd-safe/zstd-safe-%{version}.crate
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
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arrays-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+arrays-devel

This package contains library source intended for building other packages which
use the "arrays" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+bindgen-devel

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+doc-cfg-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+doc-cfg-devel

This package contains library source intended for building other packages which
use the "doc-cfg" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+experimental-devel

This package contains library source intended for building other packages which
use the "experimental" feature of the "%{crate}" crate.

%package     -n %{name}+legacy-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+legacy-devel

This package contains library source intended for building other packages which
use the "legacy" feature of the "%{crate}" crate.

%package     -n %{name}+no_asm-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+no_asm-devel

This package contains library source intended for building other packages which
use the "no_asm" feature of the "%{crate}" crate.

%package     -n %{name}+pkg-config-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+pkg-config-devel

This package contains library source intended for building other packages which
use the "pkg-config" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+thin-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+thin-devel

This package contains library source intended for building other packages which
use the "thin" feature of the "%{crate}" crate.

%package     -n %{name}+zdict_builder-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+zdict_builder-devel

This package contains library source intended for building other packages which
use the "zdict_builder" feature of the "%{crate}" crate.

%package     -n %{name}+zstdmt-devel
Summary:        Safe low-level bindings for the zstd compression library.
BuildArch:      noarch
%description -n %{name}+zstdmt-devel

This package contains library source intended for building other packages which
use the "zstdmt" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-zstd-safe5-devel -f %{oreon_filedir}/rust-zstd-safe5-devel.list

%changelog

%autochangelog

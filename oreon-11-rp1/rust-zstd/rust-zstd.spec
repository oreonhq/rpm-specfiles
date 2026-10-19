%global source0_hash e91ee311a569c327171651566e07972200e76fcfe2242a4fa446149a3881c08a
%bcond check 0
%global debug_package %{nil}
%global crate zstd
Name:           rust-zstd
Version:        0.13.3
Release:        1%{?dist}
Summary:        Binding for the zstd compression library
License:        MIT
URL:            https://crates.io/crates/zstd
Source0:        https://static.crates.io/crates/zstd/zstd-%{version}.crate
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
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arrays-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+arrays-devel

This package contains library source intended for building other packages which
use the "arrays" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+bindgen-devel

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+debug-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+debug-devel

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%package     -n %{name}+doc-cfg-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+doc-cfg-devel

This package contains library source intended for building other packages which
use the "doc-cfg" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+experimental-devel

This package contains library source intended for building other packages which
use the "experimental" feature of the "%{crate}" crate.

%package     -n %{name}+fat-lto-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+fat-lto-devel

This package contains library source intended for building other packages which
use the "fat-lto" feature of the "%{crate}" crate.

%package     -n %{name}+legacy-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+legacy-devel

This package contains library source intended for building other packages which
use the "legacy" feature of the "%{crate}" crate.

%package     -n %{name}+no_asm-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+no_asm-devel

This package contains library source intended for building other packages which
use the "no_asm" feature of the "%{crate}" crate.

%package     -n %{name}+pkg-config-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+pkg-config-devel

This package contains library source intended for building other packages which
use the "pkg-config" feature of the "%{crate}" crate.

%package     -n %{name}+thin-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+thin-devel

This package contains library source intended for building other packages which
use the "thin" feature of the "%{crate}" crate.

%package     -n %{name}+thin-lto-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+thin-lto-devel

This package contains library source intended for building other packages which
use the "thin-lto" feature of the "%{crate}" crate.

%package     -n %{name}+wasm-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+wasm-devel

This package contains library source intended for building other packages which
use the "wasm" feature of the "%{crate}" crate.

%package     -n %{name}+zdict_builder-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+zdict_builder-devel

This package contains library source intended for building other packages which
use the "zdict_builder" feature of the "%{crate}" crate.

%package     -n %{name}+zstdmt-devel
Summary:        Binding for the zstd compression library
BuildArch:      noarch
%description -n %{name}+zstdmt-devel

This package contains library source intended for building other packages which
use the "zstdmt" feature of the "%{crate}" crate.

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
%files -n rust-zstd-devel -f %{oreon_filedir}/rust-zstd-devel.list

%changelog

%autochangelog

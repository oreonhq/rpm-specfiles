%global source0_hash ba0346fc595fa2c8e274903e8a0e3ed5e6a29183af167567f6289fd3b116881b
%bcond check 1
%global debug_package %{nil}
%global crate libbpf-sys
%global crate_version 1.6.2+v1.6.2
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-libbpf-sys
Version:        1.6.2
Release:        1%{?dist}
Summary:        Rust bindings to libbpf from the Linux kernel
License:        BSD-2-Clause
URL:            https://crates.io/crates/libbpf-sys
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          libbpf-sys-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  elfutils-libelf-devel
BuildRequires:  kernel-headers
BuildRequires:  rustc
BuildRequires:  zlib-devel
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       elfutils-libelf-devel
Requires:       kernel-headers
Requires:       zlib-devel
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+bindgen-devel

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-source-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+bindgen-source-devel

This package contains library source intended for building other packages which
use the "bindgen-source" feature of the "%{crate}" crate.

%package     -n %{name}+novendor-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+novendor-devel

This package contains library source intended for building other packages which
use the "novendor" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%package     -n %{name}+static-libbpf-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+static-libbpf-devel

This package contains library source intended for building other packages which
use the "static-libbpf" feature of the "%{crate}" crate.

%package     -n %{name}+static-libelf-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+static-libelf-devel

This package contains library source intended for building other packages which
use the "static-libelf" feature of the "%{crate}" crate.

%package     -n %{name}+static-zlib-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+static-zlib-devel

This package contains library source intended for building other packages which
use the "static-zlib" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+vendored-devel

This package contains library source intended for building other packages which
use the "vendored" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-libbpf-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+vendored-libbpf-devel

This package contains library source intended for building other packages which
use the "vendored-libbpf" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-libelf-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+vendored-libelf-devel

This package contains library source intended for building other packages which
use the "vendored-libelf" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-zlib-devel
Summary:        Rust bindings to libbpf from the Linux kernel
BuildArch:      noarch
%description -n %{name}+vendored-zlib-devel

This package contains library source intended for building other packages which
use the "vendored-zlib" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
rm -rf elfutils zlib
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
%files -n rust-libbpf-sys-devel -f %{oreon_filedir}/rust-libbpf-sys-devel.list

%changelog

%autochangelog

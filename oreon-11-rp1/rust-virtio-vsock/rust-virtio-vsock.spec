%global source0_hash e49ff39d455ce92f01a910cb11b01e54b61c6f3b5d308a144c86044b39955b79
%bcond check 1
%global debug_package %{nil}
%global crate virtio-vsock
Name:           rust-virtio-vsock
Version:        0.10.0
Release:        1%{?dist}
Summary:        Virtio vsock device implementation
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://crates.io/crates/virtio-vsock
Source0:        https://static.crates.io/crates/virtio-vsock/virtio-vsock-%{version}.crate
ExclusiveArch:  aarch64 ppc64le riscv64 x86_64
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
Summary:        Virtio vsock device implementation
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
%files -n rust-virtio-vsock-devel -f %{oreon_filedir}/rust-virtio-vsock-devel.list

%changelog

%autochangelog

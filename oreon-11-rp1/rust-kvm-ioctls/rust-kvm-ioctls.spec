%global source0_hash 0e00243d27a20feb05cf001ae52ddc79831ac70c020f215ba1153ff9270b650a
%bcond check 0
%global debug_package %{nil}
%global crate kvm-ioctls
%global supported_arches aarch64 riscv64 x86_64
Name:           rust-kvm-ioctls
Version:        0.23.0
Release:        1%{?dist}
Summary:        Safe wrappers over KVM ioctls
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/kvm-ioctls
Source0:        https://static.crates.io/crates/kvm-ioctls/kvm-ioctls-%{version}.crate
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
Summary:        Safe wrappers over KVM ioctls
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-kvm-ioctls-devel -f %{oreon_filedir}/rust-kvm-ioctls-devel.list

%changelog

%autochangelog

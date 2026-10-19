%global source0_hash d1ee41cf6fb1bb6030dfb59ffb7bc01ab26aade44142084c87f0fc7a1658fe71
%bcond check 1
%global debug_package %{nil}
%global crate libdeflater
Name:           rust-libdeflater
Version:        1.25.2
Release:        1%{?dist}
Summary:        Bindings to libdeflate for DEFLATE
License:        Apache-2.0
URL:            https://crates.io/crates/libdeflater
Source0:        https://static.crates.io/crates/libdeflater/libdeflater-%{version}.crate
Patch:          libdeflater-fix-metadata.diff
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
Summary:        Bindings to libdeflate for DEFLATE
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dynamic-devel
Summary:        Bindings to libdeflate for DEFLATE
BuildArch:      noarch
%description -n %{name}+dynamic-devel

This package contains library source intended for building other packages which
use the "dynamic" feature of the "%{crate}" crate.

%package     -n %{name}+freestanding-devel
Summary:        Bindings to libdeflate for DEFLATE
BuildArch:      noarch
%description -n %{name}+freestanding-devel

This package contains library source intended for building other packages which
use the "freestanding" feature of the "%{crate}" crate.

%package     -n %{name}+use_rust_alloc-devel
Summary:        Bindings to libdeflate for DEFLATE
BuildArch:      noarch
%description -n %{name}+use_rust_alloc-devel

This package contains library source intended for building other packages which
use the "use_rust_alloc" feature of the "%{crate}" crate.

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
%files -n rust-libdeflater-devel -f %{oreon_filedir}/rust-libdeflater-devel.list

%changelog

%autochangelog

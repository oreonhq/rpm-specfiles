%global source0_hash 71fe3824f5629716b1589be05dacd749f6aa084c87e00e016714a8cdfccc997c
%bcond check 0
%global debug_package %{nil}
%global crate rend
Name:           rust-rend
Version:        0.4.2
Release:        1%{?dist}
Summary:        Endian-aware primitives for Rust
License:        MIT
URL:            https://crates.io/crates/rend
Source0:        https://static.crates.io/crates/rend/rend-%{version}.crate
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
Summary:        Endian-aware primitives for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytecheck-devel
Summary:        Endian-aware primitives for Rust
BuildArch:      noarch
%description -n %{name}+bytecheck-devel

This package contains library source intended for building other packages which
use the "bytecheck" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Endian-aware primitives for Rust
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Endian-aware primitives for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+validation-devel
Summary:        Endian-aware primitives for Rust
BuildArch:      noarch
%description -n %{name}+validation-devel

This package contains library source intended for building other packages which
use the "validation" feature of the "%{crate}" crate.

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
%files -n rust-rend-devel -f %{oreon_filedir}/rust-rend-devel.list

%changelog

%autochangelog

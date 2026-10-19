%global source101_hash ade7464c3862231dee5b9f464b7c9dbd8bec689524aa17f2c21c69760fe594fc
%global source100_hash c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4
%global source0_hash 2a2d6934d2508f94fd4cbda6c2a326f111f60ce59fd9136df6d478564397dd40
%bcond check 0
%global debug_package %{nil}
%global crate openxr
Name:           rust-openxr
Version:        0.19.0
Release:        1%{?dist}
Summary:        High-level, mostly-safe OpenXR bindings
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/openxr
Source0:        https://static.crates.io/crates/openxr/openxr-%{version}.crate
Source100:      https://raw.githubusercontent.com/Ralith/openxrs/refs/heads/master/LICENSE-APACHE
Source101:      https://raw.githubusercontent.com/Ralith/openxrs/refs/heads/master/LICENSE-MIT
Patch:          openxr-fix-metadata-auto.diff
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
Summary:        High-level, mostly-safe OpenXR bindings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+libloading-devel
Summary:        High-level, mostly-safe OpenXR bindings
BuildArch:      noarch
%description -n %{name}+libloading-devel

This package contains library source intended for building other packages which
use the "libloading" feature of the "%{crate}" crate.

%package     -n %{name}+linked-devel
Summary:        High-level, mostly-safe OpenXR bindings
BuildArch:      noarch
%description -n %{name}+linked-devel

This package contains library source intended for building other packages which
use the "linked" feature of the "%{crate}" crate.

%package     -n %{name}+loaded-devel
Summary:        High-level, mostly-safe OpenXR bindings
BuildArch:      noarch
%description -n %{name}+loaded-devel

This package contains library source intended for building other packages which
use the "loaded" feature of the "%{crate}" crate.

%package     -n %{name}+mint-devel
Summary:        High-level, mostly-safe OpenXR bindings
BuildArch:      noarch
%description -n %{name}+mint-devel

This package contains library source intended for building other packages which
use the "mint" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        High-level, mostly-safe OpenXR bindings
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE100} %{SOURCE101} .
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
%files -n rust-openxr-devel -f %{oreon_filedir}/rust-openxr-devel.list

%changelog

%autochangelog

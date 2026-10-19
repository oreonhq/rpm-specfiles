%global source0_hash 03b69722f9386e24ae14655f8faddff28cb6a9a5511d7ffdde3a4499b51cca07
%bcond check 1
%global debug_package %{nil}
%global crate libheif-sys
%global crate_version 5.3.1+1.23.1+1.21.2
%global crate_instdir %{cargo_registry}/%{crate}-%{crate_version}
Name:           rust-libheif-sys
Version:        5.3.1+1.23.1
Release:        1%{?dist}
Summary:        Libheif bindings
License:        MIT
URL:            https://crates.io/crates/libheif-sys
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          libheif-sys-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(libheif)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libheif) >= 1.21
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Libheif bindings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+latest-devel
Summary:        Libheif bindings
BuildArch:      noarch
%description -n %{name}+latest-devel

This package contains library source intended for building other packages which
use the "latest" feature of the "%{crate}" crate.

%package     -n %{name}+use-bindgen-devel
Summary:        Libheif bindings
BuildArch:      noarch
%description -n %{name}+use-bindgen-devel

This package contains library source intended for building other packages which
use the "use-bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+v1_17-devel
Summary:        Libheif bindings
BuildArch:      noarch
%description -n %{name}+v1_17-devel

This package contains library source intended for building other packages which
use the "v1_17" feature of the "%{crate}" crate.

%package     -n %{name}+v1_18-devel
Summary:        Libheif bindings
BuildArch:      noarch
%description -n %{name}+v1_18-devel

This package contains library source intended for building other packages which
use the "v1_18" feature of the "%{crate}" crate.

%package     -n %{name}+v1_19-devel
Summary:        Libheif bindings
BuildArch:      noarch
%description -n %{name}+v1_19-devel

This package contains library source intended for building other packages which
use the "v1_19" feature of the "%{crate}" crate.

%package     -n %{name}+v1_20-devel
Summary:        Libheif bindings
BuildArch:      noarch
%description -n %{name}+v1_20-devel

This package contains library source intended for building other packages which
use the "v1_20" feature of the "%{crate}" crate.

%package     -n %{name}+v1_21-devel
Summary:        Libheif bindings
BuildArch:      noarch
%description -n %{name}+v1_21-devel

This package contains library source intended for building other packages which
use the "v1_21" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
rm -rf vendor/
%oreon_vendor_cargo
%build

%cargo_build -f v1_21
%install
%cargo_install -f v1_21
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f v1_21 -- -- --skip create_heic_context
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-libheif-sys-devel -f %{oreon_filedir}/rust-libheif-sys-devel.list

%changelog

%autochangelog

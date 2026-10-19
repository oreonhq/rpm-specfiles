%global source0_hash c66d4b9ed69c4009f6321f762d6e61ad8a2389cd431b97cb1e146812e9e6c732
%bcond check 1
%global debug_package %{nil}
%global crate winit
Name:           rust-winit
Version:        0.30.12
Release:        1%{?dist}
Summary:        Cross-platform window creation library
License:        Apache-2.0
URL:            https://crates.io/crates/winit
Source0:        https://static.crates.io/crates/winit/winit-%{version}.crate
Patch:          winit-fix-metadata-auto.diff
Patch:          winit-fix-metadata.diff
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
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ahash-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+ahash-devel

This package contains library source intended for building other packages which
use the "ahash" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+memmap2-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+memmap2-devel

This package contains library source intended for building other packages which
use the "memmap2" feature of the "%{crate}" crate.

%package     -n %{name}+mint-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+mint-devel

This package contains library source intended for building other packages which
use the "mint" feature of the "%{crate}" crate.

%package     -n %{name}+percent-encoding-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+percent-encoding-devel

This package contains library source intended for building other packages which
use the "percent-encoding" feature of the "%{crate}" crate.

%package     -n %{name}+rwh_05-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+rwh_05-devel

This package contains library source intended for building other packages which
use the "rwh_05" feature of the "%{crate}" crate.

%package     -n %{name}+rwh_06-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+rwh_06-devel

This package contains library source intended for building other packages which
use the "rwh_06" feature of the "%{crate}" crate.

%package     -n %{name}+sctk-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+sctk-devel

This package contains library source intended for building other packages which
use the "sctk" feature of the "%{crate}" crate.

%package     -n %{name}+sctk-adwaita-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+sctk-adwaita-devel

This package contains library source intended for building other packages which
use the "sctk-adwaita" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+wayland-devel

This package contains library source intended for building other packages which
use the "wayland" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-backend-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+wayland-backend-devel

This package contains library source intended for building other packages which
use the "wayland-backend" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-client-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+wayland-client-devel

This package contains library source intended for building other packages which
use the "wayland-client" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-csd-adwaita-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+wayland-csd-adwaita-devel

This package contains library source intended for building other packages which
use the "wayland-csd-adwaita" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-csd-adwaita-crossfont-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+wayland-csd-adwaita-crossfont-devel

This package contains library source intended for building other packages which
use the "wayland-csd-adwaita-crossfont" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-csd-adwaita-notitle-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+wayland-csd-adwaita-notitle-devel

This package contains library source intended for building other packages which
use the "wayland-csd-adwaita-notitle" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-dlopen-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+wayland-dlopen-devel

This package contains library source intended for building other packages which
use the "wayland-dlopen" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-protocols-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+wayland-protocols-devel

This package contains library source intended for building other packages which
use the "wayland-protocols" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-protocols-plasma-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+wayland-protocols-plasma-devel

This package contains library source intended for building other packages which
use the "wayland-protocols-plasma" feature of the "%{crate}" crate.

%package     -n %{name}+x11-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+x11-devel

This package contains library source intended for building other packages which
use the "x11" feature of the "%{crate}" crate.

%package     -n %{name}+x11-dl-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+x11-dl-devel

This package contains library source intended for building other packages which
use the "x11-dl" feature of the "%{crate}" crate.

%package     -n %{name}+x11rb-devel
Summary:        Cross-platform window creation library
BuildArch:      noarch
%description -n %{name}+x11rb-devel

This package contains library source intended for building other packages which
use the "x11rb" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -rf examples/
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
%files -n rust-winit-devel -f %{oreon_filedir}/rust-winit-devel.list

%changelog

%autochangelog

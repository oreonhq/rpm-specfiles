%global source0_hash 9a83ca3d2030846f01be738b8b867ecb4b95269497bcfa459b8fc1ce897ad9f4
%bcond check 1
%global debug_package %{nil}
%global crate gstreamer-gl-wayland
Name:           rust-gstreamer-gl-wayland
Version:        0.25.0
Release:        1%{?dist}
Summary:        Rust bindings for GStreamer GL library (Wayland support)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gstreamer-gl-wayland
Source0:        https://static.crates.io/crates/gstreamer-gl-wayland/gstreamer-gl-wayland-%{version}.crate
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
Summary:        Rust bindings for GStreamer GL library (Wayland support)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v1_16-devel
Summary:        Rust bindings for GStreamer GL library (Wayland support)
BuildArch:      noarch
%description -n %{name}+v1_16-devel

This package contains library source intended for building other packages which
use the "v1_16" feature of the "%{crate}" crate.

%package     -n %{name}+v1_18-devel
Summary:        Rust bindings for GStreamer GL library (Wayland support)
BuildArch:      noarch
%description -n %{name}+v1_18-devel

This package contains library source intended for building other packages which
use the "v1_18" feature of the "%{crate}" crate.

%package     -n %{name}+v1_20-devel
Summary:        Rust bindings for GStreamer GL library (Wayland support)
BuildArch:      noarch
%description -n %{name}+v1_20-devel

This package contains library source intended for building other packages which
use the "v1_20" feature of the "%{crate}" crate.

%package     -n %{name}+v1_22-devel
Summary:        Rust bindings for GStreamer GL library (Wayland support)
BuildArch:      noarch
%description -n %{name}+v1_22-devel

This package contains library source intended for building other packages which
use the "v1_22" feature of the "%{crate}" crate.

%package     -n %{name}+v1_24-devel
Summary:        Rust bindings for GStreamer GL library (Wayland support)
BuildArch:      noarch
%description -n %{name}+v1_24-devel

This package contains library source intended for building other packages which
use the "v1_24" feature of the "%{crate}" crate.

%package     -n %{name}+v1_26-devel
Summary:        Rust bindings for GStreamer GL library (Wayland support)
BuildArch:      noarch
%description -n %{name}+v1_26-devel

This package contains library source intended for building other packages which
use the "v1_26" feature of the "%{crate}" crate.

%package     -n %{name}+v1_28-devel
Summary:        Rust bindings for GStreamer GL library (Wayland support)
BuildArch:      noarch
%description -n %{name}+v1_28-devel

This package contains library source intended for building other packages which
use the "v1_28" feature of the "%{crate}" crate.

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
%files -n rust-gstreamer-gl-wayland-devel -f %{oreon_filedir}/rust-gstreamer-gl-wayland-devel.list

%changelog

%autochangelog

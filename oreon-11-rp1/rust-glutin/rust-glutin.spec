%global source0_hash 12124de845cacfebedff80e877bb37b5b75c34c5a4c89e47e1cdd67fb6041325
%bcond check 1
%global debug_package %{nil}
%global crate glutin
Name:           rust-glutin
Version:        0.32.3
Release:        1%{?dist}
Summary:        Cross-platform OpenGL context provider
License:        Apache-2.0
URL:            https://crates.io/crates/glutin
Source0:        https://static.crates.io/crates/glutin/glutin-%{version}.crate
Patch:          glutin-fix-metadata-auto.diff
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
Summary:        Cross-platform OpenGL context provider
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+egl-devel
Summary:        Cross-platform OpenGL context provider
BuildArch:      noarch
%description -n %{name}+egl-devel

This package contains library source intended for building other packages which
use the "egl" feature of the "%{crate}" crate.

%package     -n %{name}+glutin_egl_sys-devel
Summary:        Cross-platform OpenGL context provider
BuildArch:      noarch
%description -n %{name}+glutin_egl_sys-devel

This package contains library source intended for building other packages which
use the "glutin_egl_sys" feature of the "%{crate}" crate.

%package     -n %{name}+glutin_glx_sys-devel
Summary:        Cross-platform OpenGL context provider
BuildArch:      noarch
%description -n %{name}+glutin_glx_sys-devel

This package contains library source intended for building other packages which
use the "glutin_glx_sys" feature of the "%{crate}" crate.

%package     -n %{name}+glx-devel
Summary:        Cross-platform OpenGL context provider
BuildArch:      noarch
%description -n %{name}+glx-devel

This package contains library source intended for building other packages which
use the "glx" feature of the "%{crate}" crate.

%package     -n %{name}+libloading-devel
Summary:        Cross-platform OpenGL context provider
BuildArch:      noarch
%description -n %{name}+libloading-devel

This package contains library source intended for building other packages which
use the "libloading" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-devel
Summary:        Cross-platform OpenGL context provider
BuildArch:      noarch
%description -n %{name}+wayland-devel

This package contains library source intended for building other packages which
use the "wayland" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-sys-devel
Summary:        Cross-platform OpenGL context provider
BuildArch:      noarch
%description -n %{name}+wayland-sys-devel

This package contains library source intended for building other packages which
use the "wayland-sys" feature of the "%{crate}" crate.

%package     -n %{name}+wgl-devel
Summary:        Cross-platform OpenGL context provider
BuildArch:      noarch
%description -n %{name}+wgl-devel

This package contains library source intended for building other packages which
use the "wgl" feature of the "%{crate}" crate.

%package     -n %{name}+x11-devel
Summary:        Cross-platform OpenGL context provider
BuildArch:      noarch
%description -n %{name}+x11-devel

This package contains library source intended for building other packages which
use the "x11" feature of the "%{crate}" crate.

%package     -n %{name}+x11-dl-devel
Summary:        Cross-platform OpenGL context provider
BuildArch:      noarch
%description -n %{name}+x11-dl-devel

This package contains library source intended for building other packages which
use the "x11-dl" feature of the "%{crate}" crate.

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
%files -n rust-glutin-devel -f %{oreon_filedir}/rust-glutin-devel.list

%changelog

%autochangelog

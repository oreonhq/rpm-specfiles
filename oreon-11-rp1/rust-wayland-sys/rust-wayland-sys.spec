%global source0_hash d8eab23fefc9e41f8e841df4a9c707e8a8c4ed26e944ef69297184de2785e3be
%bcond check 1
%global debug_package %{nil}
%global crate wayland-sys
Name:           rust-wayland-sys
Version:        0.31.11
Release:        1%{?dist}
Summary:        FFI bindings to the various libwayland-*.so libraries
License:        MIT
URL:            https://crates.io/crates/wayland-sys
Source0:        https://static.crates.io/crates/wayland-sys/wayland-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       wayland-devel
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to the various libwayland-*.so libraries
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+client-devel
Summary:        FFI bindings to the various libwayland-*.so libraries
BuildArch:      noarch
Requires:       pkgconfig(wayland-client)
%description -n %{name}+client-devel

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%package     -n %{name}+cursor-devel
Summary:        FFI bindings to the various libwayland-*.so libraries
BuildArch:      noarch
Requires:       pkgconfig(wayland-cursor)
%description -n %{name}+cursor-devel

This package contains library source intended for building other packages which
use the "cursor" feature of the "%{crate}" crate.

%package     -n %{name}+dlopen-devel
Summary:        FFI bindings to the various libwayland-*.so libraries
BuildArch:      noarch
%description -n %{name}+dlopen-devel

This package contains library source intended for building other packages which
use the "dlopen" feature of the "%{crate}" crate.

%package     -n %{name}+egl-devel
Summary:        FFI bindings to the various libwayland-*.so libraries
BuildArch:      noarch
Requires:       pkgconfig(wayland-egl)
%description -n %{name}+egl-devel

This package contains library source intended for building other packages which
use the "egl" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        FFI bindings to the various libwayland-*.so libraries
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+memoffset-devel
Summary:        FFI bindings to the various libwayland-*.so libraries
BuildArch:      noarch
%description -n %{name}+memoffset-devel

This package contains library source intended for building other packages which
use the "memoffset" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        FFI bindings to the various libwayland-*.so libraries
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        FFI bindings to the various libwayland-*.so libraries
BuildArch:      noarch
Requires:       pkgconfig(wayland-server)
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

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
%files -n rust-wayland-sys-devel -f %{oreon_filedir}/rust-wayland-sys-devel.list

%changelog

%autochangelog

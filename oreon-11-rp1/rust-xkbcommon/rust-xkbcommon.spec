%global source0_hash 8d66ca9352cbd4eecbbc40871d8a11b4ac8107cfc528a6e14d7c19c69d0e1ac9
%bcond check 1
%global debug_package %{nil}
%global crate xkbcommon
Name:           rust-xkbcommon
Version:        0.8.0
Release:        1%{?dist}
Summary:        Rust bindings and wrappers for libxkbcommon
License:        MIT
URL:            https://crates.io/crates/xkbcommon
Source0:        https://static.crates.io/crates/xkbcommon/xkbcommon-%{version}.crate
Patch:          xkbcommon-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  libxkbcommon-devel
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       libxkbcommon-devel
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Rust bindings and wrappers for libxkbcommon
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+as-raw-xcb-connection-devel
Summary:        Rust bindings and wrappers for libxkbcommon
BuildArch:      noarch
%description -n %{name}+as-raw-xcb-connection-devel

This package contains library source intended for building other packages which
use the "as-raw-xcb-connection" feature of the "%{crate}" crate.

%package     -n %{name}+memmap2-devel
Summary:        Rust bindings and wrappers for libxkbcommon
BuildArch:      noarch
%description -n %{name}+memmap2-devel

This package contains library source intended for building other packages which
use the "memmap2" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-devel
Summary:        Rust bindings and wrappers for libxkbcommon
BuildArch:      noarch
%description -n %{name}+wayland-devel

This package contains library source intended for building other packages which
use the "wayland" feature of the "%{crate}" crate.

%package     -n %{name}+x11-devel
Summary:        Rust bindings and wrappers for libxkbcommon
BuildArch:      noarch
%description -n %{name}+x11-devel

This package contains library source intended for building other packages which
use the "x11" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -f examples/quick-evdev.rs
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
%files -n rust-xkbcommon-devel -f %{oreon_filedir}/rust-xkbcommon-devel.list

%changelog

%autochangelog

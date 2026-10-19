%global source0_hash 3457dea1f0eb631b4034d61d4d8c32074caa6cd1ab2d59f2327bd8461e2c0016
%bcond check 1
%global debug_package %{nil}
%global crate smithay-client-toolkit
Name:           rust-smithay-client-toolkit
Version:        0.19.2
Release:        1%{?dist}
Summary:        Toolkit for making client wayland applications
License:        MIT
URL:            https://crates.io/crates/smithay-client-toolkit
Source0:        https://static.crates.io/crates/smithay-client-toolkit/smithay-client-toolkit-%{version}.crate
Patch:          smithay-client-toolkit-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
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
Summary:        Toolkit for making client wayland applications
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Toolkit for making client wayland applications
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+calloop-devel
Summary:        Toolkit for making client wayland applications
BuildArch:      noarch
%description -n %{name}+calloop-devel

This package contains library source intended for building other packages which
use the "calloop" feature of the "%{crate}" crate.

%package     -n %{name}+calloop-wayland-source-devel
Summary:        Toolkit for making client wayland applications
BuildArch:      noarch
%description -n %{name}+calloop-wayland-source-devel

This package contains library source intended for building other packages which
use the "calloop-wayland-source" feature of the "%{crate}" crate.

%package     -n %{name}+pkg-config-devel
Summary:        Toolkit for making client wayland applications
BuildArch:      noarch
%description -n %{name}+pkg-config-devel

This package contains library source intended for building other packages which
use the "pkg-config" feature of the "%{crate}" crate.

%package     -n %{name}+xkbcommon-devel
Summary:        Toolkit for making client wayland applications
BuildArch:      noarch
%description -n %{name}+xkbcommon-devel

This package contains library source intended for building other packages which
use the "xkbcommon" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -f examples/{relative_pointer.rs,wgpu.rs}
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
%files -n rust-smithay-client-toolkit-devel -f %{oreon_filedir}/rust-smithay-client-toolkit-devel.list

%changelog

%autochangelog

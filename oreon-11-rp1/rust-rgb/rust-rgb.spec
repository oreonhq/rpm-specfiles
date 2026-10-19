%global source0_hash 47b34b781b31e5d73e9fbc8689c70551fd1ade9a19e3e28cfec8580a79290cc4
%bcond check 0
%global debug_package %{nil}
%global crate rgb
Name:           rust-rgb
Version:        0.8.53
Release:        1%{?dist}
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenienc...
License:        MIT
URL:            https://crates.io/crates/rgb
Source0:        https://static.crates.io/crates/rgb/rgb-%{version}.crate
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
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenienc...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+argb-devel
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenienc...
BuildArch:      noarch
%description -n %{name}+argb-devel

This package contains library source intended for building other packages which
use the "argb" feature of the "%{crate}" crate.

%package     -n %{name}+as-bytes-devel
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenienc...
BuildArch:      noarch
%description -n %{name}+as-bytes-devel

This package contains library source intended for building other packages which
use the "as-bytes" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenienc...
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+checked_fns-devel
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenienc...
BuildArch:      noarch
%description -n %{name}+checked_fns-devel

This package contains library source intended for building other packages which
use the "checked_fns" feature of the "%{crate}" crate.

%package     -n %{name}+defmt-03-devel
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenienc...
BuildArch:      noarch
%description -n %{name}+defmt-03-devel

This package contains library source intended for building other packages which
use the "defmt-03" feature of the "%{crate}" crate.

%package     -n %{name}+grb-devel
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenienc...
BuildArch:      noarch
%description -n %{name}+grb-devel

This package contains library source intended for building other packages which
use the "grb" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenienc...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-experimental-devel
Summary:        `struct RGB/RGBA/etc.` for sharing pixels between crates + convenienc...
BuildArch:      noarch
%description -n %{name}+unstable-experimental-devel

This package contains library source intended for building other packages which
use the "unstable-experimental" feature of the "%{crate}" crate.

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
%files -n rust-rgb-devel -f %{oreon_filedir}/rust-rgb-devel.list

%changelog

%autochangelog

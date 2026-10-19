%global source0_hash 533fa8d28fc830eafccbcfcfddb390563ea5d3a351af2c3aab99e197e5f5b1ba
%bcond check 1
%global debug_package %{nil}
%global crate gstreamer-sys
Name:           rust-gstreamer-sys
Version:        0.25.2
Release:        1%{?dist}
Summary:        FFI bindings to libgstreamer-1.0
License:        MIT
URL:            https://crates.io/crates/gstreamer-sys
Source0:        https://static.crates.io/crates/gstreamer-sys/gstreamer-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gstreamer-1.0) >= 1.14
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to libgstreamer-1.0
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v1_16-devel
Summary:        FFI bindings to libgstreamer-1.0
BuildArch:      noarch
Requires:       pkgconfig(gstreamer-1.0) >= 1.16
%description -n %{name}+v1_16-devel

This package contains library source intended for building other packages which
use the "v1_16" feature of the "%{crate}" crate.

%package     -n %{name}+v1_18-devel
Summary:        FFI bindings to libgstreamer-1.0
BuildArch:      noarch
Requires:       pkgconfig(gstreamer-1.0) >= 1.18
%description -n %{name}+v1_18-devel

This package contains library source intended for building other packages which
use the "v1_18" feature of the "%{crate}" crate.

%package     -n %{name}+v1_18_3-devel
Summary:        FFI bindings to libgstreamer-1.0
BuildArch:      noarch
Requires:       pkgconfig(gstreamer-1.0) >= 1.18.3
%description -n %{name}+v1_18_3-devel

This package contains library source intended for building other packages which
use the "v1_18_3" feature of the "%{crate}" crate.

%package     -n %{name}+v1_20-devel
Summary:        FFI bindings to libgstreamer-1.0
BuildArch:      noarch
Requires:       pkgconfig(gstreamer-1.0) >= 1.20
%description -n %{name}+v1_20-devel

This package contains library source intended for building other packages which
use the "v1_20" feature of the "%{crate}" crate.

%package     -n %{name}+v1_20_4-devel
Summary:        FFI bindings to libgstreamer-1.0
BuildArch:      noarch
Requires:       pkgconfig(gstreamer-1.0) >= 1.20.4
%description -n %{name}+v1_20_4-devel

This package contains library source intended for building other packages which
use the "v1_20_4" feature of the "%{crate}" crate.

%package     -n %{name}+v1_22-devel
Summary:        FFI bindings to libgstreamer-1.0
BuildArch:      noarch
Requires:       pkgconfig(gstreamer-1.0) >= 1.22
%description -n %{name}+v1_22-devel

This package contains library source intended for building other packages which
use the "v1_22" feature of the "%{crate}" crate.

%package     -n %{name}+v1_24-devel
Summary:        FFI bindings to libgstreamer-1.0
BuildArch:      noarch
Requires:       pkgconfig(gstreamer-1.0) >= 1.24
%description -n %{name}+v1_24-devel

This package contains library source intended for building other packages which
use the "v1_24" feature of the "%{crate}" crate.

%package     -n %{name}+v1_26-devel
Summary:        FFI bindings to libgstreamer-1.0
BuildArch:      noarch
Requires:       pkgconfig(gstreamer-1.0) >= 1.26
%description -n %{name}+v1_26-devel

This package contains library source intended for building other packages which
use the "v1_26" feature of the "%{crate}" crate.

%package     -n %{name}+v1_28-devel
Summary:        FFI bindings to libgstreamer-1.0
BuildArch:      noarch
Requires:       pkgconfig(gstreamer-1.0) >= 1.28
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
%files -n rust-gstreamer-sys-devel -f %{oreon_filedir}/rust-gstreamer-sys-devel.list

%changelog

%autochangelog

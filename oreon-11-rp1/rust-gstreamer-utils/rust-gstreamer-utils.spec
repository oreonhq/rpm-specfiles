%global source0_hash 7e81a18c2f314d567e11e4187ca60c6feb116fe85f23553e92a6d8f38c205998
%bcond check 1
%global debug_package %{nil}
%global crate gstreamer-utils
Name:           rust-gstreamer-utils
Version:        0.25.0
Release:        1%{?dist}
Summary:        GStreamer Rust APIs for linking producers and consumers
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gstreamer-utils
Source0:        https://static.crates.io/crates/gstreamer-utils/gstreamer-utils-%{version}.crate
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
Summary:        GStreamer Rust APIs for linking producers and consumers
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v1_22-devel
Summary:        GStreamer Rust APIs for linking producers and consumers
BuildArch:      noarch
%description -n %{name}+v1_22-devel

This package contains library source intended for building other packages which
use the "v1_22" feature of the "%{crate}" crate.

%package     -n %{name}+v1_24-devel
Summary:        GStreamer Rust APIs for linking producers and consumers
BuildArch:      noarch
%description -n %{name}+v1_24-devel

This package contains library source intended for building other packages which
use the "v1_24" feature of the "%{crate}" crate.

%package     -n %{name}+v1_26-devel
Summary:        GStreamer Rust APIs for linking producers and consumers
BuildArch:      noarch
%description -n %{name}+v1_26-devel

This package contains library source intended for building other packages which
use the "v1_26" feature of the "%{crate}" crate.

%package     -n %{name}+v1_28-devel
Summary:        GStreamer Rust APIs for linking producers and consumers
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
%files -n rust-gstreamer-utils-devel -f %{oreon_filedir}/rust-gstreamer-utils-devel.list

%changelog

%autochangelog

%global source0_hash 138afa2bdcee5df89b5f9db6abe89a3eff71dc8813e1eae00754a9e3cbd16bee
%bcond check 1
%global crate gst-plugin-hsv
Name:           rust-gst-plugin-hsv
Version:        0.15.0
Release:        1%{?dist}
Summary:        GStreamer plugin with HSV manipulation elements
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gst-plugin-hsv
Source0:        https://static.crates.io/crates/gst-plugin-hsv/gst-plugin-hsv-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n gstreamer1-plugin-hsv
Summary:        GStreamer plugin with HSV manipulation elements
License:        (Apache-2.0 OR MIT) AND MIT AND (Unlicense OR MIT)
Provides:       %{crate} = %{version}-%{release}
%description -n gstreamer1-plugin-hsv

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        GStreamer plugin with HSV manipulation elements
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        GStreamer plugin with HSV manipulation elements
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+doc-devel
Summary:        GStreamer plugin with HSV manipulation elements
BuildArch:      noarch
%description -n %{name}+doc-devel

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        GStreamer plugin with HSV manipulation elements
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%cargo_cbuild
%install
%cargo_install
%cargo_cinstall
rm -v %{buildroot}/%{_libdir}/gstreamer-1.0/libgsthsv.a
rm -v %{buildroot}/%{_libdir}/pkgconfig/gsthsv.pc
%oreon_autofiles gstreamer1-plugin-hsv usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n gstreamer1-plugin-hsv -f %{oreon_filedir}/gstreamer1-plugin-hsv.list
%files -n rust-gst-plugin-hsv-devel -f %{oreon_filedir}/rust-gst-plugin-hsv-devel.list

%changelog

%autochangelog

%global source0_hash 1af679769a9e89f97c224ea4c5b3663b40dfae2d265c4d2953c8b9413aefa273
%bcond check 1
%global crate gst-plugin-dav1d
Name:           rust-gst-plugin-dav1d
Version:        0.15.0
Release:        1%{?dist}
Summary:        GStreamer dav1d AV1 decoder Plugin
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gst-plugin-dav1d
Source0:        https://static.crates.io/crates/gst-plugin-dav1d/gst-plugin-dav1d-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n gstreamer1-plugin-dav1d
Summary:        GStreamer dav1d AV1 decoder Plugin
License:        MIT AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
Provides:       %{crate} = %{version}-%{release}
%description -n gstreamer1-plugin-dav1d

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        GStreamer dav1d AV1 decoder Plugin
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        GStreamer dav1d AV1 decoder Plugin
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+doc-devel
Summary:        GStreamer dav1d AV1 decoder Plugin
BuildArch:      noarch
%description -n %{name}+doc-devel

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        GStreamer dav1d AV1 decoder Plugin
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
rm -v %{buildroot}/%{_libdir}/gstreamer-1.0/libgstdav1d.a
rm -v %{buildroot}/%{_libdir}/pkgconfig/gstdav1d.pc
%oreon_autofiles gstreamer1-plugin-dav1d usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n gstreamer1-plugin-dav1d -f %{oreon_filedir}/gstreamer1-plugin-dav1d.list
%files -n rust-gst-plugin-dav1d-devel -f %{oreon_filedir}/rust-gst-plugin-dav1d-devel.list

%changelog

%autochangelog

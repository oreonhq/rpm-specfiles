%global source0_hash 0b86f9391e55b43c6c03d18d626d725c9c72d9d88aea4b1e0751ea23978e4bc2
%bcond check 1
%global crate gst-plugin-gif
Name:           rust-gst-plugin-gif
Version:        0.15.0
Release:        1%{?dist}
Summary:        GStreamer GIF plugin
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gst-plugin-gif
Source0:        https://static.crates.io/crates/gst-plugin-gif/gst-plugin-gif-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n gstreamer1-plugin-gif
Summary:        GStreamer GIF plugin
License:        MIT AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
Provides:       %{crate} = %{version}-%{release}
%description -n gstreamer1-plugin-gif

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        GStreamer GIF plugin
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        GStreamer GIF plugin
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+doc-devel
Summary:        GStreamer GIF plugin
BuildArch:      noarch
%description -n %{name}+doc-devel

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        GStreamer GIF plugin
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
rm -v %{buildroot}/%{_libdir}/gstreamer-1.0/libgstgif.a
rm -v %{buildroot}/%{_libdir}/pkgconfig/gstgif.pc
%oreon_autofiles gstreamer1-plugin-gif usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n gstreamer1-plugin-gif -f %{oreon_filedir}/gstreamer1-plugin-gif.list
%files -n rust-gst-plugin-gif-devel -f %{oreon_filedir}/rust-gst-plugin-gif-devel.list

%changelog

%autochangelog

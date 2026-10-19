%global source0_hash 251c867f762f136393a8f5b838b0a953ef161e702ef6137eb1fa3906521a46de
%bcond check 1
%global crate gst-plugin-json
Name:           rust-gst-plugin-json
Version:        0.15.0
Release:        1%{?dist}
Summary:        GStreamer JSON Plugin
License:        MPL-2.0
URL:            https://crates.io/crates/gst-plugin-json
Source0:        https://static.crates.io/crates/gst-plugin-json/gst-plugin-json-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n gstreamer1-plugin-json
Summary:        GStreamer JSON Plugin
License:        %{shrink:
    MIT AND
    MPL-2.0 AND
    (Apache-2.0 OR MIT) AND
    (Unlicense OR MIT)
}
Provides:       %{crate} = %{version}-%{release}
%description -n gstreamer1-plugin-json

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        GStreamer JSON Plugin
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        GStreamer JSON Plugin
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+doc-devel
Summary:        GStreamer JSON Plugin
BuildArch:      noarch
%description -n %{name}+doc-devel

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        GStreamer JSON Plugin
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
rm -v %{buildroot}/%{_libdir}/gstreamer-1.0/libgstjson.a
rm -v %{buildroot}/%{_libdir}/pkgconfig/gstjson.pc
%oreon_autofiles gstreamer1-plugin-json usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n gstreamer1-plugin-json -f %{oreon_filedir}/gstreamer1-plugin-json.list
%files -n rust-gst-plugin-json-devel -f %{oreon_filedir}/rust-gst-plugin-json-devel.list

%changelog

%autochangelog

%global source0_hash cf6687eda447b99865bb466da3b1a9ab501cb1d02db952162bc9f5d5fd87da31
%bcond check 1
%global crate gst-plugin-reqwest
Name:           rust-gst-plugin-reqwest
Version:        0.15.0
Release:        1%{?dist}
Summary:        GStreamer reqwest HTTP Source Plugin
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gst-plugin-reqwest
Source0:        https://static.crates.io/crates/gst-plugin-reqwest/gst-plugin-reqwest-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n gstreamer1-plugin-reqwest
Summary:        GStreamer reqwest HTTP Source Plugin
License:        %{shrink:
    Apache-2.0 AND
    BSD-3-Clause AND
    CDLA-Permissive-2.0 AND
    ISC AND
    MIT AND
    Unicode-3.0 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR ISC OR MIT) AND
    (Apache-2.0 OR MIT) AND
    (MIT OR Zlib OR Apache-2.0) AND
    (Unlicense OR MIT)
}
Provides:       %{crate} = %{version}-%{release}
%description -n gstreamer1-plugin-reqwest

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        GStreamer reqwest HTTP Source Plugin
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        GStreamer reqwest HTTP Source Plugin
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+doc-devel
Summary:        GStreamer reqwest HTTP Source Plugin
BuildArch:      noarch
%description -n %{name}+doc-devel

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        GStreamer reqwest HTTP Source Plugin
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
rm -v %{buildroot}/%{_libdir}/gstreamer-1.0/libgstreqwest.a
rm -v %{buildroot}/%{_libdir}/pkgconfig/gstreqwest.pc
%oreon_autofiles gstreamer1-plugin-reqwest usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n gstreamer1-plugin-reqwest -f %{oreon_filedir}/gstreamer1-plugin-reqwest.list
%files -n rust-gst-plugin-reqwest-devel -f %{oreon_filedir}/rust-gst-plugin-reqwest-devel.list

%changelog

%autochangelog

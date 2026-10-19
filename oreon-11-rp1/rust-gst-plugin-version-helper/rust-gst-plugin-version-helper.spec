%global source0_hash 94668bc2592732b8c2b653668ae41211d45988fb61264888b9c2d545d4bd826d
%bcond check 1
%global debug_package %{nil}
%global crate gst-plugin-version-helper
Name:           rust-gst-plugin-version-helper
Version:        0.8.4
Release:        1%{?dist}
Summary:        Build.rs helper function for GStreamer plugin metadata
License:        MIT
URL:            https://crates.io/crates/gst-plugin-version-helper
Source0:        https://static.crates.io/crates/gst-plugin-version-helper/gst-plugin-version-helper-%{version}.crate
Patch:          gst-plugin-version-helper-fix-metadata.diff
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
Summary:        Build.rs helper function for GStreamer plugin metadata
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-gst-plugin-version-helper-devel -f %{oreon_filedir}/rust-gst-plugin-version-helper-devel.list

%changelog

%autochangelog

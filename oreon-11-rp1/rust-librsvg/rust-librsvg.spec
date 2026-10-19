%global source0_hash c343d11cf050f7c9e35aceb66f9c6818cdca6c8f322c158242dba9833e21afa5
%bcond check 0
%global debug_package %{nil}
%global crate librsvg
Name:           rust-librsvg
Version:        2.62.0
Release:        1%{?dist}
Summary:        Library to render SVG images to Cairo surfaces
License:        LGPL-2.1-or-later
URL:            https://crates.io/crates/librsvg
Source0:        https://static.crates.io/crates/librsvg/librsvg-%{version}.crate
Patch:          librsvg-fix-metadata.diff
Patch2:         0001-Drop-unused-annotations-for-mutation-testing.patch
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
Summary:        Library to render SVG images to Cairo surfaces
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+avif-devel
Summary:        Library to render SVG images to Cairo surfaces
BuildArch:      noarch
%description -n %{name}+avif-devel

This package contains library source intended for building other packages which
use the "avif" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        Library to render SVG images to Cairo surfaces
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

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
%files -n rust-librsvg-devel -f %{oreon_filedir}/rust-librsvg-devel.list

%changelog

%autochangelog

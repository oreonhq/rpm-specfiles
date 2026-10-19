%global source0_hash 60d02eb2c9ccbbab470538fce34c7bc3be7b4e59268e65a3171367b296cdb842
%bcond check 1
%global debug_package %{nil}
%global crate image-extras
Name:           rust-image-extras
Version:        0.1.1
Release:        1%{?dist}
Summary:        Additional image format decoders for the image crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/image-extras
Source0:        https://static.crates.io/crates/image-extras/image-extras-%{version}.crate
Patch:          image-extras-fix-metadata.diff
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
Summary:        Additional image format decoders for the image crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+xbm-devel
Summary:        Additional image format decoders for the image crate
BuildArch:      noarch
%description -n %{name}+xbm-devel

This package contains library source intended for building other packages which
use the "xbm" feature of the "%{crate}" crate.

%package     -n %{name}+xpm-devel
Summary:        Additional image format decoders for the image crate
BuildArch:      noarch
%description -n %{name}+xpm-devel

This package contains library source intended for building other packages which
use the "xpm" feature of the "%{crate}" crate.

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

%{cargo_test -- -- %{shrink:
    --skip xbm::tests::image_with_hotspot
    --skip xbm::tests::image_without_hotspot
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-image-extras-devel -f %{oreon_filedir}/rust-image-extras-devel.list

%changelog

%autochangelog

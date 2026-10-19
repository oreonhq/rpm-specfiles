%global source0_hash 72ce181e3f6bf82d6c1dc569103ca7b1bd964c60ba03d7e6cdfbb3e3eb7f7405
%bcond check 0
%global debug_package %{nil}
%global crate plotters-bitmap
Name:           rust-plotters-bitmap
Version:        0.3.7
Release:        1%{?dist}
Summary:        Plotters Bitmap Backend
License:        MIT
URL:            https://crates.io/crates/plotters-bitmap
Source0:        https://static.crates.io/crates/plotters-bitmap/plotters-bitmap-%{version}.crate
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
Summary:        Plotters Bitmap Backend
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gif-devel
Summary:        Plotters Bitmap Backend
BuildArch:      noarch
%description -n %{name}+gif-devel

This package contains library source intended for building other packages which
use the "gif" feature of the "%{crate}" crate.

%package     -n %{name}+gif_backend-devel
Summary:        Plotters Bitmap Backend
BuildArch:      noarch
%description -n %{name}+gif_backend-devel

This package contains library source intended for building other packages which
use the "gif_backend" feature of the "%{crate}" crate.

%package     -n %{name}+image_encoder-devel
Summary:        Plotters Bitmap Backend
BuildArch:      noarch
%description -n %{name}+image_encoder-devel

This package contains library source intended for building other packages which
use the "image_encoder" feature of the "%{crate}" crate.

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
%files -n rust-plotters-bitmap-devel -f %{oreon_filedir}/rust-plotters-bitmap-devel.list

%changelog

%autochangelog

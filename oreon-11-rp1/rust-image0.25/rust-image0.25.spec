%global source0_hash 85ab80394333c02fe689eaf900ab500fbd0c2213da414687ebf995a65d5a6104
%bcond check 0
%global debug_package %{nil}
%global crate image
Name:           rust-image0.25
Version:        0.25.10
Release:        1%{?dist}
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/image
Source0:        https://static.crates.io/crates/image/image-%{version}.crate
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
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+avif-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+avif-devel

This package contains library source intended for building other packages which
use the "avif" feature of the "%{crate}" crate.

%package     -n %{name}+avif-native-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+avif-native-devel

This package contains library source intended for building other packages which
use the "avif-native" feature of the "%{crate}" crate.

%package     -n %{name}+benchmarks-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+benchmarks-devel

This package contains library source intended for building other packages which
use the "benchmarks" feature of the "%{crate}" crate.

%package     -n %{name}+bmp-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+bmp-devel

This package contains library source intended for building other packages which
use the "bmp" feature of the "%{crate}" crate.

%package     -n %{name}+color_quant-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+color_quant-devel

This package contains library source intended for building other packages which
use the "color_quant" feature of the "%{crate}" crate.

%package     -n %{name}+dav1d-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+dav1d-devel

This package contains library source intended for building other packages which
use the "dav1d" feature of the "%{crate}" crate.

%package     -n %{name}+dds-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+dds-devel

This package contains library source intended for building other packages which
use the "dds" feature of the "%{crate}" crate.

%package     -n %{name}+default-formats-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+default-formats-devel

This package contains library source intended for building other packages which
use the "default-formats" feature of the "%{crate}" crate.

%package     -n %{name}+exr-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+exr-devel

This package contains library source intended for building other packages which
use the "exr" feature of the "%{crate}" crate.

%package     -n %{name}+ff-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+ff-devel

This package contains library source intended for building other packages which
use the "ff" feature of the "%{crate}" crate.

%package     -n %{name}+gif-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+gif-devel

This package contains library source intended for building other packages which
use the "gif" feature of the "%{crate}" crate.

%package     -n %{name}+hdr-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+hdr-devel

This package contains library source intended for building other packages which
use the "hdr" feature of the "%{crate}" crate.

%package     -n %{name}+ico-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+ico-devel

This package contains library source intended for building other packages which
use the "ico" feature of the "%{crate}" crate.

%package     -n %{name}+image-webp-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+image-webp-devel

This package contains library source intended for building other packages which
use the "image-webp" feature of the "%{crate}" crate.

%package     -n %{name}+jpeg-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+jpeg-devel

This package contains library source intended for building other packages which
use the "jpeg" feature of the "%{crate}" crate.

%package     -n %{name}+mp4parse-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+mp4parse-devel

This package contains library source intended for building other packages which
use the "mp4parse" feature of the "%{crate}" crate.

%package     -n %{name}+nasm-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+nasm-devel

This package contains library source intended for building other packages which
use the "nasm" feature of the "%{crate}" crate.

%package     -n %{name}+png-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+png-devel

This package contains library source intended for building other packages which
use the "png" feature of the "%{crate}" crate.

%package     -n %{name}+pnm-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+pnm-devel

This package contains library source intended for building other packages which
use the "pnm" feature of the "%{crate}" crate.

%package     -n %{name}+qoi-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+qoi-devel

This package contains library source intended for building other packages which
use the "qoi" feature of the "%{crate}" crate.

%package     -n %{name}+ravif-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+ravif-devel

This package contains library source intended for building other packages which
use the "ravif" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+rgb-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+rgb-devel

This package contains library source intended for building other packages which
use the "rgb" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+tga-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+tga-devel

This package contains library source intended for building other packages which
use the "tga" feature of the "%{crate}" crate.

%package     -n %{name}+tiff-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+tiff-devel

This package contains library source intended for building other packages which
use the "tiff" feature of the "%{crate}" crate.

%package     -n %{name}+webp-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+webp-devel

This package contains library source intended for building other packages which
use the "webp" feature of the "%{crate}" crate.

%package     -n %{name}+zune-core-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+zune-core-devel

This package contains library source intended for building other packages which
use the "zune-core" feature of the "%{crate}" crate.

%package     -n %{name}+zune-jpeg-devel
Summary:        Imaging library. Provides basic image processing and encoders/decoder...
BuildArch:      noarch
%description -n %{name}+zune-jpeg-devel

This package contains library source intended for building other packages which
use the "zune-jpeg" feature of the "%{crate}" crate.

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
%files -n rust-image0.25-devel -f %{oreon_filedir}/rust-image0.25-devel.list

%changelog

%autochangelog

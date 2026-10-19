%global source0_hash eeba013228b7f744e2ede32bbc4ea9056a9a27910e2ff61fdb146f94ed89f7ea
%bcond check 1
%global debug_package %{nil}
%global crate libheif-rs
Name:           rust-libheif-rs
Version:        3.0.0
Release:        1%{?dist}
Summary:        Safe wrapper around the libheif-sys crate for parsing heif/heic files
License:        MIT
URL:            https://crates.io/crates/libheif-rs
Source0:        https://static.crates.io/crates/libheif-rs/libheif-rs-%{version}.crate
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
Summary:        Safe wrapper around the libheif-sys crate for parsing heif/heic files
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        Safe wrapper around the libheif-sys crate for parsing heif/heic files
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+latest-devel
Summary:        Safe wrapper around the libheif-sys crate for parsing heif/heic files
BuildArch:      noarch
%description -n %{name}+latest-devel

This package contains library source intended for building other packages which
use the "latest" feature of the "%{crate}" crate.

%package     -n %{name}+v1_17-devel
Summary:        Safe wrapper around the libheif-sys crate for parsing heif/heic files
BuildArch:      noarch
%description -n %{name}+v1_17-devel

This package contains library source intended for building other packages which
use the "v1_17" feature of the "%{crate}" crate.

%package     -n %{name}+v1_18-devel
Summary:        Safe wrapper around the libheif-sys crate for parsing heif/heic files
BuildArch:      noarch
%description -n %{name}+v1_18-devel

This package contains library source intended for building other packages which
use the "v1_18" feature of the "%{crate}" crate.

%package     -n %{name}+v1_19-devel
Summary:        Safe wrapper around the libheif-sys crate for parsing heif/heic files
BuildArch:      noarch
%description -n %{name}+v1_19-devel

This package contains library source intended for building other packages which
use the "v1_19" feature of the "%{crate}" crate.

%package     -n %{name}+v1_20-devel
Summary:        Safe wrapper around the libheif-sys crate for parsing heif/heic files
BuildArch:      noarch
%description -n %{name}+v1_20-devel

This package contains library source intended for building other packages which
use the "v1_20" feature of the "%{crate}" crate.

%package     -n %{name}+v1_21-devel
Summary:        Safe wrapper around the libheif-sys crate for parsing heif/heic files
BuildArch:      noarch
%description -n %{name}+v1_21-devel

This package contains library source intended for building other packages which
use the "v1_21" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f image
%install
%cargo_install -f image
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%{cargo_test -f image -- -- --exact %{shrink:
    --skip get_auxiliary_images
    --skip test_nclx_color_profile_of_handle_and_image
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-libheif-rs-devel -f %{oreon_filedir}/rust-libheif-rs-devel.list

%changelog

%autochangelog

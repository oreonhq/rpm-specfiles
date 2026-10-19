%global source0_hash 5e2ec995d822e05cabc3f06d196ee43650af3fe4fe38012cacb35e0c3d113b68
%bcond check 0
%global debug_package %{nil}
%global crate lopdf
Name:           rust-lopdf0.44
Version:        0.44.0
Release:        1%{?dist}
Summary:        Rust library for PDF document manipulation
License:        MIT
URL:            https://crates.io/crates/lopdf
Source0:        https://static.crates.io/crates/lopdf/lopdf-%{version}.crate
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
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-devel
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+async-devel

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+embed_image-devel
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+embed_image-devel

This package contains library source intended for building other packages which
use the "embed_image" feature of the "%{crate}" crate.

%package     -n %{name}+font_embedding-devel
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+font_embedding-devel

This package contains library source intended for building other packages which
use the "font_embedding" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+jiff-devel
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+jiff-devel

This package contains library source intended for building other packages which
use the "jiff" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+wasm_js-devel
Summary:        Rust library for PDF document manipulation
BuildArch:      noarch
%description -n %{name}+wasm_js-devel

This package contains library source intended for building other packages which
use the "wasm_js" feature of the "%{crate}" crate.

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
%files -n rust-lopdf0.44-devel -f %{oreon_filedir}/rust-lopdf0.44-devel.list

%changelog

%autochangelog

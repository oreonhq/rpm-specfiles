%global source0_hash b63feaf3343d35b6ca4d50483f94843803b0f51634937cc2ec519fc32232bc52
%bcond check 0
%global debug_package %{nil}
%global crate tiff
Name:           rust-tiff0.11
Version:        0.11.3
Release:        1%{?dist}
Summary:        TIFF decoding and encoding library in pure Rust
License:        MIT
URL:            https://crates.io/crates/tiff
Source0:        https://static.crates.io/crates/tiff/tiff-%{version}.crate
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
Summary:        TIFF decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-devel
Summary:        TIFF decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+deflate-devel

This package contains library source intended for building other packages which
use the "deflate" feature of the "%{crate}" crate.

%package     -n %{name}+fax-devel
Summary:        TIFF decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+fax-devel

This package contains library source intended for building other packages which
use the "fax" feature of the "%{crate}" crate.

%package     -n %{name}+fax34-devel
Summary:        TIFF decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+fax34-devel

This package contains library source intended for building other packages which
use the "fax34" feature of the "%{crate}" crate.

%package     -n %{name}+flate2-devel
Summary:        TIFF decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+flate2-devel

This package contains library source intended for building other packages which
use the "flate2" feature of the "%{crate}" crate.

%package     -n %{name}+image-webp-devel
Summary:        TIFF decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+image-webp-devel

This package contains library source intended for building other packages which
use the "image-webp" feature of the "%{crate}" crate.

%package     -n %{name}+jpeg-devel
Summary:        TIFF decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+jpeg-devel

This package contains library source intended for building other packages which
use the "jpeg" feature of the "%{crate}" crate.

%package     -n %{name}+lzw-devel
Summary:        TIFF decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+lzw-devel

This package contains library source intended for building other packages which
use the "lzw" feature of the "%{crate}" crate.

%package     -n %{name}+webp-devel
Summary:        TIFF decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+webp-devel

This package contains library source intended for building other packages which
use the "webp" feature of the "%{crate}" crate.

%package     -n %{name}+weezl-devel
Summary:        TIFF decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+weezl-devel

This package contains library source intended for building other packages which
use the "weezl" feature of the "%{crate}" crate.

%package     -n %{name}+zstd-devel
Summary:        TIFF decoding and encoding library in pure Rust
BuildArch:      noarch
%description -n %{name}+zstd-devel

This package contains library source intended for building other packages which
use the "zstd" feature of the "%{crate}" crate.

%package     -n %{name}+zune-jpeg-devel
Summary:        TIFF decoding and encoding library in pure Rust
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
%files -n rust-tiff0.11-devel -f %{oreon_filedir}/rust-tiff0.11-devel.list

%changelog

%autochangelog

%global source3_hash 51b50e6120c344dcc146bbd6375ca1c78e079d97c8bea76e67a53d6ff0efebac
%global source2_hash 0cec06e0e55fbc3dc5cee4fca9b607f66cb8f4e4dbcf3b3c013594dd156732e9
%global source0_hash bab0c77d09c0d9b144d429d0bf0fcd4c63c01d5f6c33f9b8ed501283e0f1ef76
%bcond check 1
%global debug_package %{nil}
%global crate hayro-jpeg2000
Name:           rust-hayro-jpeg2000
Version:        0.4.0
Release:        1%{?dist}
Summary:        Memory-safe, pure-Rust JPEG 2000 decoder
License:        (Apache-2.0 OR MIT) AND CC0-1.0
URL:            https://crates.io/crates/hayro-jpeg2000
Source0:        https://static.crates.io/crates/hayro-jpeg2000/hayro-jpeg2000-%{version}.crate
Source2:        https://github.com/LaurenzV/hayro/raw/refs/tags/%{crate}-v%{version}/LICENSE-APACHE
Source3:        https://github.com/LaurenzV/hayro/raw/refs/tags/%{crate}-v%{version}/LICENSE-MIT
Patch:          hayro-jpeg2000-fix-metadata.diff
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
Summary:        Memory-safe, pure-Rust JPEG 2000 decoder
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+fearless_simd-devel
Summary:        Memory-safe, pure-Rust JPEG 2000 decoder
BuildArch:      noarch
%description -n %{name}+fearless_simd-devel

This package contains library source intended for building other packages which
use the "fearless_simd" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        Memory-safe, pure-Rust JPEG 2000 decoder
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Memory-safe, pure-Rust JPEG 2000 decoder
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        Memory-safe, pure-Rust JPEG 2000 decoder
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Memory-safe, pure-Rust JPEG 2000 decoder
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %SOURCE2 %SOURCE3 .
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
%files -n rust-hayro-jpeg2000-devel -f %{oreon_filedir}/rust-hayro-jpeg2000-devel.list

%changelog

%autochangelog

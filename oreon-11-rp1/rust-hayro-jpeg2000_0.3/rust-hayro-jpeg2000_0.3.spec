%global source0_hash c75ab947623ef4ccaa7acf0579edf7cbb5a73838e3839a7be73335e522f433a1
%bcond check 0
%global debug_package %{nil}
%global crate hayro-jpeg2000
Name:           rust-hayro-jpeg2000_0.3
Version:        0.3.5
Release:        1%{?dist}
Summary:        Memory-safe, pure-Rust JPEG 2000 decoder
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/hayro-jpeg2000
Source0:        https://static.crates.io/crates/hayro-jpeg2000/hayro-jpeg2000-%{version}.crate
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
%files -n rust-hayro-jpeg2000_0.3-devel -f %{oreon_filedir}/rust-hayro-jpeg2000_0.3-devel.list

%changelog

%autochangelog

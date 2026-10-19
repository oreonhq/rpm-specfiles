%global source0_hash 0b0b36cbb4e6704f12f5b5d7b01dac593982c6550859ebd5a66fb15c9ea27fd5
%bcond check 1
%global debug_package %{nil}
%global crate jpeg-encoder
Name:           rust-jpeg-encoder
Version:        0.7.0
Release:        1%{?dist}
Summary:        JPEG encoder
License:        (MIT OR Apache-2.0) AND IJG
URL:            https://crates.io/crates/jpeg-encoder
Source0:        https://static.crates.io/crates/jpeg-encoder/jpeg-encoder-%{version}.crate
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
Summary:        JPEG encoder
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+benchmark-devel
Summary:        JPEG encoder
BuildArch:      noarch
%description -n %{name}+benchmark-devel

This package contains library source intended for building other packages which
use the "benchmark" feature of the "%{crate}" crate.

%package     -n %{name}+simd-devel
Summary:        JPEG encoder
BuildArch:      noarch
%description -n %{name}+simd-devel

This package contains library source intended for building other packages which
use the "simd" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        JPEG encoder
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
%files -n rust-jpeg-encoder-devel -f %{oreon_filedir}/rust-jpeg-encoder-devel.list

%changelog

%autochangelog

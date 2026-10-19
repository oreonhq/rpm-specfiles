%global source2_hash 71674605ec4c087fe9eb534e3e4f9e26eb2e4aabcd76a29fd156c6a844d44b3d
%global source0_hash 339abbe78e73178762e23bea9dfd08e697eb3f3301cd4be981c0f78ba5859195
%bcond check 1
%global debug_package %{nil}
%global crate base64-simd
Name:           rust-base64-simd
Version:        0.8.0
Release:        1%{?dist}
Summary:        SIMD-accelerated base64 encoding and decoding
License:        MIT
URL:            https://crates.io/crates/base64-simd
Source0:        https://static.crates.io/crates/base64-simd/base64-simd-%{version}.crate
Source2:        https://raw.githubusercontent.com/Nugine/simd/refs/tags/v0.8.0/LICENSE
Patch:          base64-simd-fix-metadata-auto.diff
Patch:          base64-simd-fix-metadata.diff
Patch2:         base64-simd-update-base64-to-0_21.diff
Patch3:         base64-simd-update-rand-to-0.10.diff
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
Summary:        SIMD-accelerated base64 encoding and decoding
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        SIMD-accelerated base64 encoding and decoding
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+detect-devel
Summary:        SIMD-accelerated base64 encoding and decoding
BuildArch:      noarch
%description -n %{name}+detect-devel

This package contains library source intended for building other packages which
use the "detect" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        SIMD-accelerated base64 encoding and decoding
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        SIMD-accelerated base64 encoding and decoding
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %{SOURCE2} .
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
%files -n rust-base64-simd-devel -f %{oreon_filedir}/rust-base64-simd-devel.list

%changelog

%autochangelog

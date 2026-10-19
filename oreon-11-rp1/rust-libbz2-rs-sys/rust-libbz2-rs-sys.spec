%global source0_hash 2c4a545a15244c7d945065b5d392b2d2d7f21526fba56ce51467b06ed445e8f7
%bcond check 1
%global debug_package %{nil}
%global crate libbz2-rs-sys
Name:           rust-libbz2-rs-sys
Version:        0.2.2
Release:        1%{?dist}
Summary:        Drop-in compatible rust bzip2 implementation
License:        bzip2-1.0.6
URL:            https://crates.io/crates/libbz2-rs-sys
Source0:        https://static.crates.io/crates/libbz2-rs-sys/libbz2-rs-sys-%{version}.crate
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
Summary:        Drop-in compatible rust bzip2 implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+c-allocator-devel
Summary:        Drop-in compatible rust bzip2 implementation
BuildArch:      noarch
%description -n %{name}+c-allocator-devel

This package contains library source intended for building other packages which
use the "c-allocator" feature of the "%{crate}" crate.

%package     -n %{name}+custom-prefix-devel
Summary:        Drop-in compatible rust bzip2 implementation
BuildArch:      noarch
%description -n %{name}+custom-prefix-devel

This package contains library source intended for building other packages which
use the "custom-prefix" feature of the "%{crate}" crate.

%package     -n %{name}+export-symbols-devel
Summary:        Drop-in compatible rust bzip2 implementation
BuildArch:      noarch
%description -n %{name}+export-symbols-devel

This package contains library source intended for building other packages which
use the "export-symbols" feature of the "%{crate}" crate.

%package     -n %{name}+rust-allocator-devel
Summary:        Drop-in compatible rust bzip2 implementation
BuildArch:      noarch
%description -n %{name}+rust-allocator-devel

This package contains library source intended for building other packages which
use the "rust-allocator" feature of the "%{crate}" crate.

%package     -n %{name}+semver-prefix-devel
Summary:        Drop-in compatible rust bzip2 implementation
BuildArch:      noarch
%description -n %{name}+semver-prefix-devel

This package contains library source intended for building other packages which
use the "semver-prefix" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Drop-in compatible rust bzip2 implementation
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+stdio-devel
Summary:        Drop-in compatible rust bzip2 implementation
BuildArch:      noarch
%description -n %{name}+stdio-devel

This package contains library source intended for building other packages which
use the "stdio" feature of the "%{crate}" crate.

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
%files -n rust-libbz2-rs-sys-devel -f %{oreon_filedir}/rust-libbz2-rs-sys-devel.list

%changelog

%autochangelog

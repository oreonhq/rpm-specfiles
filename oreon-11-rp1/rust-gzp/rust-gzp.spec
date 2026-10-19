%global source0_hash 661d8307941355219635daa5ce1b110a247a17e6e49a2d8be2058d51b7d5f317
%bcond check 1
%global debug_package %{nil}
%global crate gzp
Name:           rust-gzp
Version:        2.0.4
Release:        1%{?dist}
Summary:        Parallel Compression
License:        Unlicense OR MIT
URL:            https://crates.io/crates/gzp
Source0:        https://static.crates.io/crates/gzp/gzp-%{version}.crate
Patch:          gzp-fix-metadata.diff
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
Summary:        Parallel Compression
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+any_zlib-devel
Summary:        Parallel Compression
BuildArch:      noarch
%description -n %{name}+any_zlib-devel

This package contains library source intended for building other packages which
use the "any_zlib" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-devel
Summary:        Parallel Compression
BuildArch:      noarch
%description -n %{name}+deflate-devel

This package contains library source intended for building other packages which
use the "deflate" feature of the "%{crate}" crate.

%package     -n %{name}+deflate_default-devel
Summary:        Parallel Compression
BuildArch:      noarch
%description -n %{name}+deflate_default-devel

This package contains library source intended for building other packages which
use the "deflate_default" feature of the "%{crate}" crate.

%package     -n %{name}+deflate_rust-devel
Summary:        Parallel Compression
BuildArch:      noarch
%description -n %{name}+deflate_rust-devel

This package contains library source intended for building other packages which
use the "deflate_rust" feature of the "%{crate}" crate.

%package     -n %{name}+deflate_zlib_ng-devel
Summary:        Parallel Compression
BuildArch:      noarch
%description -n %{name}+deflate_zlib_ng-devel

This package contains library source intended for building other packages which
use the "deflate_zlib_ng" feature of the "%{crate}" crate.

%package     -n %{name}+flate2-devel
Summary:        Parallel Compression
BuildArch:      noarch
%description -n %{name}+flate2-devel

This package contains library source intended for building other packages which
use the "flate2" feature of the "%{crate}" crate.

%package     -n %{name}+libdeflate-devel
Summary:        Parallel Compression
BuildArch:      noarch
%description -n %{name}+libdeflate-devel

This package contains library source intended for building other packages which
use the "libdeflate" feature of the "%{crate}" crate.

%package     -n %{name}+libdeflater-devel
Summary:        Parallel Compression
BuildArch:      noarch
%description -n %{name}+libdeflater-devel

This package contains library source intended for building other packages which
use the "libdeflater" feature of the "%{crate}" crate.

%package     -n %{name}+libz-ng-sys-devel
Summary:        Parallel Compression
BuildArch:      noarch
%description -n %{name}+libz-ng-sys-devel

This package contains library source intended for building other packages which
use the "libz-ng-sys" feature of the "%{crate}" crate.

%package     -n %{name}+snap-devel
Summary:        Parallel Compression
BuildArch:      noarch
%description -n %{name}+snap-devel

This package contains library source intended for building other packages which
use the "snap" feature of the "%{crate}" crate.

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
%files -n rust-gzp-devel -f %{oreon_filedir}/rust-gzp-devel.list

%changelog

%autochangelog

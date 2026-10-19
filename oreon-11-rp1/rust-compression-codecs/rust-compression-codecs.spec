%global source0_hash 98fc98460ba0ad5317075d3632b8dfc45d0be8c4a49347c2a38272019717614a
%bcond check 1
%global debug_package %{nil}
%global crate compression-codecs
Name:           rust-compression-codecs
Version:        0.4.45
Release:        1%{?dist}
Summary:        Adaptors for various compression algorithms
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/compression-codecs
Source0:        https://static.crates.io/crates/compression-codecs/compression-codecs-%{version}.crate
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
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-algorithms-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+all-algorithms-devel

This package contains library source intended for building other packages which
use the "all-algorithms" feature of the "%{crate}" crate.

%package     -n %{name}+brotli-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+brotli-devel

This package contains library source intended for building other packages which
use the "brotli" feature of the "%{crate}" crate.

%package     -n %{name}+brotli-mbrotli-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+brotli-mbrotli-devel

This package contains library source intended for building other packages which
use the "brotli-mbrotli" feature of the "%{crate}" crate.

%package     -n %{name}+bzip2-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+bzip2-devel

This package contains library source intended for building other packages which
use the "bzip2" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+deflate-devel

This package contains library source intended for building other packages which
use the "deflate" feature of the "%{crate}" crate.

%package     -n %{name}+deflate64-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+deflate64-devel

This package contains library source intended for building other packages which
use the "deflate64" feature of the "%{crate}" crate.

%package     -n %{name}+flate2-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+flate2-devel

This package contains library source intended for building other packages which
use the "flate2" feature of the "%{crate}" crate.

%package     -n %{name}+gzip-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+gzip-devel

This package contains library source intended for building other packages which
use the "gzip" feature of the "%{crate}" crate.

%package     -n %{name}+libzstd-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+libzstd-devel

This package contains library source intended for building other packages which
use the "libzstd" feature of the "%{crate}" crate.

%package     -n %{name}+lz4-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+lz4-devel

This package contains library source intended for building other packages which
use the "lz4" feature of the "%{crate}" crate.

%package     -n %{name}+lzma-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+lzma-devel

This package contains library source intended for building other packages which
use the "lzma" feature of the "%{crate}" crate.

%package     -n %{name}+memchr-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+memchr-devel

This package contains library source intended for building other packages which
use the "memchr" feature of the "%{crate}" crate.

%package     -n %{name}+xz-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+xz-devel

This package contains library source intended for building other packages which
use the "xz" feature of the "%{crate}" crate.

%package     -n %{name}+xz-parallel-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+xz-parallel-devel

This package contains library source intended for building other packages which
use the "xz-parallel" feature of the "%{crate}" crate.

%package     -n %{name}+xz2-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+xz2-devel

This package contains library source intended for building other packages which
use the "xz2" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+zlib-devel

This package contains library source intended for building other packages which
use the "zlib" feature of the "%{crate}" crate.

%package     -n %{name}+zstd-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+zstd-devel

This package contains library source intended for building other packages which
use the "zstd" feature of the "%{crate}" crate.

%package     -n %{name}+zstd-safe-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+zstd-safe-devel

This package contains library source intended for building other packages which
use the "zstd-safe" feature of the "%{crate}" crate.

%package     -n %{name}+zstdmt-devel
Summary:        Adaptors for various compression algorithms
BuildArch:      noarch
%description -n %{name}+zstdmt-devel

This package contains library source intended for building other packages which
use the "zstdmt" feature of the "%{crate}" crate.

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
%files -n rust-compression-codecs-devel -f %{oreon_filedir}/rust-compression-codecs-devel.list

%changelog

%autochangelog

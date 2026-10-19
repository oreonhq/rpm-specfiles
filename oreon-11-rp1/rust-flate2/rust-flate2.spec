%global source0_hash 6e634e2e0ebac1ee034020da1ca582e17ffe4e0f5e985823721e168928136dcb
%bcond check 1
%global debug_package %{nil}
%global crate flate2
Name:           rust-flate2
Version:        1.1.10
Release:        1%{?dist}
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/flate2
Source0:        https://static.crates.io/crates/flate2/flate2-%{version}.crate
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
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+any_c_zlib-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+any_c_zlib-devel

This package contains library source intended for building other packages which
use the "any_c_zlib" feature of the "%{crate}" crate.

%package     -n %{name}+any_impl-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+any_impl-devel

This package contains library source intended for building other packages which
use the "any_impl" feature of the "%{crate}" crate.

%package     -n %{name}+any_zlib-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+any_zlib-devel

This package contains library source intended for building other packages which
use the "any_zlib" feature of the "%{crate}" crate.

%package     -n %{name}+document-features-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+document-features-devel

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%package     -n %{name}+libz-ng-sys-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+libz-ng-sys-devel

This package contains library source intended for building other packages which
use the "libz-ng-sys" feature of the "%{crate}" crate.

%package     -n %{name}+libz-sys-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+libz-sys-devel

This package contains library source intended for building other packages which
use the "libz-sys" feature of the "%{crate}" crate.

%package     -n %{name}+miniz-sys-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+miniz-sys-devel

This package contains library source intended for building other packages which
use the "miniz-sys" feature of the "%{crate}" crate.

%package     -n %{name}+miniz_oxide-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+miniz_oxide-devel

This package contains library source intended for building other packages which
use the "miniz_oxide" feature of the "%{crate}" crate.

%package     -n %{name}+rust_backend-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+rust_backend-devel

This package contains library source intended for building other packages which
use the "rust_backend" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+zlib-devel

This package contains library source intended for building other packages which
use the "zlib" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-default-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+zlib-default-devel

This package contains library source intended for building other packages which
use the "zlib-default" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-ng-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+zlib-ng-devel

This package contains library source intended for building other packages which
use the "zlib-ng" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-rs-devel
Summary:        DEFLATE compression and decompression exposed as Read/BufRead/Write streams
BuildArch:      noarch
%description -n %{name}+zlib-rs-devel

This package contains library source intended for building other packages which
use the "zlib-rs" feature of the "%{crate}" crate.

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
%files -n rust-flate2-devel -f %{oreon_filedir}/rust-flate2-devel.list

%changelog

%autochangelog

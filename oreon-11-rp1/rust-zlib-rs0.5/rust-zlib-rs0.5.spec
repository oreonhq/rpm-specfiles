%global source0_hash 40990edd51aae2c2b6907af74ffb635029d5788228222c4bb811e9351c0caad3
%bcond check 0
%global debug_package %{nil}
%global crate zlib-rs
Name:           rust-zlib-rs0.5
Version:        0.5.5
Release:        1%{?dist}
Summary:        A memory-safe zlib implementation written in rust
License:        Zlib
URL:            https://crates.io/crates/zlib-rs
Source0:        https://static.crates.io/crates/zlib-rs/zlib-rs-%{version}.crate
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
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ZLIB_DEBUG-devel
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+ZLIB_DEBUG-devel

This package contains library source intended for building other packages which
use the "ZLIB_DEBUG" feature of the "%{crate}" crate.

%package     -n %{name}+__internal-fuzz-devel
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+__internal-fuzz-devel

This package contains library source intended for building other packages which
use the "__internal-fuzz" feature of the "%{crate}" crate.

%package     -n %{name}+__internal-fuzz-disable-checksum-devel
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+__internal-fuzz-disable-checksum-devel

This package contains library source intended for building other packages which
use the "__internal-fuzz-disable-checksum" feature of the "%{crate}" crate.

%package     -n %{name}+__internal-test-devel
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+__internal-test-devel

This package contains library source intended for building other packages which
use the "__internal-test" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+avx512-devel
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+avx512-devel

This package contains library source intended for building other packages which
use the "avx512" feature of the "%{crate}" crate.

%package     -n %{name}+c-allocator-devel
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+c-allocator-devel

This package contains library source intended for building other packages which
use the "c-allocator" feature of the "%{crate}" crate.

%package     -n %{name}+quickcheck-devel
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+quickcheck-devel

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%package     -n %{name}+rust-allocator-devel
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+rust-allocator-devel

This package contains library source intended for building other packages which
use the "rust-allocator" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+vpclmulqdq-devel
Summary:        A memory-safe zlib implementation written in rust
BuildArch:      noarch
%description -n %{name}+vpclmulqdq-devel

This package contains library source intended for building other packages which
use the "vpclmulqdq" feature of the "%{crate}" crate.

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
%files -n rust-zlib-rs0.5-devel -f %{oreon_filedir}/rust-zlib-rs0.5-devel.list

%changelog

%autochangelog

%global source0_hash 7c2c118cb077cca2822033836dfb1b975355dfb784b5e8da48f7b6c5db74e60e
%bcond check 0
%global debug_package %{nil}
%global crate rustls
Name:           rust-rustls0.23
Version:        0.23.39
Release:        1%{?dist}
Summary:        Rustls is a modern TLS library written in Rust.
License:        Apache-2.0 OR ISC OR MIT
URL:            https://crates.io/crates/rustls
Source0:        https://static.crates.io/crates/rustls/rustls-%{version}.crate
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
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-rs-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+aws-lc-rs-devel

This package contains library source intended for building other packages which
use the "aws-lc-rs" feature of the "%{crate}" crate.

%package     -n %{name}+aws_lc_rs-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+aws_lc_rs-devel

This package contains library source intended for building other packages which
use the "aws_lc_rs" feature of the "%{crate}" crate.

%package     -n %{name}+brotli-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+brotli-devel

This package contains library source intended for building other packages which
use the "brotli" feature of the "%{crate}" crate.

%package     -n %{name}+brotli-decompressor-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+brotli-decompressor-devel

This package contains library source intended for building other packages which
use the "brotli-decompressor" feature of the "%{crate}" crate.

%package     -n %{name}+custom-provider-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+custom-provider-devel

This package contains library source intended for building other packages which
use the "custom-provider" feature of the "%{crate}" crate.

%package     -n %{name}+fips-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+fips-devel

This package contains library source intended for building other packages which
use the "fips" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+prefer-post-quantum-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+prefer-post-quantum-devel

This package contains library source intended for building other packages which
use the "prefer-post-quantum" feature of the "%{crate}" crate.

%package     -n %{name}+read_buf-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+read_buf-devel

This package contains library source intended for building other packages which
use the "read_buf" feature of the "%{crate}" crate.

%package     -n %{name}+ring-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tls12-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+tls12-devel

This package contains library source intended for building other packages which
use the "tls12" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-devel
Summary:        Rustls is a modern TLS library written in Rust.
BuildArch:      noarch
%description -n %{name}+zlib-devel

This package contains library source intended for building other packages which
use the "zlib" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-rs-devel
Summary:        Rustls is a modern TLS library written in Rust.
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
%files -n rust-rustls0.23-devel -f %{oreon_filedir}/rust-rustls0.23-devel.list

%changelog

%autochangelog

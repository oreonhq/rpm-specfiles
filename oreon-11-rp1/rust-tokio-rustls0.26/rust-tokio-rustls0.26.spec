%global source0_hash b0c85f2c3ef0b1cd58b36682f4b17aaa995f0e5db534d85692b4903abce21f67
%bcond check 0
%global debug_package %{nil}
%global crate tokio-rustls
Name:           rust-tokio-rustls0.26
Version:        0.26.5
Release:        1%{?dist}
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tokio-rustls
Source0:        https://static.crates.io/crates/tokio-rustls/tokio-rustls-%{version}.crate
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
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-rs-devel
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls.
BuildArch:      noarch
%description -n %{name}+aws-lc-rs-devel

This package contains library source intended for building other packages which
use the "aws-lc-rs" feature of the "%{crate}" crate.

%package     -n %{name}+aws_lc_rs-devel
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls.
BuildArch:      noarch
%description -n %{name}+aws_lc_rs-devel

This package contains library source intended for building other packages which
use the "aws_lc_rs" feature of the "%{crate}" crate.

%package     -n %{name}+brotli-devel
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls.
BuildArch:      noarch
%description -n %{name}+brotli-devel

This package contains library source intended for building other packages which
use the "brotli" feature of the "%{crate}" crate.

%package     -n %{name}+early-data-devel
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls.
BuildArch:      noarch
%description -n %{name}+early-data-devel

This package contains library source intended for building other packages which
use the "early-data" feature of the "%{crate}" crate.

%package     -n %{name}+fips-devel
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls.
BuildArch:      noarch
%description -n %{name}+fips-devel

This package contains library source intended for building other packages which
use the "fips" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls.
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+ring-devel
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls.
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%package     -n %{name}+tls12-devel
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls.
BuildArch:      noarch
%description -n %{name}+tls12-devel

This package contains library source intended for building other packages which
use the "tls12" feature of the "%{crate}" crate.

%package     -n %{name}+zlib-devel
Summary:        Asynchronous TLS/SSL streams for Tokio using Rustls.
BuildArch:      noarch
%description -n %{name}+zlib-devel

This package contains library source intended for building other packages which
use the "zlib" feature of the "%{crate}" crate.

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
%files -n rust-tokio-rustls0.26-devel -f %{oreon_filedir}/rust-tokio-rustls0.26-devel.list

%changelog

%autochangelog

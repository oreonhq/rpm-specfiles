%global source0_hash 57e80b8f2dee9c7cd5ad441577a8f350cf67080205dd3415bbafa7998fc6b5cf
%bcond check 0
%global debug_package %{nil}
%global crate rustls-ffi
Name:           rust-rustls-ffi
Version:        0.15.3
Release:        1%{?dist}
Summary:        Rustls bindings for non-Rust languages
License:        Apache-2.0 OR ISC OR MIT
URL:            https://crates.io/crates/rustls-ffi
Source0:        https://static.crates.io/crates/rustls-ffi/rustls-ffi-%{version}.crate
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
Summary:        Rustls bindings for non-Rust languages
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-rs-devel
Summary:        Rustls bindings for non-Rust languages
BuildArch:      noarch
%description -n %{name}+aws-lc-rs-devel

This package contains library source intended for building other packages which
use the "aws-lc-rs" feature of the "%{crate}" crate.

%package     -n %{name}+capi-devel
Summary:        Rustls bindings for non-Rust languages
BuildArch:      noarch
%description -n %{name}+capi-devel

This package contains library source intended for building other packages which
use the "capi" feature of the "%{crate}" crate.

%package     -n %{name}+cert_compression-devel
Summary:        Rustls bindings for non-Rust languages
BuildArch:      noarch
%description -n %{name}+cert_compression-devel

This package contains library source intended for building other packages which
use the "cert_compression" feature of the "%{crate}" crate.

%package     -n %{name}+fips-devel
Summary:        Rustls bindings for non-Rust languages
BuildArch:      noarch
%description -n %{name}+fips-devel

This package contains library source intended for building other packages which
use the "fips" feature of the "%{crate}" crate.

%package     -n %{name}+no_log_capture-devel
Summary:        Rustls bindings for non-Rust languages
BuildArch:      noarch
%description -n %{name}+no_log_capture-devel

This package contains library source intended for building other packages which
use the "no_log_capture" feature of the "%{crate}" crate.

%package     -n %{name}+prefer-post-quantum-devel
Summary:        Rustls bindings for non-Rust languages
BuildArch:      noarch
%description -n %{name}+prefer-post-quantum-devel

This package contains library source intended for building other packages which
use the "prefer-post-quantum" feature of the "%{crate}" crate.

%package     -n %{name}+read_buf-devel
Summary:        Rustls bindings for non-Rust languages
BuildArch:      noarch
%description -n %{name}+read_buf-devel

This package contains library source intended for building other packages which
use the "read_buf" feature of the "%{crate}" crate.

%package     -n %{name}+ring-devel
Summary:        Rustls bindings for non-Rust languages
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

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
%files -n rust-rustls-ffi-devel -f %{oreon_filedir}/rust-rustls-ffi-devel.list

%changelog

%autochangelog

%global source0_hash ec3efd23720e2049821a693cbc7e65ea87c72f1c58ff2f9522ff332b1491e590
%bcond check 0
%global debug_package %{nil}
%global crate hyper-rustls
Name:           rust-hyper-rustls0.24
Version:        0.24.2
Release:        1%{?dist}
Summary:        Rustls+hyper integration for pure rust HTTPS
License:        Apache-2.0 OR ISC OR MIT
URL:            https://crates.io/crates/hyper-rustls
Source0:        https://static.crates.io/crates/hyper-rustls/hyper-rustls-%{version}.crate
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
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+acceptor-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+acceptor-devel

This package contains library source intended for building other packages which
use the "acceptor" feature of the "%{crate}" crate.

%package     -n %{name}+http1-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+http1-devel

This package contains library source intended for building other packages which
use the "http1" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+native-tokio-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+native-tokio-devel

This package contains library source intended for building other packages which
use the "native-tokio" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-native-certs-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+rustls-native-certs-devel

This package contains library source intended for building other packages which
use the "rustls-native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+tls12-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+tls12-devel

This package contains library source intended for building other packages which
use the "tls12" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-runtime-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+tokio-runtime-devel

This package contains library source intended for building other packages which
use the "tokio-runtime" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+webpki-roots-devel

This package contains library source intended for building other packages which
use the "webpki-roots" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-tokio-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+webpki-tokio-devel

This package contains library source intended for building other packages which
use the "webpki-tokio" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip client --skip custom_ca_store --skip server
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-hyper-rustls0.24-devel -f %{oreon_filedir}/rust-hyper-rustls0.24-devel.list

%changelog

%autochangelog

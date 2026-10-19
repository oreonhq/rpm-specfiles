%global source0_hash 33ca68d021ef39cf6463ab54c1d0f5daf03377b70561305bb89a8f83aab66e0f
%bcond check 1
%global debug_package %{nil}
%global crate hyper-rustls
Name:           rust-hyper-rustls
Version:        0.27.9
Release:        1%{?dist}
Summary:        Rustls+hyper integration for pure rust HTTPS
License:        Apache-2.0 OR ISC OR MIT
URL:            https://crates.io/crates/hyper-rustls
Source0:        https://static.crates.io/crates/hyper-rustls/hyper-rustls-%{version}.crate
Patch:          hyper-rustls-fix-metadata.diff
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

%package     -n %{name}+ring-devel
Summary:        Rustls+hyper integration for pure rust HTTPS
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

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

%{cargo_test -- --lib -- %{shrink:
    --skip connector::tests::connects_http
    --skip connector::tests::connects_https
    --skip connector::tests::connects_https_only
}}
%cargo_test -- --doc
%{cargo_test -- --test tests -- %{shrink:
    --skip client
    --skip custom_ca_store
    --skip server
}}
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-hyper-rustls-devel -f %{oreon_filedir}/rust-hyper-rustls-devel.list

%changelog

%autochangelog

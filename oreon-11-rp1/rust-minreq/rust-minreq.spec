%global source0_hash 05015102dad0f7d61691ca347e9d9d9006685a64aefb3d79eecf62665de2153d
%bcond check 1
%global debug_package %{nil}
%global crate minreq
Name:           rust-minreq
Version:        2.14.1
Release:        1%{?dist}
Summary:        Simple, minimal-dependency HTTP client
License:        ISC
URL:            https://crates.io/crates/minreq
Source0:        https://static.crates.io/crates/minreq/minreq-%{version}.crate
Patch:          minreq-fix-metadata.diff
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
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+https-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+https-devel

This package contains library source intended for building other packages which
use the "https" feature of the "%{crate}" crate.

%package     -n %{name}+https-native-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+https-native-devel

This package contains library source intended for building other packages which
use the "https-native" feature of the "%{crate}" crate.

%package     -n %{name}+https-rustls-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+https-rustls-devel

This package contains library source intended for building other packages which
use the "https-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+https-rustls-probe-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+https-rustls-probe-devel

This package contains library source intended for building other packages which
use the "https-rustls-probe" feature of the "%{crate}" crate.

%package     -n %{name}+json-using-serde-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+json-using-serde-devel

This package contains library source intended for building other packages which
use the "json-using-serde" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+proxy-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+proxy-devel

This package contains library source intended for building other packages which
use the "proxy" feature of the "%{crate}" crate.

%package     -n %{name}+punycode-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+punycode-devel

This package contains library source intended for building other packages which
use the "punycode" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-native-certs-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+rustls-native-certs-devel

This package contains library source intended for building other packages which
use the "rustls-native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-webpki-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+rustls-webpki-devel

This package contains library source intended for building other packages which
use the "rustls-webpki" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%package     -n %{name}+urlencoding-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+urlencoding-devel

This package contains library source intended for building other packages which
use the "urlencoding" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Simple, minimal-dependency HTTP client
BuildArch:      noarch
%description -n %{name}+webpki-roots-devel

This package contains library source intended for building other packages which
use the "webpki-roots" feature of the "%{crate}" crate.

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

%cargo_test -- --lib
%cargo_test -- --tests
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-minreq-devel -f %{oreon_filedir}/rust-minreq-devel.list

%changelog

%autochangelog

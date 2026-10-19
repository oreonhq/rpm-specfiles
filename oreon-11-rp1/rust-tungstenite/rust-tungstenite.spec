%global source0_hash 6c01152af293afb9c7c2a57e4b559c5620b421f6d133261c60dd2d0cdb38e6b8
%bcond check 0
%global debug_package %{nil}
%global crate tungstenite
Name:           rust-tungstenite
Version:        0.29.0
Release:        1%{?dist}
Summary:        Lightweight stream-based WebSocket implementation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/tungstenite
Source0:        https://static.crates.io/crates/tungstenite/tungstenite-%{version}.crate
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
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__rustls-tls-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+__rustls-tls-devel

This package contains library source intended for building other packages which
use the "__rustls-tls" feature of the "%{crate}" crate.

%package     -n %{name}+data-encoding-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+data-encoding-devel

This package contains library source intended for building other packages which
use the "data-encoding" feature of the "%{crate}" crate.

%package     -n %{name}+handshake-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+handshake-devel

This package contains library source intended for building other packages which
use the "handshake" feature of the "%{crate}" crate.

%package     -n %{name}+http-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+http-devel

This package contains library source intended for building other packages which
use the "http" feature of the "%{crate}" crate.

%package     -n %{name}+httparse-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+httparse-devel

This package contains library source intended for building other packages which
use the "httparse" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-crate-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+native-tls-crate-devel

This package contains library source intended for building other packages which
use the "native-tls-crate" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-vendored-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+native-tls-vendored-devel

This package contains library source intended for building other packages which
use the "native-tls-vendored" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-native-certs-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+rustls-native-certs-devel

This package contains library source intended for building other packages which
use the "rustls-native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-pki-types-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+rustls-pki-types-devel

This package contains library source intended for building other packages which
use the "rustls-pki-types" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-native-roots-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+rustls-tls-native-roots-devel

This package contains library source intended for building other packages which
use the "rustls-tls-native-roots" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-tls-webpki-roots-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+rustls-tls-webpki-roots-devel

This package contains library source intended for building other packages which
use the "rustls-tls-webpki-roots" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+url-devel
Summary:        Lightweight stream-based WebSocket implementation
BuildArch:      noarch
%description -n %{name}+url-devel

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Lightweight stream-based WebSocket implementation
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

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tungstenite-devel -f %{oreon_filedir}/rust-tungstenite-devel.list

%changelog

%autochangelog

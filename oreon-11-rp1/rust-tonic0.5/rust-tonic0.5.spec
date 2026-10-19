%global source0_hash 796c5e1cd49905e65dd8e700d4cb1dffcbfdb4fc9d017de08c1a537afd83627c
%bcond check 0
%global debug_package %{nil}
%global crate tonic
Name:           rust-tonic0.5
Version:        0.5.2
Release:        1%{?dist}
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
License:        MIT
URL:            https://crates.io/crates/tonic
Source0:        https://static.crates.io/crates/tonic/tonic-%{version}.crate
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
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-trait-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+async-trait-devel

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%package     -n %{name}+codegen-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+codegen-devel

This package contains library source intended for building other packages which
use the "codegen" feature of the "%{crate}" crate.

%package     -n %{name}+compression-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+compression-devel

This package contains library source intended for building other packages which
use the "compression" feature of the "%{crate}" crate.

%package     -n %{name}+flate2-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+flate2-devel

This package contains library source intended for building other packages which
use the "flate2" feature of the "%{crate}" crate.

%package     -n %{name}+h2-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+h2-devel

This package contains library source intended for building other packages which
use the "h2" feature of the "%{crate}" crate.

%package     -n %{name}+hyper-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+hyper-devel

This package contains library source intended for building other packages which
use the "hyper" feature of the "%{crate}" crate.

%package     -n %{name}+hyper-timeout-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+hyper-timeout-devel

This package contains library source intended for building other packages which
use the "hyper-timeout" feature of the "%{crate}" crate.

%package     -n %{name}+prost-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+prost-devel

This package contains library source intended for building other packages which
use the "prost" feature of the "%{crate}" crate.

%package     -n %{name}+prost-derive-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+prost-derive-devel

This package contains library source intended for building other packages which
use the "prost-derive" feature of the "%{crate}" crate.

%package     -n %{name}+prost1-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+prost1-devel

This package contains library source intended for building other packages which
use the "prost1" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-native-certs-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+rustls-native-certs-devel

This package contains library source intended for building other packages which
use the "rustls-native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+tls-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tls-devel

This package contains library source intended for building other packages which
use the "tls" feature of the "%{crate}" crate.

%package     -n %{name}+tls-roots-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tls-roots-devel

This package contains library source intended for building other packages which
use the "tls-roots" feature of the "%{crate}" crate.

%package     -n %{name}+tls-roots-common-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tls-roots-common-devel

This package contains library source intended for building other packages which
use the "tls-roots-common" feature of the "%{crate}" crate.

%package     -n %{name}+tls-webpki-roots-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tls-webpki-roots-devel

This package contains library source intended for building other packages which
use the "tls-webpki-roots" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-rustls-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tokio-rustls-devel

This package contains library source intended for building other packages which
use the "tokio-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+tower-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tower-devel

This package contains library source intended for building other packages which
use the "tower" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-futures-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tracing-futures-devel

This package contains library source intended for building other packages which
use the "tracing-futures" feature of the "%{crate}" crate.

%package     -n %{name}+transport-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+transport-devel

This package contains library source intended for building other packages which
use the "transport" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
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
%files -n rust-tonic0.5-devel -f %{oreon_filedir}/rust-tonic0.5-devel.list

%changelog

%autochangelog

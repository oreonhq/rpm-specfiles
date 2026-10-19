%global source0_hash ac2a5518c70fa84342385732db33fb3f44bc4cc748936eb5833d2df34d6445ef
%bcond check 0
%global debug_package %{nil}
%global crate tonic
Name:           rust-tonic
Version:        0.14.6
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

%package     -n %{name}+_tls-any-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+_tls-any-devel

This package contains library source intended for building other packages which
use the "_tls-any" feature of the "%{crate}" crate.

%package     -n %{name}+channel-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+channel-devel

This package contains library source intended for building other packages which
use the "channel" feature of the "%{crate}" crate.

%package     -n %{name}+codegen-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+codegen-devel

This package contains library source intended for building other packages which
use the "codegen" feature of the "%{crate}" crate.

%package     -n %{name}+deflate-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+deflate-devel

This package contains library source intended for building other packages which
use the "deflate" feature of the "%{crate}" crate.

%package     -n %{name}+gzip-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+gzip-devel

This package contains library source intended for building other packages which
use the "gzip" feature of the "%{crate}" crate.

%package     -n %{name}+router-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+router-devel

This package contains library source intended for building other packages which
use the "router" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+tls-aws-lc-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tls-aws-lc-devel

This package contains library source intended for building other packages which
use the "tls-aws-lc" feature of the "%{crate}" crate.

%package     -n %{name}+tls-connect-info-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tls-connect-info-devel

This package contains library source intended for building other packages which
use the "tls-connect-info" feature of the "%{crate}" crate.

%package     -n %{name}+tls-native-roots-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tls-native-roots-devel

This package contains library source intended for building other packages which
use the "tls-native-roots" feature of the "%{crate}" crate.

%package     -n %{name}+tls-ring-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tls-ring-devel

This package contains library source intended for building other packages which
use the "tls-ring" feature of the "%{crate}" crate.

%package     -n %{name}+tls-webpki-roots-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+tls-webpki-roots-devel

This package contains library source intended for building other packages which
use the "tls-webpki-roots" feature of the "%{crate}" crate.

%package     -n %{name}+transport-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+transport-devel

This package contains library source intended for building other packages which
use the "transport" feature of the "%{crate}" crate.

%package     -n %{name}+zstd-devel
Summary:        A gRPC over HTTP/2 implementation focused on high performance, intero...
BuildArch:      noarch
%description -n %{name}+zstd-devel

This package contains library source intended for building other packages which
use the "zstd" feature of the "%{crate}" crate.

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
%files -n rust-tonic-devel -f %{oreon_filedir}/rust-tonic-devel.list

%changelog

%autochangelog

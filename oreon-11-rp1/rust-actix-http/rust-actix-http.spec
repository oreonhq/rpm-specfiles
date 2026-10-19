%global source0_hash 7926860314cbe2fb5d1f13731e387ab43bd32bca224e82e6e2db85de0a3dba49
%bcond check 0
%global debug_package %{nil}
%global crate actix-http
Name:           rust-actix-http
Version:        3.11.2
Release:        1%{?dist}
Summary:        HTTP types and services for the Actix ecosystem
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-http
Source0:        https://static.crates.io/crates/actix-http/actix-http-%{version}.crate
Patch:          actix-http-fix-metadata.diff
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
Summary:        HTTP types and services for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+__compress-devel
Summary:        HTTP types and services for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+__compress-devel

This package contains library source intended for building other packages which
use the "__compress" feature of the "%{crate}" crate.

%package     -n %{name}+__tls-devel
Summary:        HTTP types and services for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+__tls-devel

This package contains library source intended for building other packages which
use the "__tls" feature of the "%{crate}" crate.

%package     -n %{name}+actix-tls-devel
Summary:        HTTP types and services for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+actix-tls-devel

This package contains library source intended for building other packages which
use the "actix-tls" feature of the "%{crate}" crate.

%package     -n %{name}+compress-gzip-devel
Summary:        HTTP types and services for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+compress-gzip-devel

This package contains library source intended for building other packages which
use the "compress-gzip" feature of the "%{crate}" crate.

%package     -n %{name}+compress-zstd-devel
Summary:        HTTP types and services for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+compress-zstd-devel

This package contains library source intended for building other packages which
use the "compress-zstd" feature of the "%{crate}" crate.

%package     -n %{name}+http2-devel
Summary:        HTTP types and services for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+http2-devel

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-devel
Summary:        HTTP types and services for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+openssl-devel

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

%package     -n %{name}+ws-devel
Summary:        HTTP types and services for the Actix ecosystem
BuildArch:      noarch
%description -n %{name}+ws-devel

This package contains library source intended for building other packages which
use the "ws" feature of the "%{crate}" crate.

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
%files -n rust-actix-http-devel -f %{oreon_filedir}/rust-actix-http-devel.list

%changelog

%autochangelog

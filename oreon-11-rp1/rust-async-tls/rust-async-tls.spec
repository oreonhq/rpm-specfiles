%global source0_hash d85a97c4a0ecce878efd3f945f119c78a646d8975340bca0398f9bb05c30cc52
%bcond check 0
%global debug_package %{nil}
%global crate async-tls
Name:           rust-async-tls
Version:        0.10.0
Release:        1%{?dist}
Summary:        Asynchronous TLS/SSL streams using Rustls.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/async-tls
Source0:        https://static.crates.io/crates/async-tls/async-tls-%{version}.crate
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
Summary:        Asynchronous TLS/SSL streams using Rustls.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+client-devel
Summary:        Asynchronous TLS/SSL streams using Rustls.
BuildArch:      noarch
%description -n %{name}+client-devel

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%package     -n %{name}+early-data-devel
Summary:        Asynchronous TLS/SSL streams using Rustls.
BuildArch:      noarch
%description -n %{name}+early-data-devel

This package contains library source intended for building other packages which
use the "early-data" feature of the "%{crate}" crate.

%package     -n %{name}+server-devel
Summary:        Asynchronous TLS/SSL streams using Rustls.
BuildArch:      noarch
%description -n %{name}+server-devel

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-devel
Summary:        Asynchronous TLS/SSL streams using Rustls.
BuildArch:      noarch
%description -n %{name}+webpki-devel

This package contains library source intended for building other packages which
use the "webpki" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Asynchronous TLS/SSL streams using Rustls.
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
%files -n rust-async-tls-devel -f %{oreon_filedir}/rust-async-tls-devel.list

%changelog

%autochangelog

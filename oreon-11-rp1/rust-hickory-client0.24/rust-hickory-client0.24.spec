%global source0_hash 156579a5cd8d1fc6f0df87cc21b6ee870db978a163a1ba484acd98a4eff5a6de
%bcond check 1
%global debug_package %{nil}
%global crate hickory-client
Name:           rust-hickory-client0.24
Version:        0.24.4
Release:        1%{?dist}
Summary:        Hickory DNS is a safe and secure DNS library
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hickory-client
Source0:        https://static.crates.io/crates/hickory-client/hickory-client-%{version}.crate
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
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+backtrace-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+backtrace-devel

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%package     -n %{name}+dns-over-https-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dns-over-https-devel

This package contains library source intended for building other packages which
use the "dns-over-https" feature of the "%{crate}" crate.

%package     -n %{name}+dns-over-https-openssl-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dns-over-https-openssl-devel

This package contains library source intended for building other packages which
use the "dns-over-https-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+dns-over-https-rustls-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dns-over-https-rustls-devel

This package contains library source intended for building other packages which
use the "dns-over-https-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+dns-over-native-tls-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dns-over-native-tls-devel

This package contains library source intended for building other packages which
use the "dns-over-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+dns-over-openssl-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dns-over-openssl-devel

This package contains library source intended for building other packages which
use the "dns-over-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+dns-over-quic-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dns-over-quic-devel

This package contains library source intended for building other packages which
use the "dns-over-quic" feature of the "%{crate}" crate.

%package     -n %{name}+dns-over-rustls-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dns-over-rustls-devel

This package contains library source intended for building other packages which
use the "dns-over-rustls" feature of the "%{crate}" crate.

%package     -n %{name}+dns-over-tls-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dns-over-tls-devel

This package contains library source intended for building other packages which
use the "dns-over-tls" feature of the "%{crate}" crate.

%package     -n %{name}+dnssec-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dnssec-devel

This package contains library source intended for building other packages which
use the "dnssec" feature of the "%{crate}" crate.

%package     -n %{name}+dnssec-openssl-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dnssec-openssl-devel

This package contains library source intended for building other packages which
use the "dnssec-openssl" feature of the "%{crate}" crate.

%package     -n %{name}+dnssec-ring-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+dnssec-ring-devel

This package contains library source intended for building other packages which
use the "dnssec-ring" feature of the "%{crate}" crate.

%package     -n %{name}+mdns-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+mdns-devel

This package contains library source intended for building other packages which
use the "mdns" feature of the "%{crate}" crate.

%package     -n %{name}+native-certs-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+native-certs-devel

This package contains library source intended for building other packages which
use the "native-certs" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde-config-devel
Summary:        Hickory DNS is a safe and secure DNS library
BuildArch:      noarch
%description -n %{name}+serde-config-devel

This package contains library source intended for building other packages which
use the "serde-config" feature of the "%{crate}" crate.

%package     -n %{name}+webpki-roots-devel
Summary:        Hickory DNS is a safe and secure DNS library
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
%files -n rust-hickory-client0.24-devel -f %{oreon_filedir}/rust-hickory-client0.24-devel.list

%changelog

%autochangelog

%global source0_hash 1d9efca8738c78ee9484207732f728b1ef517bbb1833d6fc0879ca898a522f6f
%bcond check 0
%global debug_package %{nil}
%global crate spki
Name:           rust-spki0.8
Version:        0.8.0
Release:        1%{?dist}
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as wel...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/spki
Source0:        https://static.crates.io/crates/spki/spki-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as wel...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as wel...
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as wel...
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+base64ct-devel
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as wel...
BuildArch:      noarch
%description -n %{name}+base64ct-devel

This package contains library source intended for building other packages which
use the "base64ct" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as wel...
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+fingerprint-devel
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as wel...
BuildArch:      noarch
%description -n %{name}+fingerprint-devel

This package contains library source intended for building other packages which
use the "fingerprint" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as wel...
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as wel...
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        X.509 Subject Public Key Info (RFC5280) describing public keys as wel...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-spki0.8-devel -f %{oreon_filedir}/rust-spki0.8-devel.list

%changelog

%autochangelog

%global source0_hash 83be360ca0cc8659abfbda932098e606fe52fa129508b92f0ce2998c00679170
%bcond check 1
%global debug_package %{nil}
%global crate picky
%global crate_version 7.0.0-rc.15
Name:           rust-picky
Version:        7.0.0~rc.15
Release:        1%{?dist}
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/picky
Source0:        https://crates.io/api/v1/crates/%{crate}/%{crate_version}/download#/%{crate}-%{crate_version}.crate
Patch:          picky-fix-metadata.diff
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
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+chrono_conversion-devel
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
BuildArch:      noarch
%description -n %{name}+chrono_conversion-devel

This package contains library source intended for building other packages which
use the "chrono_conversion" feature of the "%{crate}" crate.

%package     -n %{name}+http_signature-devel
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
BuildArch:      noarch
%description -n %{name}+http_signature-devel

This package contains library source intended for building other packages which
use the "http_signature" feature of the "%{crate}" crate.

%package     -n %{name}+http_timestamp-devel
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
BuildArch:      noarch
%description -n %{name}+http_timestamp-devel

This package contains library source intended for building other packages which
use the "http_timestamp" feature of the "%{crate}" crate.

%package     -n %{name}+http_trait_impl-devel
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
BuildArch:      noarch
%description -n %{name}+http_trait_impl-devel

This package contains library source intended for building other packages which
use the "http_trait_impl" feature of the "%{crate}" crate.

%package     -n %{name}+jose-devel
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
BuildArch:      noarch
%description -n %{name}+jose-devel

This package contains library source intended for building other packages which
use the "jose" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs12-devel
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
BuildArch:      noarch
%description -n %{name}+pkcs12-devel

This package contains library source intended for building other packages which
use the "pkcs12" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs7-devel
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
BuildArch:      noarch
%description -n %{name}+pkcs7-devel

This package contains library source intended for building other packages which
use the "pkcs7" feature of the "%{crate}" crate.

%package     -n %{name}+time_conversion-devel
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
BuildArch:      noarch
%description -n %{name}+time_conversion-devel

This package contains library source intended for building other packages which
use the "time_conversion" feature of the "%{crate}" crate.

%package     -n %{name}+wincert-devel
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
BuildArch:      noarch
%description -n %{name}+wincert-devel

This package contains library source intended for building other packages which
use the "wincert" feature of the "%{crate}" crate.

%package     -n %{name}+x509-devel
Summary:        Portable X.509, PKI, JOSE and HTTP signature implementation
BuildArch:      noarch
%description -n %{name}+x509-devel

This package contains library source intended for building other packages which
use the "x509" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{crate_version} -p1
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
%files -n rust-picky-devel -f %{oreon_filedir}/rust-picky-devel.list

%changelog

%autochangelog

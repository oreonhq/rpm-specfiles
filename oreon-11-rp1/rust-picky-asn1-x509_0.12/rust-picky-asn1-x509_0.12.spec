%global source0_hash 2c5f20f71a68499ff32310f418a6fad8816eac1a2859ed3f0c5c741389dd6208
%bcond check 0
%global debug_package %{nil}
%global crate picky-asn1-x509
Name:           rust-picky-asn1-x509_0.12
Version:        0.12.0
Release:        1%{?dist}
Summary:        ASN1 types defined by X.509 related RFCs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/picky-asn1-x509
Source0:        https://static.crates.io/crates/picky-asn1-x509/picky-asn1-x509-%{version}.crate
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
Summary:        ASN1 types defined by X.509 related RFCs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ctl-devel
Summary:        ASN1 types defined by X.509 related RFCs
BuildArch:      noarch
%description -n %{name}+ctl-devel

This package contains library source intended for building other packages which
use the "ctl" feature of the "%{crate}" crate.

%package     -n %{name}+legacy-devel
Summary:        ASN1 types defined by X.509 related RFCs
BuildArch:      noarch
%description -n %{name}+legacy-devel

This package contains library source intended for building other packages which
use the "legacy" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-dig-devel
Summary:        ASN1 types defined by X.509 related RFCs
BuildArch:      noarch
%description -n %{name}+num-bigint-dig-devel

This package contains library source intended for building other packages which
use the "num-bigint-dig" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs12-devel
Summary:        ASN1 types defined by X.509 related RFCs
BuildArch:      noarch
%description -n %{name}+pkcs12-devel

This package contains library source intended for building other packages which
use the "pkcs12" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs7-devel
Summary:        ASN1 types defined by X.509 related RFCs
BuildArch:      noarch
%description -n %{name}+pkcs7-devel

This package contains library source intended for building other packages which
use the "pkcs7" feature of the "%{crate}" crate.

%package     -n %{name}+widestring-devel
Summary:        ASN1 types defined by X.509 related RFCs
BuildArch:      noarch
%description -n %{name}+widestring-devel

This package contains library source intended for building other packages which
use the "widestring" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        ASN1 types defined by X.509 related RFCs
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-picky-asn1-x509_0.12-devel -f %{oreon_filedir}/rust-picky-asn1-x509_0.12-devel.list

%changelog

%autochangelog

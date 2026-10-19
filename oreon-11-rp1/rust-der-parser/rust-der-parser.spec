%global source0_hash 07da5016415d5a3c4dd39b11ed26f915f52fc4e0dc197d87908bc916e51bc1a6
%bcond check 0
%global debug_package %{nil}
%global crate der-parser
Name:           rust-der-parser
Version:        10.0.0
Release:        1%{?dist}
Summary:        Parser/encoder for ASN.1 BER/DER data
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/der-parser
Source0:        https://static.crates.io/crates/der-parser/der-parser-%{version}.crate
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
Summary:        Parser/encoder for ASN.1 BER/DER data
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bigint-devel
Summary:        Parser/encoder for ASN.1 BER/DER data
BuildArch:      noarch
%description -n %{name}+bigint-devel

This package contains library source intended for building other packages which
use the "bigint" feature of the "%{crate}" crate.

%package     -n %{name}+cookie-factory-devel
Summary:        Parser/encoder for ASN.1 BER/DER data
BuildArch:      noarch
%description -n %{name}+cookie-factory-devel

This package contains library source intended for building other packages which
use the "cookie-factory" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        Parser/encoder for ASN.1 BER/DER data
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%package     -n %{name}+serialize-devel
Summary:        Parser/encoder for ASN.1 BER/DER data
BuildArch:      noarch
%description -n %{name}+serialize-devel

This package contains library source intended for building other packages which
use the "serialize" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Parser/encoder for ASN.1 BER/DER data
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+unstable-devel
Summary:        Parser/encoder for ASN.1 BER/DER data
BuildArch:      noarch
%description -n %{name}+unstable-devel

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

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
%files -n rust-der-parser-devel -f %{oreon_filedir}/rust-der-parser-devel.list

%changelog

%autochangelog

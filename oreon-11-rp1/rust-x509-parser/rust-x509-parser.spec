%global source0_hash 9fb9bace5b5589ffead1afb76e43e34cff39cd0f3ce7e170ae0c29e53b88eb1c
%bcond check 0
%global debug_package %{nil}
%global crate x509-parser
Name:           rust-x509-parser
Version:        0.13.2
Release:        1%{?dist}
Summary:        Parser for the X.509 v3 format (RFC 5280 certificates)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/x509-parser
Source0:        https://static.crates.io/crates/x509-parser/x509-parser-%{version}.crate
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
Summary:        Parser for the X.509 v3 format (RFC 5280 certificates)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+ring-devel
Summary:        Parser for the X.509 v3 format (RFC 5280 certificates)
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%package     -n %{name}+validate-devel
Summary:        Parser for the X.509 v3 format (RFC 5280 certificates)
BuildArch:      noarch
%description -n %{name}+validate-devel

This package contains library source intended for building other packages which
use the "validate" feature of the "%{crate}" crate.

%package     -n %{name}+verify-devel
Summary:        Parser for the X.509 v3 format (RFC 5280 certificates)
BuildArch:      noarch
%description -n %{name}+verify-devel

This package contains library source intended for building other packages which
use the "verify" feature of the "%{crate}" crate.

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
%files -n rust-x509-parser-devel -f %{oreon_filedir}/rust-x509-parser-devel.list

%changelog

%autochangelog

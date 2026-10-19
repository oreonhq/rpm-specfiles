%global source0_hash 38e20717fa0541f39bd146692035c37bedfa532b3e5071b35761082407546b2a
%bcond check 0
%global debug_package %{nil}
%global crate oid-registry
Name:           rust-oid-registry
Version:        0.4.0
Release:        1%{?dist}
Summary:        Object Identifier (OID) database
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/oid-registry
Source0:        https://static.crates.io/crates/oid-registry/oid-registry-%{version}.crate
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
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-devel
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+crypto-devel

This package contains library source intended for building other packages which
use the "crypto" feature of the "%{crate}" crate.

%package     -n %{name}+kdf-devel
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+kdf-devel

This package contains library source intended for building other packages which
use the "kdf" feature of the "%{crate}" crate.

%package     -n %{name}+ms_spc-devel
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+ms_spc-devel

This package contains library source intended for building other packages which
use the "ms_spc" feature of the "%{crate}" crate.

%package     -n %{name}+nist_algs-devel
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+nist_algs-devel

This package contains library source intended for building other packages which
use the "nist_algs" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs1-devel
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+pkcs1-devel

This package contains library source intended for building other packages which
use the "pkcs1" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs12-devel
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+pkcs12-devel

This package contains library source intended for building other packages which
use the "pkcs12" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs7-devel
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+pkcs7-devel

This package contains library source intended for building other packages which
use the "pkcs7" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs9-devel
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+pkcs9-devel

This package contains library source intended for building other packages which
use the "pkcs9" feature of the "%{crate}" crate.

%package     -n %{name}+registry-devel
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+registry-devel

This package contains library source intended for building other packages which
use the "registry" feature of the "%{crate}" crate.

%package     -n %{name}+x509-devel
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+x509-devel

This package contains library source intended for building other packages which
use the "x509" feature of the "%{crate}" crate.

%package     -n %{name}+x962-devel
Summary:        Object Identifier (OID) database
BuildArch:      noarch
%description -n %{name}+x962-devel

This package contains library source intended for building other packages which
use the "x962" feature of the "%{crate}" crate.

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
%files -n rust-oid-registry-devel -f %{oreon_filedir}/rust-oid-registry-devel.list

%changelog

%autochangelog

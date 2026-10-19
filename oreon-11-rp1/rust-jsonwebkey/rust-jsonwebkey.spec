%global source0_hash c57c852b14147e2bd58c14fde40398864453403ef632b1101db130282ee6e2cc
%bcond check 1
%global debug_package %{nil}
%global crate jsonwebkey
Name:           rust-jsonwebkey
Version:        0.3.5
Release:        1%{?dist}
Summary:        JSON Web Key (JWK) (de)serialization, generation, and conversion
License:        MIT
URL:            https://crates.io/crates/jsonwebkey
Source0:        https://static.crates.io/crates/jsonwebkey/jsonwebkey-%{version}.crate
Patch:          jsonwebkey-fix-metadata.diff
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
Summary:        JSON Web Key (JWK) (de)serialization, generation, and conversion
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        JSON Web Key (JWK) (de)serialization, generation, and conversion
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs-convert-devel
Summary:        JSON Web Key (JWK) (de)serialization, generation, and conversion
BuildArch:      noarch
%description -n %{name}+pkcs-convert-devel

This package contains library source intended for building other packages which
use the "pkcs-convert" feature of the "%{crate}" crate.

%package     -n %{name}+yasna-devel
Summary:        JSON Web Key (JWK) (de)serialization, generation, and conversion
BuildArch:      noarch
%description -n %{name}+yasna-devel

This package contains library source intended for building other packages which
use the "yasna" feature of the "%{crate}" crate.

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
%files -n rust-jsonwebkey-devel -f %{oreon_filedir}/rust-jsonwebkey-devel.list

%changelog

%autochangelog

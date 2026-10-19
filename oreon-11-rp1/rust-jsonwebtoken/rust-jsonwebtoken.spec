%global source0_hash 5a87cc7a48537badeae96744432de36f4be2b4a34a05a5ef32e9dd8a1c169dde
%bcond check 1
%global debug_package %{nil}
%global crate jsonwebtoken
Name:           rust-jsonwebtoken
Version:        9.3.1
Release:        1%{?dist}
Summary:        Create and decode JWTs in a strongly typed way
License:        MIT
URL:            https://crates.io/crates/jsonwebtoken
Source0:        https://static.crates.io/crates/jsonwebtoken/jsonwebtoken-%{version}.crate
Patch:          jsonwebtoken-fix-metadata-auto.diff
Patch:          jsonwebtoken-fix-metadata.diff
Patch10:        0001-Fix-type-confusion.patch
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
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+simple_asn1-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+simple_asn1-devel

This package contains library source intended for building other packages which
use the "simple_asn1" feature of the "%{crate}" crate.

%package     -n %{name}+use_pem-devel
Summary:        Create and decode JWTs in a strongly typed way
BuildArch:      noarch
%description -n %{name}+use_pem-devel

This package contains library source intended for building other packages which
use the "use_pem" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
grep -lr wasm_bindgen_test | xargs sed -i /wasm_bindgen_test/d
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
%files -n rust-jsonwebtoken-devel -f %{oreon_filedir}/rust-jsonwebtoken-devel.list

%changelog

%autochangelog

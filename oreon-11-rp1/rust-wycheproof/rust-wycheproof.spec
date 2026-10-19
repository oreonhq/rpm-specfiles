%global source0_hash efb3be19abfb206c6adcbdf2007b09b0e8ca1f6530db40c03b42ce8ed4719894
%bcond check 1
%global debug_package %{nil}
%global crate wycheproof
Name:           rust-wycheproof
Version:        0.6.0
Release:        1%{?dist}
Summary:        Wycheproof test vectors
License:        Apache-2.0
URL:            https://crates.io/crates/wycheproof
Source0:        https://static.crates.io/crates/wycheproof/wycheproof-%{version}.crate
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
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aead-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+aead-devel

This package contains library source intended for building other packages which
use the "aead" feature of the "%{crate}" crate.

%package     -n %{name}+cipher-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+cipher-devel

This package contains library source intended for building other packages which
use the "cipher" feature of the "%{crate}" crate.

%package     -n %{name}+dsa-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+dsa-devel

This package contains library source intended for building other packages which
use the "dsa" feature of the "%{crate}" crate.

%package     -n %{name}+ec-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+ec-devel

This package contains library source intended for building other packages which
use the "ec" feature of the "%{crate}" crate.

%package     -n %{name}+ecdh-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+ecdh-devel

This package contains library source intended for building other packages which
use the "ecdh" feature of the "%{crate}" crate.

%package     -n %{name}+ecdsa-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+ecdsa-devel

This package contains library source intended for building other packages which
use the "ecdsa" feature of the "%{crate}" crate.

%package     -n %{name}+eddsa-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+eddsa-devel

This package contains library source intended for building other packages which
use the "eddsa" feature of the "%{crate}" crate.

%package     -n %{name}+fpe-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+fpe-devel

This package contains library source intended for building other packages which
use the "fpe" feature of the "%{crate}" crate.

%package     -n %{name}+hkdf-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+hkdf-devel

This package contains library source intended for building other packages which
use the "hkdf" feature of the "%{crate}" crate.

%package     -n %{name}+keywrap-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+keywrap-devel

This package contains library source intended for building other packages which
use the "keywrap" feature of the "%{crate}" crate.

%package     -n %{name}+mac-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+mac-devel

This package contains library source intended for building other packages which
use the "mac" feature of the "%{crate}" crate.

%package     -n %{name}+num-bigint-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+num-bigint-devel

This package contains library source intended for building other packages which
use the "num-bigint" feature of the "%{crate}" crate.

%package     -n %{name}+primality-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+primality-devel

This package contains library source intended for building other packages which
use the "primality" feature of the "%{crate}" crate.

%package     -n %{name}+rsa_enc-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+rsa_enc-devel

This package contains library source intended for building other packages which
use the "rsa_enc" feature of the "%{crate}" crate.

%package     -n %{name}+rsa_sig-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+rsa_sig-devel

This package contains library source intended for building other packages which
use the "rsa_sig" feature of the "%{crate}" crate.

%package     -n %{name}+xdh-devel
Summary:        Wycheproof test vectors
BuildArch:      noarch
%description -n %{name}+xdh-devel

This package contains library source intended for building other packages which
use the "xdh" feature of the "%{crate}" crate.

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
%files -n rust-wycheproof-devel -f %{oreon_filedir}/rust-wycheproof-devel.list

%changelog

%autochangelog

%global source0_hash 8f34df8ca6a2920b0fae969ced913c714b41f23b655a434a45c6a9843a75c019
%bcond check 0
%global debug_package %{nil}
%global crate ossl
Name:           rust-ossl
Version:        1.5.2
Release:        1%{?dist}
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
License:        Apache-2.0
URL:            https://crates.io/crates/ossl
Source0:        https://static.crates.io/crates/ossl/ossl-%{version}.crate
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
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dynamic-devel
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
BuildArch:      noarch
%description -n %{name}+dynamic-devel

This package contains library source intended for building other packages which
use the "dynamic" feature of the "%{crate}" crate.

%package     -n %{name}+fips-devel
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
BuildArch:      noarch
%description -n %{name}+fips-devel

This package contains library source intended for building other packages which
use the "fips" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-sys-devel
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
BuildArch:      noarch
%description -n %{name}+openssl-sys-devel

This package contains library source intended for building other packages which
use the "openssl-sys" feature of the "%{crate}" crate.

%package     -n %{name}+ossl-sys-devel
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
BuildArch:      noarch
%description -n %{name}+ossl-sys-devel

This package contains library source intended for building other packages which
use the "ossl-sys" feature of the "%{crate}" crate.

%package     -n %{name}+ossl320-devel
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
BuildArch:      noarch
%description -n %{name}+ossl320-devel

This package contains library source intended for building other packages which
use the "ossl320" feature of the "%{crate}" crate.

%package     -n %{name}+ossl350-devel
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
BuildArch:      noarch
%description -n %{name}+ossl350-devel

This package contains library source intended for building other packages which
use the "ossl350" feature of the "%{crate}" crate.

%package     -n %{name}+ossl400-devel
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
BuildArch:      noarch
%description -n %{name}+ossl400-devel

This package contains library source intended for building other packages which
use the "ossl400" feature of the "%{crate}" crate.

%package     -n %{name}+rfc9580-devel
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
BuildArch:      noarch
%description -n %{name}+rfc9580-devel

This package contains library source intended for building other packages which
use the "rfc9580" feature of the "%{crate}" crate.

%package     -n %{name}+vsprintf-devel
Summary:        OpenSSL version 3+ bindings to modern EVP APIs
BuildArch:      noarch
%description -n %{name}+vsprintf-devel

This package contains library source intended for building other packages which
use the "vsprintf" feature of the "%{crate}" crate.

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
%files -n rust-ossl-devel -f %{oreon_filedir}/rust-ossl-devel.list

%changelog

%autochangelog

%global source0_hash 77823a27f0babb03091cb9ed9ef80af3b39dbc82f97e8fa530374b7dafd87a45
%bcond check 0
%global debug_package %{nil}
%global crate openssl
Name:           rust-openssl
Version:        0.10.81
Release:        1%{?dist}
Summary:        OpenSSL bindings
License:        Apache-2.0
URL:            https://crates.io/crates/openssl
Source0:        https://static.crates.io/crates/openssl/openssl-%{version}.crate
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
Summary:        OpenSSL bindings
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-devel
Summary:        OpenSSL bindings
BuildArch:      noarch
%description -n %{name}+aws-lc-devel

This package contains library source intended for building other packages which
use the "aws-lc" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-fips-devel
Summary:        OpenSSL bindings
BuildArch:      noarch
%description -n %{name}+aws-lc-fips-devel

This package contains library source intended for building other packages which
use the "aws-lc-fips" feature of the "%{crate}" crate.

%package     -n %{name}+bindgen-devel
Summary:        OpenSSL bindings
BuildArch:      noarch
%description -n %{name}+bindgen-devel

This package contains library source intended for building other packages which
use the "bindgen" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_boringssl-devel
Summary:        OpenSSL bindings
BuildArch:      noarch
%description -n %{name}+unstable_boringssl-devel

This package contains library source intended for building other packages which
use the "unstable_boringssl" feature of the "%{crate}" crate.

%package     -n %{name}+v101-devel
Summary:        OpenSSL bindings
BuildArch:      noarch
%description -n %{name}+v101-devel

This package contains library source intended for building other packages which
use the "v101" feature of the "%{crate}" crate.

%package     -n %{name}+v102-devel
Summary:        OpenSSL bindings
BuildArch:      noarch
%description -n %{name}+v102-devel

This package contains library source intended for building other packages which
use the "v102" feature of the "%{crate}" crate.

%package     -n %{name}+v110-devel
Summary:        OpenSSL bindings
BuildArch:      noarch
%description -n %{name}+v110-devel

This package contains library source intended for building other packages which
use the "v110" feature of the "%{crate}" crate.

%package     -n %{name}+v111-devel
Summary:        OpenSSL bindings
BuildArch:      noarch
%description -n %{name}+v111-devel

This package contains library source intended for building other packages which
use the "v111" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-devel
Summary:        OpenSSL bindings
BuildArch:      noarch
%description -n %{name}+vendored-devel

This package contains library source intended for building other packages which
use the "vendored" feature of the "%{crate}" crate.

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
%files -n rust-openssl-devel -f %{oreon_filedir}/rust-openssl-devel.list

%changelog

%autochangelog

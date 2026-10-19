%global source0_hash 15b2c103cf610ec6cae3da84a766285b42fd16aad564758459e6ecf128c75206
%bcond check 1
%global debug_package %{nil}
%global crate cookie_store
Name:           rust-cookie_store
Version:        0.22.1
Release:        1%{?dist}
Summary:        Implementation of Cookie storage and retrieval
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cookie_store
Source0:        https://static.crates.io/crates/cookie_store/cookie_store-%{version}.crate
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
Summary:        Implementation of Cookie storage and retrieval
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+log_secure_cookie_values-devel
Summary:        Implementation of Cookie storage and retrieval
BuildArch:      noarch
%description -n %{name}+log_secure_cookie_values-devel

This package contains library source intended for building other packages which
use the "log_secure_cookie_values" feature of the "%{crate}" crate.

%package     -n %{name}+preserve_order-devel
Summary:        Implementation of Cookie storage and retrieval
BuildArch:      noarch
%description -n %{name}+preserve_order-devel

This package contains library source intended for building other packages which
use the "preserve_order" feature of the "%{crate}" crate.

%package     -n %{name}+public_suffix-devel
Summary:        Implementation of Cookie storage and retrieval
BuildArch:      noarch
%description -n %{name}+public_suffix-devel

This package contains library source intended for building other packages which
use the "public_suffix" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Implementation of Cookie storage and retrieval
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_json-devel
Summary:        Implementation of Cookie storage and retrieval
BuildArch:      noarch
%description -n %{name}+serde_json-devel

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

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
%files -n rust-cookie_store-devel -f %{oreon_filedir}/rust-cookie_store-devel.list

%changelog

%autochangelog

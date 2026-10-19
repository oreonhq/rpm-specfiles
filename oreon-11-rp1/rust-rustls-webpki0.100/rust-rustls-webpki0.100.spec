%global source0_hash 5f6a5fc258f1c1276dfe3016516945546e2d5383911efc0fc4f1cdc5df3a4ae3
%bcond check 0
%global debug_package %{nil}
%global crate rustls-webpki
Name:           rust-rustls-webpki0.100
Version:        0.100.3
Release:        1%{?dist}
Summary:        Web PKI X.509 Certificate Verification.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustls-webpki
Source0:        https://static.crates.io/crates/rustls-webpki/rustls-webpki-%{version}.crate
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
Summary:        Web PKI X.509 Certificate Verification.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Web PKI X.509 Certificate Verification.
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Web PKI X.509 Certificate Verification.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-rustls-webpki0.100-devel -f %{oreon_filedir}/rust-rustls-webpki0.100-devel.list

%changelog

%autochangelog

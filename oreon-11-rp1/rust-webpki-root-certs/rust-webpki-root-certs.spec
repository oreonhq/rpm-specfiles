%global source0_hash 804f18a4ac2676ffb4e8b5b5fa9ae38af06df08162314f96a68d2a363e21a8ca
%bcond check 1
%global debug_package %{nil}
%global crate webpki-root-certs
Name:           rust-webpki-root-certs
Version:        1.0.6
Release:        1%{?dist}
Summary:        Mozilla trusted certificate authorities in self-signed X.509 format
License:        CDLA-Permissive-2.0
URL:            https://crates.io/crates/webpki-root-certs
Source0:        https://static.crates.io/crates/webpki-root-certs/webpki-root-certs-%{version}.crate
Patch:          webpki-root-certs-fix-metadata.diff
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
Summary:        Mozilla trusted certificate authorities in self-signed X.509 format
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-webpki-root-certs-devel -f %{oreon_filedir}/rust-webpki-root-certs-devel.list

%changelog

%autochangelog

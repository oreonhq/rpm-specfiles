%global source0_hash b8e38c0608262c46d4a56202ebabdeb094cef7e560ca7a226c6bf055188aa4ea
%bcond check 0
%global debug_package %{nil}
%global crate webpki
Name:           rust-webpki
Version:        0.21.4
Release:        1%{?dist}
Summary:        Web PKI X.509 Certificate Verification.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/webpki
Source0:        https://static.crates.io/crates/webpki/webpki-%{version}.crate
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

%package     -n %{name}+std-devel
Summary:        Web PKI X.509 Certificate Verification.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+trust_anchor_util-devel
Summary:        Web PKI X.509 Certificate Verification.
BuildArch:      noarch
%description -n %{name}+trust_anchor_util-devel

This package contains library source intended for building other packages which
use the "trust_anchor_util" feature of the "%{crate}" crate.

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
%files -n rust-webpki-devel -f %{oreon_filedir}/rust-webpki-devel.list

%changelog

%autochangelog

%global source0_hash f3c3cf1d8b1e7d4927e2d154c3fcb02979afb9939629c62cd9048d4f07b60ac2
%bcond check 0
%global debug_package %{nil}
%global crate rustls-webpki
Name:           rust-rustls-webpki
Version:        0.103.15
Release:        1%{?dist}
Summary:        Web PKI X.509 Certificate Verification
License:        ISC
URL:            https://crates.io/crates/rustls-webpki
Source0:        https://static.crates.io/crates/rustls-webpki/rustls-webpki-%{version}.crate
Patch:          rustls-webpki-fix-metadata.diff
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
Summary:        Web PKI X.509 Certificate Verification
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Web PKI X.509 Certificate Verification
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+ring-devel
Summary:        Web PKI X.509 Certificate Verification
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Web PKI X.509 Certificate Verification
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
%files -n rust-rustls-webpki-devel -f %{oreon_filedir}/rust-rustls-webpki-devel.list

%changelog

%autochangelog

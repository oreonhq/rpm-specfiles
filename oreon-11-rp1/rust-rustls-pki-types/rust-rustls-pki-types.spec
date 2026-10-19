%global source0_hash 2f4925028c7eb5d1fcdaf196971378ed9d2c1c4efc7dc5d011256f76c99c0a96
%bcond check 0
%global debug_package %{nil}
%global crate rustls-pki-types
Name:           rust-rustls-pki-types
Version:        1.15.1
Release:        1%{?dist}
Summary:        Shared types for the rustls PKI ecosystem
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustls-pki-types
Source0:        https://static.crates.io/crates/rustls-pki-types/rustls-pki-types-%{version}.crate
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
Summary:        Shared types for the rustls PKI ecosystem
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Shared types for the rustls PKI ecosystem
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Shared types for the rustls PKI ecosystem
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+web-devel
Summary:        Shared types for the rustls PKI ecosystem
BuildArch:      noarch
%description -n %{name}+web-devel

This package contains library source intended for building other packages which
use the "web" feature of the "%{crate}" crate.

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
%files -n rust-rustls-pki-types-devel -f %{oreon_filedir}/rust-rustls-pki-types-devel.list

%changelog

%autochangelog

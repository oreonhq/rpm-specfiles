%global source0_hash a6305423e0e7738146434843d1694d621cce767262b2a86910beab705e4493d9
%bcond check 0
%global debug_package %{nil}
%global crate pem-rfc7468
Name:           rust-pem-rfc74681
Version:        1.0.0
Release:        1%{?dist}
Summary:        PEM Encoding (RFC 7468) for PKIX, PKCS, and CMS Structures, implement...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/pem-rfc7468
Source0:        https://static.crates.io/crates/pem-rfc7468/pem-rfc7468-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        PEM Encoding (RFC 7468) for PKIX, PKCS, and CMS Structures, implement...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        PEM Encoding (RFC 7468) for PKIX, PKCS, and CMS Structures, implement...
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
%files -n rust-pem-rfc74681-devel -f %{oreon_filedir}/rust-pem-rfc74681-devel.list

%changelog

%autochangelog

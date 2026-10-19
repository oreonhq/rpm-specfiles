%global source0_hash b47e7e6bb2c38cd930d25a23b40fa52e068c10e85f3e03a7f5ba5aaca5713695
%bcond check 0
%global debug_package %{nil}
%global crate openssl-sys
Name:           rust-openssl-sys
Version:        0.9.117
Release:        2%{?dist}
Summary:        FFI bindings to OpenSSL
License:        MIT
URL:            https://crates.io/crates/openssl-sys
Source0:        https://static.crates.io/crates/openssl-sys/openssl-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  openssl-devel
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
Summary:        FFI bindings to OpenSSL
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-devel
Summary:        FFI bindings to OpenSSL
BuildArch:      noarch
%description -n %{name}+aws-lc-devel

This package contains library source intended for building other packages which
use the "aws-lc" feature of the "%{crate}" crate.

%package     -n %{name}+aws-lc-fips-devel
Summary:        FFI bindings to OpenSSL
BuildArch:      noarch
%description -n %{name}+aws-lc-fips-devel

This package contains library source intended for building other packages which
use the "aws-lc-fips" feature of the "%{crate}" crate.

%package     -n %{name}+bssl-sys-devel
Summary:        FFI bindings to OpenSSL
BuildArch:      noarch
%description -n %{name}+bssl-sys-devel

This package contains library source intended for building other packages which
use the "bssl-sys" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_boringssl-devel
Summary:        FFI bindings to OpenSSL
BuildArch:      noarch
%description -n %{name}+unstable_boringssl-devel

This package contains library source intended for building other packages which
use the "unstable_boringssl" feature of the "%{crate}" crate.

%package     -n %{name}+vendored-devel
Summary:        FFI bindings to OpenSSL
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
%files -n rust-openssl-sys-devel -f %{oreon_filedir}/rust-openssl-sys-devel.list

%changelog

%autochangelog

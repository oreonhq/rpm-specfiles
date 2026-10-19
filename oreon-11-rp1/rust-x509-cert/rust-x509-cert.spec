%global source0_hash 105ef4642d9cb137ef83d623d0e4bf08b8adf69e9918ca904a174adb6d3d038b
%bcond check 0
%global debug_package %{nil}
%global crate x509-cert
Name:           rust-x509-cert
Version:        0.3.0
Release:        1%{?dist}
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certi...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/x509-cert
Source0:        https://static.crates.io/crates/x509-cert/x509-cert-%{version}.crate
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
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certi...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certi...
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%package     -n %{name}+builder-devel
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certi...
BuildArch:      noarch
%description -n %{name}+builder-devel

This package contains library source intended for building other packages which
use the "builder" feature of the "%{crate}" crate.

%package     -n %{name}+hazmat-devel
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certi...
BuildArch:      noarch
%description -n %{name}+hazmat-devel

This package contains library source intended for building other packages which
use the "hazmat" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certi...
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+sct-devel
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certi...
BuildArch:      noarch
%description -n %{name}+sct-devel

This package contains library source intended for building other packages which
use the "sct" feature of the "%{crate}" crate.

%package     -n %{name}+sha1-devel
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certi...
BuildArch:      noarch
%description -n %{name}+sha1-devel

This package contains library source intended for building other packages which
use the "sha1" feature of the "%{crate}" crate.

%package     -n %{name}+signature-devel
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certi...
BuildArch:      noarch
%description -n %{name}+signature-devel

This package contains library source intended for building other packages which
use the "signature" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certi...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+tls_codec-devel
Summary:        Pure Rust implementation of the X.509 Public Key Infrastructure Certi...
BuildArch:      noarch
%description -n %{name}+tls_codec-devel

This package contains library source intended for building other packages which
use the "tls_codec" feature of the "%{crate}" crate.

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
%files -n rust-x509-cert-devel -f %{oreon_filedir}/rust-x509-cert-devel.list

%changelog

%autochangelog

%global source0_hash 5fae430c6b28f1ad601274e78b7dffa0546de0b73b4cd32f46723c0c2a16f7a5
%bcond check 1
%global debug_package %{nil}
%global crate rcgen
Name:           rust-rcgen
Version:        0.14.5
Release:        1%{?dist}
Summary:        Rust X.509 certificate generator
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rcgen
Source0:        https://static.crates.io/crates/rcgen/rcgen-%{version}.crate
Patch:          rcgen-fix-metadata.diff
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
Summary:        Rust X.509 certificate generator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+crypto-devel
Summary:        Rust X.509 certificate generator
BuildArch:      noarch
%description -n %{name}+crypto-devel

This package contains library source intended for building other packages which
use the "crypto" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Rust X.509 certificate generator
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+ring-devel
Summary:        Rust X.509 certificate generator
BuildArch:      noarch
%description -n %{name}+ring-devel

This package contains library source intended for building other packages which
use the "ring" feature of the "%{crate}" crate.

%package     -n %{name}+x509-parser-devel
Summary:        Rust X.509 certificate generator
BuildArch:      noarch
%description -n %{name}+x509-parser-devel

This package contains library source intended for building other packages which
use the "x509-parser" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Rust X.509 certificate generator
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f x509-parser
%install
%cargo_install -f x509-parser
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f x509-parser
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rcgen-devel -f %{oreon_filedir}/rust-rcgen-devel.list

%changelog

%autochangelog

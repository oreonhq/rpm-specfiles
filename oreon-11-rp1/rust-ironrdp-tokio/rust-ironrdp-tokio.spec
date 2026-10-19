%global source0_hash 6a5815ae4dd7866a6730efb653281406a77fd1f5426d77dd959fc04e3512410f
%bcond check 1
%global debug_package %{nil}
%global crate ironrdp-tokio
Name:           rust-ironrdp-tokio
Version:        0.6.0
Release:        1%{?dist}
Summary:        Framed* traits implementation above Tokio’s traits
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp-tokio
Source0:        https://static.crates.io/crates/ironrdp-tokio/ironrdp-tokio-%{version}.crate
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
Summary:        Framed* traits implementation above Tokio’s traits
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+reqwest-devel
Summary:        Framed* traits implementation above Tokio’s traits
BuildArch:      noarch
%description -n %{name}+reqwest-devel

This package contains library source intended for building other packages which
use the "reqwest" feature of the "%{crate}" crate.

%package     -n %{name}+reqwest-native-tls-devel
Summary:        Framed* traits implementation above Tokio’s traits
BuildArch:      noarch
%description -n %{name}+reqwest-native-tls-devel

This package contains library source intended for building other packages which
use the "reqwest-native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+reqwest-rustls-ring-devel
Summary:        Framed* traits implementation above Tokio’s traits
BuildArch:      noarch
%description -n %{name}+reqwest-rustls-ring-devel

This package contains library source intended for building other packages which
use the "reqwest-rustls-ring" feature of the "%{crate}" crate.

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
%files -n rust-ironrdp-tokio-devel -f %{oreon_filedir}/rust-ironrdp-tokio-devel.list

%changelog

%autochangelog

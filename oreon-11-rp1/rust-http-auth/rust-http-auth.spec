%global source0_hash 150fa4a9462ef926824cf4519c84ed652ca8f4fbae34cb8af045b5cbcaf98822
%bcond check 0
%global debug_package %{nil}
%global crate http-auth
Name:           rust-http-auth
Version:        0.1.10
Release:        1%{?dist}
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/http-auth
Source0:        https://static.crates.io/crates/http-auth/http-auth-%{version}.crate
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
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+base64-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+base64-devel

This package contains library source intended for building other packages which
use the "base64" feature of the "%{crate}" crate.

%package     -n %{name}+basic-scheme-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+basic-scheme-devel

This package contains library source intended for building other packages which
use the "basic-scheme" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+digest-scheme-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+digest-scheme-devel

This package contains library source intended for building other packages which
use the "digest-scheme" feature of the "%{crate}" crate.

%package     -n %{name}+hex-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+hex-devel

This package contains library source intended for building other packages which
use the "hex" feature of the "%{crate}" crate.

%package     -n %{name}+http-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+http-devel

This package contains library source intended for building other packages which
use the "http" feature of the "%{crate}" crate.

%package     -n %{name}+http10-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+http10-devel

This package contains library source intended for building other packages which
use the "http10" feature of the "%{crate}" crate.

%package     -n %{name}+log-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+log-devel

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%package     -n %{name}+md-5-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+md-5-devel

This package contains library source intended for building other packages which
use the "md-5" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+sha2-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+sha2-devel

This package contains library source intended for building other packages which
use the "sha2" feature of the "%{crate}" crate.

%package     -n %{name}+trace-devel
Summary:        HTTP authentication: parse challenge lists, respond to Basic and Dige...
BuildArch:      noarch
%description -n %{name}+trace-devel

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

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
%files -n rust-http-auth-devel -f %{oreon_filedir}/rust-http-auth-devel.list

%changelog

%autochangelog

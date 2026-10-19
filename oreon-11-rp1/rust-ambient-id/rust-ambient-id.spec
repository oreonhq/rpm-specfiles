%global source0_hash c1daa54020e05aa0b163ee10434fff35a0f18d28a1cafa142bd1290e1abe630e
%bcond check 1
%global debug_package %{nil}
%global crate ambient-id
Name:           rust-ambient-id
Version:        0.0.11
Release:        1%{?dist}
Summary:        Detects ambient OIDC credentials in a variety of environments
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ambient-id
Source0:        https://static.crates.io/crates/ambient-id/ambient-id-%{version}.crate
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
Summary:        Detects ambient OIDC credentials in a variety of environments
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+native-tls-devel
Summary:        Detects ambient OIDC credentials in a variety of environments
BuildArch:      noarch
%description -n %{name}+native-tls-devel

This package contains library source intended for building other packages which
use the "native-tls" feature of the "%{crate}" crate.

%package     -n %{name}+reqwest-middleware-devel
Summary:        Detects ambient OIDC credentials in a variety of environments
BuildArch:      noarch
%description -n %{name}+reqwest-middleware-devel

This package contains library source intended for building other packages which
use the "reqwest-middleware" feature of the "%{crate}" crate.

%package     -n %{name}+rustls-devel
Summary:        Detects ambient OIDC credentials in a variety of environments
BuildArch:      noarch
%description -n %{name}+rustls-devel

This package contains library source intended for building other packages which
use the "rustls" feature of the "%{crate}" crate.

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

export RUST_TEST_THREADS=1
%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-ambient-id-devel -f %{oreon_filedir}/rust-ambient-id-devel.list

%changelog

%autochangelog

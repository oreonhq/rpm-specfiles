%global source0_hash fe2412db2af7d2268e7a5406be0431f37d9eb67ff390f35b395716f5f06c2eaa
%bcond check 1
%global debug_package %{nil}
%global crate reqwest-retry
Name:           rust-reqwest-retry
Version:        0.9.1
Release:        1%{?dist}
Summary:        Retry middleware for reqwest
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/reqwest-retry
Source0:        https://static.crates.io/crates/reqwest-retry/reqwest-retry-%{version}.crate
Patch:          reqwest-retry-fix-metadata-auto.diff
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
Summary:        Retry middleware for reqwest
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Retry middleware for reqwest
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

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
%files -n rust-reqwest-retry-devel -f %{oreon_filedir}/rust-reqwest-retry-devel.list

%changelog

%autochangelog

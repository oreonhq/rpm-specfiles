%global source0_hash 48c76a42c052d7a95249b90b83d44e8f1bbde7c8e08dbed50d49c58321815da3
%bcond check 1
%global debug_package %{nil}
%global crate astral-reqwest-retry
Name:           rust-astral-reqwest-retry
Version:        0.9.1
Release:        1%{?dist}
Summary:        Retry middleware for reqwest
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/astral-reqwest-retry
Source0:        https://static.crates.io/crates/astral-reqwest-retry/astral-reqwest-retry-%{version}.crate
Patch:          astral-reqwest-retry-fix-metadata-auto.diff
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
%files -n rust-astral-reqwest-retry-devel -f %{oreon_filedir}/rust-astral-reqwest-retry-devel.list

%changelog

%autochangelog

%global source0_hash 1e0f050db9c44b97a94723127e6be766ac5c340c48f2c4bb3ffa11713744be59
%bcond check 1
%global debug_package %{nil}
%global crate ouroboros
Name:           rust-ouroboros
Version:        0.18.5
Release:        1%{?dist}
Summary:        Easy, safe self-referential struct generation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ouroboros
Source0:        https://static.crates.io/crates/ouroboros/ouroboros-%{version}.crate
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
Summary:        Easy, safe self-referential struct generation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Easy, safe self-referential struct generation
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
%files -n rust-ouroboros-devel -f %{oreon_filedir}/rust-ouroboros-devel.list

%changelog

%autochangelog

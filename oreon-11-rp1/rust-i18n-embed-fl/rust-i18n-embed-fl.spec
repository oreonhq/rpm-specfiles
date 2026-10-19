%global source0_hash 602e6bd30c3db2749e13e38b363a3d98d9d41de1d8de7a79c31bb69e45b47cda
%bcond check 1
%global debug_package %{nil}
%global crate i18n-embed-fl
Name:           rust-i18n-embed-fl
Version:        0.10.1
Release:        1%{?dist}
Summary:        Perform compile time checks when using i18n-embed with fluent
License:        MIT
URL:            https://crates.io/crates/i18n-embed-fl
Source0:        https://static.crates.io/crates/i18n-embed-fl/i18n-embed-fl-%{version}.crate
Patch:          i18n-embed-fl-fix-metadata.diff
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
Summary:        Perform compile time checks when using i18n-embed with fluent
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+dashmap-devel
Summary:        Perform compile time checks when using i18n-embed with fluent
BuildArch:      noarch
%description -n %{name}+dashmap-devel

This package contains library source intended for building other packages which
use the "dashmap" feature of the "%{crate}" crate.

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
%files -n rust-i18n-embed-fl-devel -f %{oreon_filedir}/rust-i18n-embed-fl-devel.list

%changelog

%autochangelog

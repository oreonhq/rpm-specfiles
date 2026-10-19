%global source0_hash 15c781ee0f64b928c2ddc6c371a9892337874959c4c7df914687273469152d63
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate nu-utils
Name:           rust-nu-utils
Version:        0.99.1
Release:        1%{?dist}
Summary:        Nushell utility functions
License:        MIT
URL:            https://crates.io/crates/nu-utils
Source0:        https://static.crates.io/crates/nu-utils/nu-utils-%{version}.crate
Patch:          nu-utils-fix-metadata-auto.diff
Patch:          nu-utils-fix-metadata.diff
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
Summary:        Nushell utility functions
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

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
%files -n rust-nu-utils-devel -f %{oreon_filedir}/rust-nu-utils-devel.list

%changelog

%autochangelog

%global source0_hash e0df0c7b9afa020673c0942ae257a938b257d79e6395d8f1b8b45898f3391c5e
%bcond check 0
%global crate hexyl
Name:           rust-hexyl
Version:        0.17.0
Release:        1%{?dist}
Summary:        Command-line hex viewer
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/hexyl
Source0:        https://static.crates.io/crates/hexyl/hexyl-%{version}.crate
Patch:          hexyl-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Command-line hex viewer
License:        Apache-2.0 AND ISC AND MIT AND Zlib AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
%description -n %{crate}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Command-line hex viewer
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
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n hexyl -f %{oreon_filedir}/hexyl.list
%files -n rust-hexyl-devel -f %{oreon_filedir}/rust-hexyl-devel.list

%changelog

%autochangelog

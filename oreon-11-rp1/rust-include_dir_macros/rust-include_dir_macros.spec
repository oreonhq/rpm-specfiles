%global source0_hash 7cab85a7ed0bd5f0e76d93846e0147172bed2e2d3f859bcc33a8d9699cad1a75
%bcond check 1
%global debug_package %{nil}
%global crate include_dir_macros
Name:           rust-include_dir_macros
Version:        0.7.4
Release:        1%{?dist}
Summary:        The procedural macro used by include_dir
License:        MIT
URL:            https://crates.io/crates/include_dir_macros
Source0:        https://static.crates.io/crates/include_dir_macros/include_dir_macros-%{version}.crate
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
Summary:        The procedural macro used by include_dir
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+metadata-devel
Summary:        The procedural macro used by include_dir
BuildArch:      noarch
%description -n %{name}+metadata-devel

This package contains library source intended for building other packages which
use the "metadata" feature of the "%{crate}" crate.

%package     -n %{name}+nightly-devel
Summary:        The procedural macro used by include_dir
BuildArch:      noarch
%description -n %{name}+nightly-devel

This package contains library source intended for building other packages which
use the "nightly" feature of the "%{crate}" crate.

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
%files -n rust-include_dir_macros-devel -f %{oreon_filedir}/rust-include_dir_macros-devel.list

%changelog

%autochangelog

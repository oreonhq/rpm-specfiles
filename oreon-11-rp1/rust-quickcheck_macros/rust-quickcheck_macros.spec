%global source0_hash a9a28b8493dd664c8b171dd944da82d933f7d456b829bfb236738e1fe06c5ba4
%bcond check 1
%global debug_package %{nil}
%global crate quickcheck_macros
Name:           rust-quickcheck_macros
Version:        1.2.0
Release:        1%{?dist}
Summary:        Macro attribute for quickcheck
License:        Unlicense OR MIT
URL:            https://crates.io/crates/quickcheck_macros
Source0:        https://static.crates.io/crates/quickcheck_macros/quickcheck_macros-%{version}.crate
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
Summary:        Macro attribute for quickcheck
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
%files -n rust-quickcheck_macros-devel -f %{oreon_filedir}/rust-quickcheck_macros-devel.list

%changelog

%autochangelog

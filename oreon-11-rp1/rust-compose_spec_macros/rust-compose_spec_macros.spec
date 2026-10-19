%global source0_hash b77735bd89be8da01c8d7e61faec5a9ccb0e313cece3c773c6b3ae251b90c7d4
%bcond check 1
%global debug_package %{nil}
%global crate compose_spec_macros
Name:           rust-compose_spec_macros
Version:        0.1.1
Release:        1%{?dist}
Summary:        Procedural macros for use in the compose_spec crate
License:        MPL-2.0
URL:            https://crates.io/crates/compose_spec_macros
Source0:        https://static.crates.io/crates/compose_spec_macros/compose_spec_macros-%{version}.crate
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
Summary:        Procedural macros for use in the compose_spec crate
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
%files -n rust-compose_spec_macros-devel -f %{oreon_filedir}/rust-compose_spec_macros-devel.list

%changelog

%autochangelog

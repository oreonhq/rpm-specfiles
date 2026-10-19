%global source0_hash 3fd9b9dc67f2b3024582ec6d861950f0af0aeaabb8350ccda1f0e51ff8e5895c
%bcond check 0
%global debug_package %{nil}
%global crate compose_spec
Name:           rust-compose_spec
Version:        0.3.0
Release:        1%{?dist}
Summary:        Types for (de)serializing from/to the compose-spec
License:        MPL-2.0
URL:            https://crates.io/crates/compose_spec
Source0:        https://static.crates.io/crates/compose_spec/compose_spec-%{version}.crate
Patch:          compose_spec-fix-metadata.diff
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
Summary:        Types for (de)serializing from/to the compose-spec
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
%files -n rust-compose_spec-devel -f %{oreon_filedir}/rust-compose_spec-devel.list

%changelog

%autochangelog

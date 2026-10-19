%global source0_hash 6ff55baddef9e4ad00f88b6c743a2a8062d4c6ade126c2a528644b8e444d52ce
%bcond check 0
%global debug_package %{nil}
%global crate owning_ref
Name:           rust-owning_ref
Version:        0.4.1
Release:        1%{?dist}
Summary:        A library for creating references that carry their owner with them.
License:        MIT
URL:            https://crates.io/crates/owning_ref
Source0:        https://static.crates.io/crates/owning_ref/owning_ref-%{version}.crate
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
Summary:        A library for creating references that carry their owner with them.
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
%files -n rust-owning_ref-devel -f %{oreon_filedir}/rust-owning_ref-devel.list

%changelog

%autochangelog

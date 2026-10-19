%global source0_hash 0cb98a29bdd7ef95b490050ddabe4ddd816e527ea0df9f25cc7a9a30d2584dc1
%bcond check 1
%global debug_package %{nil}
%global crate ironrdp-connector
Name:           rust-ironrdp-connector
Version:        0.6.0
Release:        1%{?dist}
Summary:        State machines to drive an RDP connection sequence
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ironrdp-connector
Source0:        https://static.crates.io/crates/ironrdp-connector/ironrdp-connector-%{version}.crate
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
Summary:        State machines to drive an RDP connection sequence
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary-devel
Summary:        State machines to drive an RDP connection sequence
BuildArch:      noarch
%description -n %{name}+arbitrary-devel

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

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
%files -n rust-ironrdp-connector-devel -f %{oreon_filedir}/rust-ironrdp-connector-devel.list

%changelog

%autochangelog

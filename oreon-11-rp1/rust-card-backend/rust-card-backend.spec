%global source0_hash bd3ee3a298842065dc489180c34a4fe4bbbb8643bb422009d79558a099fb42e5
%bcond check 0
%global debug_package %{nil}
%global crate card-backend
Name:           rust-card-backend
Version:        0.2.0
Release:        1%{?dist}
Summary:        Card backend trait, for use with the openpgp-card crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/card-backend
Source0:        https://static.crates.io/crates/card-backend/card-backend-%{version}.crate
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
Summary:        Card backend trait, for use with the openpgp-card crate
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
%files -n rust-card-backend-devel -f %{oreon_filedir}/rust-card-backend-devel.list

%changelog

%autochangelog

%global source0_hash 5692dd7b5a1978a5aeb0ce83b7655c58ca8efdcb79d21036ea249da95afec2c6
%bcond check 0
%global debug_package %{nil}
%global crate escape8259
Name:           rust-escape8259
Version:        0.5.3
Release:        1%{?dist}
Summary:        RFC8259-compliant string escaping and un-escaping
License:        MIT
URL:            https://crates.io/crates/escape8259
Source0:        https://static.crates.io/crates/escape8259/escape8259-%{version}.crate
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
Summary:        RFC8259-compliant string escaping and un-escaping
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
%files -n rust-escape8259-devel -f %{oreon_filedir}/rust-escape8259-devel.list

%changelog

%autochangelog

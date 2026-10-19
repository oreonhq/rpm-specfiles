%global source0_hash 08808e3c483c46e999108051c78334f473d5adb59d78bb80a1268c7e6aa6c514
%bcond check 0
%global debug_package %{nil}
%global crate postgres-protocol
Name:           rust-postgres-protocol
Version:        0.6.12
Release:        1%{?dist}
Summary:        Low level Postgres protocol APIs
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/postgres-protocol
Source0:        https://static.crates.io/crates/postgres-protocol/postgres-protocol-%{version}.crate
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
Summary:        Low level Postgres protocol APIs
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Low level Postgres protocol APIs
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+js-devel
Summary:        Low level Postgres protocol APIs
BuildArch:      noarch
%description -n %{name}+js-devel

This package contains library source intended for building other packages which
use the "js" feature of the "%{crate}" crate.

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
%files -n rust-postgres-protocol-devel -f %{oreon_filedir}/rust-postgres-protocol-devel.list

%changelog

%autochangelog

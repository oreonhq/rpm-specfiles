%global source0_hash 96e1090e37c7188a99a2353115083505ff6a489e86637dc41e1671457b1259d3
%bcond check 1
%global debug_package %{nil}
%global crate implib
Name:           rust-implib0.6
Version:        0.6.0
Release:        1%{?dist}
Summary:        Generate Windows import library from module definition file
License:        MIT
URL:            https://crates.io/crates/implib
Source0:        https://static.crates.io/crates/implib/implib-%{version}.crate
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
Summary:        Generate Windows import library from module definition file
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+gnu-devel
Summary:        Generate Windows import library from module definition file
BuildArch:      noarch
%description -n %{name}+gnu-devel

This package contains library source intended for building other packages which
use the "gnu" feature of the "%{crate}" crate.

%package     -n %{name}+msvc-devel
Summary:        Generate Windows import library from module definition file
BuildArch:      noarch
%description -n %{name}+msvc-devel

This package contains library source intended for building other packages which
use the "msvc" feature of the "%{crate}" crate.

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
%files -n rust-implib0.6-devel -f %{oreon_filedir}/rust-implib0.6-devel.list

%changelog

%autochangelog

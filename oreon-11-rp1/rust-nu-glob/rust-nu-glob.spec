%global source0_hash 788679a8ac0327a41af9da83a69a6caa65aebe007ec21f410bb58557480c9b3c
%bcond check 0
%global debug_package %{nil}
%global crate nu-glob
Name:           rust-nu-glob
Version:        0.115.1
Release:        1%{?dist}
Summary:        Fork of glob
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/nu-glob
Source0:        https://static.crates.io/crates/nu-glob/nu-glob-%{version}.crate
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
Summary:        Fork of glob
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
%files -n rust-nu-glob-devel -f %{oreon_filedir}/rust-nu-glob-devel.list

%changelog

%autochangelog

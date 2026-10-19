%global source0_hash 20219d20b3b77f743358539a182e339a6f682e09bb5675f870f320c4a1058c44
%bcond check 1
%global debug_package %{nil}
%global crate minspan
Name:           rust-minspan
Version:        0.1.5
Release:        1%{?dist}
Summary:        Package for determining the minimum span of one vector within another
License:        MIT
URL:            https://crates.io/crates/minspan
Source0:        https://static.crates.io/crates/minspan/minspan-%{version}.crate
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
Summary:        Package for determining the minimum span of one vector within another
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
%files -n rust-minspan-devel -f %{oreon_filedir}/rust-minspan-devel.list

%changelog

%autochangelog

%global source0_hash 0aad070be5b63aa72103f2fcdd70a83adbd5e90112ce5b574171ff1c65501773
%bcond check 0
%global debug_package %{nil}
%global crate peg
Name:           rust-peg
Version:        0.8.6
Release:        1%{?dist}
Summary:        A simple Parsing Expression Grammar (PEG) parser generator.
License:        MIT
URL:            https://crates.io/crates/peg
Source0:        https://static.crates.io/crates/peg/peg-%{version}.crate
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

%package     -n %{name}+trace-devel
Summary:        A simple Parsing Expression Grammar (PEG) parser generator.
BuildArch:      noarch
%description -n %{name}+trace-devel

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

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
%files -n rust-peg-devel -f %{oreon_filedir}/rust-peg-devel.list

%changelog

%autochangelog

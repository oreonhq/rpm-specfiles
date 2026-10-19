%global source0_hash e1766d682d402817b5ac4490b3c3002d91dfa0d22812f341609f97b08757359c
%bcond check 1
%global debug_package %{nil}
%global crate unindent
Name:           rust-unindent0.1
Version:        0.1.11
Release:        1%{?dist}
Summary:        Remove a column of leading whitespace from a string
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/unindent
Source0:        https://static.crates.io/crates/unindent/unindent-%{version}.crate
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
Summary:        Remove a column of leading whitespace from a string
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
%files -n rust-unindent0.1-devel -f %{oreon_filedir}/rust-unindent0.1-devel.list

%changelog

%autochangelog

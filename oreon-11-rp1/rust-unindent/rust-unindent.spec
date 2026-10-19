%global source0_hash 7264e107f553ccae879d21fbea1d6724ac785e8c3bfc762137959b5802826ef3
%bcond check 1
%global debug_package %{nil}
%global crate unindent
Name:           rust-unindent
Version:        0.2.4
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
%files -n rust-unindent-devel -f %{oreon_filedir}/rust-unindent-devel.list

%changelog

%autochangelog

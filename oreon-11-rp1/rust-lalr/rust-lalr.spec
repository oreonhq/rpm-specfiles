%global source0_hash 106d7548f95adbe3019b4fc4954554d7b72535867aa9ce326d2f766b68958de7
%bcond check 0
%global debug_package %{nil}
%global crate lalr
Name:           rust-lalr
Version:        0.0.2
Release:        1%{?dist}
Summary:        Library for creating LALR(1) parsers from context-free grammars
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/lalr
Source0:        https://static.crates.io/crates/lalr/lalr-%{version}.crate
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
Summary:        Library for creating LALR(1) parsers from context-free grammars
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
%files -n rust-lalr-devel -f %{oreon_filedir}/rust-lalr-devel.list

%changelog

%autochangelog

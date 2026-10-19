%global source0_hash f9d839f2a20b0aee515dc581a6172f2321f96cab76c1a38a4c584a194955390e
%bcond check 0
%global debug_package %{nil}
%global crate const-random-macro
Name:           rust-const-random-macro
Version:        0.1.16
Release:        1%{?dist}
Summary:        Provides the procedural macro used by const-random
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/const-random-macro
Source0:        https://static.crates.io/crates/const-random-macro/const-random-macro-%{version}.crate
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
Summary:        Provides the procedural macro used by const-random
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
%files -n rust-const-random-macro-devel -f %{oreon_filedir}/rust-const-random-macro-devel.list

%changelog

%autochangelog

%global source0_hash bfa799dd5ed20a7e349f3b4639aa80d74549c81716d9ec4f994c9b5815598306
%bcond check 0
%global debug_package %{nil}
%global crate indoc
Name:           rust-indoc1
Version:        1.0.9
Release:        1%{?dist}
Summary:        Indented document literals
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/indoc
Source0:        https://static.crates.io/crates/indoc/indoc-%{version}.crate
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
Summary:        Indented document literals
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
%files -n rust-indoc1-devel -f %{oreon_filedir}/rust-indoc1-devel.list

%changelog

%autochangelog

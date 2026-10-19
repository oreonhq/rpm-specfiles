%global source0_hash 3df27b8d5ddb458c5fb1bbc1ce172d4a38c614a97d550b0ac89003897fb01de4
%bcond check 1
%global debug_package %{nil}
%global crate askama_escape
Name:           rust-askama_escape
Version:        0.13.0
Release:        1%{?dist}
Summary:        HTML escaping, extracted from Askama
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/askama_escape
Source0:        https://static.crates.io/crates/askama_escape/askama_escape-%{version}.crate
Patch:          askama_escape-fix-metadata.diff
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
Summary:        HTML escaping, extracted from Askama
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
%files -n rust-askama_escape-devel -f %{oreon_filedir}/rust-askama_escape-devel.list

%changelog

%autochangelog

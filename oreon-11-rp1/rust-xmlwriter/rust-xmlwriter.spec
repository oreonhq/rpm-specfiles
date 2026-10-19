%global source0_hash ec7a2a501ed189703dba8b08142f057e887dfc4b2cc4db2d343ac6376ba3e0b9
%bcond check 0
%global debug_package %{nil}
%global crate xmlwriter
Name:           rust-xmlwriter
Version:        0.1.0
Release:        1%{?dist}
Summary:        Simple, streaming XML writer
License:        MIT
URL:            https://crates.io/crates/xmlwriter
Source0:        https://static.crates.io/crates/xmlwriter/xmlwriter-%{version}.crate
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
Summary:        Simple, streaming XML writer
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
%files -n rust-xmlwriter-devel -f %{oreon_filedir}/rust-xmlwriter-devel.list

%changelog

%autochangelog

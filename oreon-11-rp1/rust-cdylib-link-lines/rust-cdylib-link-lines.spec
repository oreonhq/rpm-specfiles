%global source0_hash d98eabef08bbdf5afd0b9c0cabb1ac335f7c70447ef095eed85dffd9628b20bc
%bcond check 0
%global debug_package %{nil}
%global crate cdylib-link-lines
Name:           rust-cdylib-link-lines
Version:        0.1.5
Release:        1%{?dist}
Summary:        Collection of link-lines useful to build correct cdylibs on targets
License:        MIT
URL:            https://crates.io/crates/cdylib-link-lines
Source0:        https://static.crates.io/crates/cdylib-link-lines/cdylib-link-lines-%{version}.crate
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
Summary:        Collection of link-lines useful to build correct cdylibs on targets
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
%files -n rust-cdylib-link-lines-devel -f %{oreon_filedir}/rust-cdylib-link-lines-devel.list

%changelog

%autochangelog

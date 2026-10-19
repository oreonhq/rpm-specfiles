%global source0_hash 10b322c8c13b6b775e5befd834d2a27c683506f1100b56a7b39d33c28024ba54
%bcond check 1
%global debug_package %{nil}
%global crate build_html
Name:           rust-build_html
Version:        2.7.0
Release:        1%{?dist}
Summary:        Library for basic server-side rendering written in pure rust
License:        MIT
URL:            https://crates.io/crates/build_html
Source0:        https://static.crates.io/crates/build_html/build_html-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  sed
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Library for basic server-side rendering written in pure rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
sed -i 's/\r$//' README.md
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
%files -n rust-build_html-devel -f %{oreon_filedir}/rust-build_html-devel.list

%changelog

%autochangelog

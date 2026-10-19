%global source0_hash a4549325971814bda7a44061bf3fe7e487d447cba01e4220a4b454d630d7a016
%bcond check 1
%global debug_package %{nil}
%global crate enum-iterator
Name:           rust-enum-iterator
Version:        2.3.0
Release:        1%{?dist}
Summary:        Tools to iterate over all values of a type
License:        0BSD
URL:            https://crates.io/crates/enum-iterator
Source0:        https://static.crates.io/crates/enum-iterator/enum-iterator-%{version}.crate
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
Summary:        Tools to iterate over all values of a type
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
%files -n rust-enum-iterator-devel -f %{oreon_filedir}/rust-enum-iterator-devel.list

%changelog

%autochangelog

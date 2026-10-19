%global source0_hash 803ec87c9cfb29b9d2633f20cba1f488db3fd53f2158b1024cbefb47ba05d413
%bcond check 1
%global debug_package %{nil}
%global crate lexopt
Name:           rust-lexopt
Version:        0.3.2
Release:        1%{?dist}
Summary:        Minimalist pedantic command line parser
License:        MIT
URL:            https://crates.io/crates/lexopt
Source0:        https://static.crates.io/crates/lexopt/lexopt-%{version}.crate
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
Summary:        Minimalist pedantic command line parser
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
%files -n rust-lexopt-devel -f %{oreon_filedir}/rust-lexopt-devel.list

%changelog

%autochangelog

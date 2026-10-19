%global source0_hash d6398cde53adc3c4557306a96ce67b302968513830a77a95b2b17305d9719a89
%bcond check 0
%global debug_package %{nil}
%global crate supports-color
Name:           rust-supports-color2
Version:        2.1.0
Release:        1%{?dist}
Summary:        Detects whether a terminal supports color, and gives details about th...
License:        Apache-2.0
URL:            https://crates.io/crates/supports-color
Source0:        https://static.crates.io/crates/supports-color/supports-color-%{version}.crate
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
Summary:        Detects whether a terminal supports color, and gives details about th...
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
%files -n rust-supports-color2-devel -f %{oreon_filedir}/rust-supports-color2-devel.list

%changelog

%autochangelog

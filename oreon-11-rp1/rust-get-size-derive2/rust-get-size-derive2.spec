%global source0_hash 7efe46d2adb529015748742f1a38594039ce357dbb21e6d178de342cfce468d4
%bcond check 0
%global debug_package %{nil}
%global crate get-size-derive2
Name:           rust-get-size-derive2
Version:        0.11.0
Release:        1%{?dist}
Summary:        Derives the GetSize trait
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/get-size-derive2
Source0:        https://static.crates.io/crates/get-size-derive2/get-size-derive2-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Derives the GetSize trait
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
find . -type f -exec dos2unix --keepdate '{}' '+'
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
%files -n rust-get-size-derive2-devel -f %{oreon_filedir}/rust-get-size-derive2-devel.list

%changelog

%autochangelog

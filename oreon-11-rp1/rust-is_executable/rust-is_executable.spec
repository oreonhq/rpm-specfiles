%global source0_hash 82cb6a9f675da968c63b6208c641b9dca58fc0133ae53375736b1767b0cab8bd
%bcond check 0
%global debug_package %{nil}
%global crate is_executable
Name:           rust-is_executable
Version:        1.0.6
Release:        1%{?dist}
Summary:        Is there an executable file at the given path?
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/is_executable
Source0:        https://static.crates.io/crates/is_executable/is_executable-%{version}.crate
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
Summary:        Is there an executable file at the given path?
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
%files -n rust-is_executable-devel -f %{oreon_filedir}/rust-is_executable-devel.list

%changelog

%autochangelog

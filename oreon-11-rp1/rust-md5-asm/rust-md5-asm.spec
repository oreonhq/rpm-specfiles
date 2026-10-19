%global source0_hash d19b8ee7fc7d812058d3b708c7f719efd0713d53854648e4223c6fcae709e2df
%bcond check 0
%global debug_package %{nil}
%global crate md5-asm
Name:           rust-md5-asm
Version:        0.5.2
Release:        1%{?dist}
Summary:        Assembly implementation of MD5 compression function
License:        MIT
URL:            https://crates.io/crates/md5-asm
Source0:        https://static.crates.io/crates/md5-asm/md5-asm-%{version}.crate
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
Summary:        Assembly implementation of MD5 compression function
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
%files -n rust-md5-asm-devel -f %{oreon_filedir}/rust-md5-asm-devel.list

%changelog

%autochangelog

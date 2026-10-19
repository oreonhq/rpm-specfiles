%global source0_hash 5ff4ae71b685bbad2f2f391fe74f6b7659a34871c08b210fdc039e43bee07d18
%bcond check 0
%global debug_package %{nil}
%global crate libflate
Name:           rust-libflate1
Version:        1.4.0
Release:        1%{?dist}
Summary:        Rust implementation of DEFLATE algorithm and related formats
License:        MIT
URL:            https://crates.io/crates/libflate
Source0:        https://static.crates.io/crates/libflate/libflate-%{version}.crate
Patch:          libflate-fix-metadata.diff
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
Summary:        Rust implementation of DEFLATE algorithm and related formats
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
%files -n rust-libflate1-devel -f %{oreon_filedir}/rust-libflate1-devel.list

%changelog

%autochangelog

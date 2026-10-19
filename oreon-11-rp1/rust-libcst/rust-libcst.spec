%global source0_hash 6aea7143e4a0ed59b87a1ee71e198500889f8b005311136be15e84c97a6fcd8d
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate libcst
Name:           rust-libcst
Version:        1.8.6
Release:        1%{?dist}
Summary:        Python parser and Concrete Syntax Tree library
License:        MIT AND (MIT AND PSF-2.0)
URL:            https://crates.io/crates/libcst
Source0:        https://static.crates.io/crates/libcst/libcst-%{version}.crate
Patch:          libcst-fix-metadata.diff
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
Summary:        Python parser and Concrete Syntax Tree library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+trace-devel
Summary:        Python parser and Concrete Syntax Tree library
BuildArch:      noarch
%description -n %{name}+trace-devel

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm tests/parser_roundtrip.rs
dos2unix --keepdate tests/fixtures/type_parameters.py
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
%files -n rust-libcst-devel -f %{oreon_filedir}/rust-libcst-devel.list

%changelog

%autochangelog

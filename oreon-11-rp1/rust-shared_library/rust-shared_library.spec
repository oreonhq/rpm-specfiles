%global source0_hash 5a9e7e0f2bfae24d8a5b5a66c5b257a83c7412304311512a0c054cd5e619da11
%bcond check 0
%global debug_package %{nil}
%global crate shared_library
Name:           rust-shared_library
Version:        0.1.9
Release:        1%{?dist}
Summary:        Easily bind to and load shared libraries
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/shared_library
Source0:        https://static.crates.io/crates/shared_library/shared_library-%{version}.crate
Patch:          0001-Load-libm-for-the-cos-symbol-to-fix-tests.patch
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
Summary:        Easily bind to and load shared libraries
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
%files -n rust-shared_library-devel -f %{oreon_filedir}/rust-shared_library-devel.list

%changelog

%autochangelog

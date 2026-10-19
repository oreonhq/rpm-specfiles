%global source0_hash 254a5372af8fc138e36684761d3c0cdb758a4410e938babcff1c860ce14ddbfc
%bcond check 0
%global debug_package %{nil}
%global crate nalgebra-macros
Name:           rust-nalgebra-macros0.2
Version:        0.2.2
Release:        1%{?dist}
Summary:        Procedural macros for nalgebra
License:        Apache-2.0
URL:            https://crates.io/crates/nalgebra-macros
Source0:        https://static.crates.io/crates/nalgebra-macros/nalgebra-macros-%{version}.crate
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
Summary:        Procedural macros for nalgebra
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
find . -type f -exec dos2unix --keepdate '{}' +
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
%files -n rust-nalgebra-macros0.2-devel -f %{oreon_filedir}/rust-nalgebra-macros0.2-devel.list

%changelog

%autochangelog

%global source0_hash bf36173d4167ed999940f804952e6b08197cae5ad5d572eb4db150ce8ad5d58f
%bcond check 0
%global debug_package %{nil}
%global crate lab
Name:           rust-lab
Version:        0.11.0
Release:        1%{?dist}
Summary:        Tools for converting RGB colors to the CIE-L*a*b* color space, and
License:        MIT
URL:            https://crates.io/crates/lab
Source0:        https://static.crates.io/crates/lab/lab-%{version}.crate
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
Summary:        Tools for converting RGB colors to the CIE-L*a*b* color space, and
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
%files -n rust-lab-devel -f %{oreon_filedir}/rust-lab-devel.list

%changelog

%autochangelog

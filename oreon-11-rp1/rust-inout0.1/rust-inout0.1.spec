%global source0_hash 879f10e63c20629ecabbb64a8010319738c66a5cd0c29b02d63d272b03751d01
%bcond check 0
%global debug_package %{nil}
%global crate inout
Name:           rust-inout0.1
Version:        0.1.4
Release:        1%{?dist}
Summary:        Custom reference types for code generic over in-place and
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/inout
Source0:        https://static.crates.io/crates/inout/inout-%{version}.crate
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
use the "inout" crate.

%package     -n %{name}+default-devel
Summary:        Custom reference types for code generic over in-place and
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+block-padding-devel
Summary:        Custom reference types for code generic over in-place and
BuildArch:      noarch
%description -n %{name}+block-padding-devel

This package contains library source intended for building other packages which
use the "block-padding" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Custom reference types for code generic over in-place and
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version}
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
%files -n rust-inout0.1-devel -f %{oreon_filedir}/rust-inout0.1-devel.list

%changelog

%autochangelog

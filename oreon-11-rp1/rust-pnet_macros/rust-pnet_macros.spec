%global source0_hash 13325ac86ee1a80a480b0bc8e3d30c25d133616112bb16e86f712dcf8a71c863
%bcond check 1
%global debug_package %{nil}
%global crate pnet_macros
Name:           rust-pnet_macros
Version:        0.35.0
Release:        1%{?dist}
Summary:        Automatic bit manipulation for binary data formats
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/pnet_macros
Source0:        https://static.crates.io/crates/pnet_macros/pnet_macros-%{version}.crate
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
Summary:        Automatic bit manipulation for binary data formats
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

%cargo_test -- -- --skip compile
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-pnet_macros-devel -f %{oreon_filedir}/rust-pnet_macros-devel.list

%changelog

%autochangelog

%global source0_hash bdff162541cd8b79de82e2edcc7eff3a8c2a6dc3d75152636028f96d93de3b26
%bcond check 0
%global debug_package %{nil}
%global crate codepage
Name:           rust-codepage
Version:        0.1.3
Release:        1%{?dist}
Summary:        Mapping between Windows code page numbers and encoding_rs character encodings
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/codepage
Source0:        https://static.crates.io/crates/codepage/codepage-%{version}.crate
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
Summary:        Mapping between Windows code page numbers and encoding_rs character encodings
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
%files -n rust-codepage-devel -f %{oreon_filedir}/rust-codepage-devel.list

%changelog

%autochangelog

%global source0_hash 849f6b1fe8a0fb07170737d7f3acf72cac5462fb3f4e86614474a49f7fac3b65
%bcond check 0
%global debug_package %{nil}
%global crate uapi-version
Name:           rust-uapi-version
Version:        0.4.0
Release:        1%{?dist}
Summary:        Compare versions according to the UAPI Version Format Specification
License:        MIT
URL:            https://crates.io/crates/uapi-version
Source0:        https://static.crates.io/crates/uapi-version/uapi-version-%{version}.crate
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
Summary:        Compare versions according to the UAPI Version Format Specification
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
%files -n rust-uapi-version-devel -f %{oreon_filedir}/rust-uapi-version-devel.list

%changelog

%autochangelog

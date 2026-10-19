%global source0_hash 4687412b5ac74d245d5bfb1733ede50c31be19bf8a4b6a967a29b451bab49e67
%bcond check 0
%global debug_package %{nil}
%global crate uefi-macros
%global unsupported_arches ppc64le s390x
Name:           rust-uefi-macros
Version:        0.19.0
Release:        1%{?dist}
Summary:        Procedural macros for the uefi crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/uefi-macros
Source0:        https://static.crates.io/crates/uefi-macros/uefi-macros-%{version}.crate
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
Summary:        Procedural macros for the uefi crate
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%ifnarch %{unsupported_arches}
%cargo_build
%endif
%install
%cargo_install
%if %{with check}
%ifnarch %{unsupported_arches}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-uefi-macros-devel -f %{oreon_filedir}/rust-uefi-macros-devel.list

%changelog

%autochangelog

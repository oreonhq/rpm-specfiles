%global source0_hash 5b02aa90784a2542ff7b9ad3871efc30c9a2b3751d6f21706e83a086ff398694
%bcond check 1
%global debug_package %{nil}
%global crate resctrlfs
%global unsupported_arches %{ix86}
Name:           rust-resctrlfs
Version:        0.9.0
Release:        1%{?dist}
Summary:        A crate for reading resctrl fs data
License:        Apache-2.0
URL:            https://crates.io/crates/resctrlfs
Source0:        https://static.crates.io/crates/resctrlfs/resctrlfs-%{version}.crate
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
Summary:        A crate for reading resctrl fs data
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
%files -n rust-resctrlfs-devel -f %{oreon_filedir}/rust-resctrlfs-devel.list

%changelog

%autochangelog

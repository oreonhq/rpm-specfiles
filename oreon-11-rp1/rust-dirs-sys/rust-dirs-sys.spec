%global source0_hash e01a3366d27ee9890022452ee61b2b63a67e6f13f58900b651ff5665f0bb1fab
%bcond check 0
%global debug_package %{nil}
%global crate dirs-sys
Name:           rust-dirs-sys
Version:        0.5.0
Release:        1%{?dist}
Summary:        System-level helper functions for the dirs and directories crates.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/dirs-sys
Source0:        https://static.crates.io/crates/dirs-sys/dirs-sys-%{version}.crate
Patch:          dirs-sys-fix-metadata-auto.diff
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
Summary:        System-level helper functions for the dirs and directories crates.
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
%files -n rust-dirs-sys-devel -f %{oreon_filedir}/rust-dirs-sys-devel.list

%changelog

%autochangelog

%global source0_hash 4ebda144c4fe02d1f7ea1a7d9641b6fc6b580adcfa024ae48797ecdeb6825b4d
%bcond check 0
%global debug_package %{nil}
%global crate dirs-sys-next
Name:           rust-dirs-sys-next
Version:        0.1.2
Release:        2%{?dist}
Summary:        system-level helper functions for the dirs and directories crates
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/dirs-sys-next
Source0:        https://static.crates.io/crates/dirs-sys-next/dirs-sys-next-%{version}.crate
Patch:          dirs-sys-next-fix-metadata-auto.diff
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
Summary:        system-level helper functions for the dirs and directories crates
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
%files -n rust-dirs-sys-next-devel -f %{oreon_filedir}/rust-dirs-sys-next-devel.list

%changelog

%autochangelog

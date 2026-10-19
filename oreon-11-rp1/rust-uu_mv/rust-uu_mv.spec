%global source0_hash f678a9ce279116c4d1aa3dc460be904069336adc63d9130acdb543568bee22a6
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_mv
Name:           rust-uu_mv
Version:        0.7.0
Release:        1%{?dist}
Summary:        mv ~ (uutils) move (rename) SOURCE to DESTINATION
License:        MIT
URL:            https://crates.io/crates/uu_mv
Source0:        https://static.crates.io/crates/uu_mv/uu_mv-%{version}.crate
Patch:          uu_mv-fix-metadata-auto.diff
Patch:          uu_mv-fix-metadata.diff
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
Summary:        mv ~ (uutils) move (rename) SOURCE to DESTINATION
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+selinux-devel
Summary:        mv ~ (uutils) move (rename) SOURCE to DESTINATION
BuildArch:      noarch
%description -n %{name}+selinux-devel

This package contains library source intended for building other packages which
use the "selinux" feature of the "%{crate}" crate.

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
%files -n rust-uu_mv-devel -f %{oreon_filedir}/rust-uu_mv-devel.list

%changelog

%autochangelog

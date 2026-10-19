%global source0_hash cb65631fc1a8e8834bd30ac4ad8ee337c6d5a46c15254dfdbdfaea96f7290fa1
%bcond check 1
%global debug_package %{nil}
%global cargo_install_bin 0
%global crate uu_rm
Name:           rust-uu_rm
Version:        0.7.0
Release:        1%{?dist}
Summary:        rm ~ (uutils) remove PATHNAME
License:        MIT
URL:            https://crates.io/crates/uu_rm
Source0:        https://static.crates.io/crates/uu_rm/uu_rm-%{version}.crate
Patch:          uu_rm-fix-metadata-auto.diff
Patch:          uu_rm-fix-metadata.diff
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
Summary:        rm ~ (uutils) remove PATHNAME
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
%files -n rust-uu_rm-devel -f %{oreon_filedir}/rust-uu_rm-devel.list

%changelog

%autochangelog

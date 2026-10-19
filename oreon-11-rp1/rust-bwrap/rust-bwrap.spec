%global source0_hash d13da3319ae5c5771712fba7b79b028793149bc462a08990bc8fd7c7554dbb95
%bcond check 0
%global debug_package %{nil}
%global crate bwrap
Name:           rust-bwrap
Version:        1.3.0
Release:        1%{?dist}
Summary:        Fast, lightweight, embedded systems-friendly library for wrapping text
License:        MIT OR GPL-3.0-or-later
URL:            https://crates.io/crates/bwrap
Source0:        https://static.crates.io/crates/bwrap/bwrap-%{version}.crate
Patch:          bwrap-fix-metadata.diff
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
Summary:        Fast, lightweight, embedded systems-friendly library for wrapping text
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+use_std-devel
Summary:        Fast, lightweight, embedded systems-friendly library for wrapping text
BuildArch:      noarch
%description -n %{name}+use_std-devel

This package contains library source intended for building other packages which
use the "use_std" feature of the "%{crate}" crate.

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
%files -n rust-bwrap-devel -f %{oreon_filedir}/rust-bwrap-devel.list

%changelog

%autochangelog

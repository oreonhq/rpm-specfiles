%global source0_hash 8eab9a99a024a169fe8a903cf9d4a3b3601109bcc13bd9e3c6fff259138626c4
%bcond check 0
%global debug_package %{nil}
%global crate sys-locale
Name:           rust-sys-locale
Version:        0.3.2
Release:        1%{?dist}
Summary:        Small and lightweight library to obtain the active system locale
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sys-locale
Source0:        https://static.crates.io/crates/sys-locale/sys-locale-%{version}.crate
Patch:          sys-locale-fix-metadata-auto.diff
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
Summary:        Small and lightweight library to obtain the active system locale
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
%files -n rust-sys-locale-devel -f %{oreon_filedir}/rust-sys-locale-devel.list

%changelog

%autochangelog

%global source0_hash 17e913097e1a2124b46746c980134e8c954bc17a6a59bb3fde96f088d126dde6
%bcond check 1
%global debug_package %{nil}
%global crate ammonia
Name:           rust-ammonia
Version:        4.1.2
Release:        1%{?dist}
Summary:        HTML Sanitization
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ammonia
Source0:        https://static.crates.io/crates/ammonia/ammonia-%{version}.crate
Patch:          ammonia-fix-metadata.diff
Patch:          0001-Revert-changes-for-cssparser-0.35.patch
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
Summary:        HTML Sanitization
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
%files -n rust-ammonia-devel -f %{oreon_filedir}/rust-ammonia-devel.list

%changelog

%autochangelog

%global source0_hash 3e0f1c7c3a72c66fd80abe965175f7523475c0489a87d3ff9d6e8c87d87a9d2d
%bcond check 1
%global debug_package %{nil}
%global crate find-msvc-tools
Name:           rust-find-msvc-tools
Version:        0.1.12
Release:        2%{?dist}
Summary:        Find windows-specific tools, read MSVC versions from the registry and from COM interfaces
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/find-msvc-tools
Source0:        https://static.crates.io/crates/find-msvc-tools/find-msvc-tools-%{version}.crate
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
Summary:        Find windows-specific tools, read MSVC versions from the registry and from COM interfaces
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
%files -n rust-find-msvc-tools-devel -f %{oreon_filedir}/rust-find-msvc-tools-devel.list

%changelog

%autochangelog

%global source0_hash 7539aeb3fdd8cb4f6a331307cf71a1039cee75e94e8a71725b9484f4a0d9451a
%bcond check 1
%global debug_package %{nil}
%global crate platform-info
Name:           rust-platform-info
Version:        2.0.5
Release:        1%{?dist}
Summary:        Simple cross-platform interface to get info about a system
License:        MIT
URL:            https://crates.io/crates/platform-info
Source0:        https://static.crates.io/crates/platform-info/platform-info-%{version}.crate
Patch:          platform-info-fix-metadata-auto.diff
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
Summary:        Simple cross-platform interface to get info about a system
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
%files -n rust-platform-info-devel -f %{oreon_filedir}/rust-platform-info-devel.list

%changelog

%autochangelog

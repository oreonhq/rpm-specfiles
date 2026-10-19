%global source0_hash 07da4ce523b4e2ebaaf330746761df23a465b951a83d84bbce4233dabedae630
%bcond check 0
%global debug_package %{nil}
%global crate async-session
Name:           rust-async-session
Version:        3.0.0
Release:        1%{?dist}
Summary:        Async session support with pluggable middleware
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/async-session
Source0:        https://static.crates.io/crates/async-session/async-session-%{version}.crate
Patch0:         async-session-bump-deps.patch
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
Summary:        Async session support with pluggable middleware
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
%files -n rust-async-session-devel -f %{oreon_filedir}/rust-async-session-devel.list

%changelog

%autochangelog

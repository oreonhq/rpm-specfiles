%global source0_hash 9bb517913cfcfb9eeda59f36020269075a152701a01606c612f547e4890be399
%bcond check 1
%global debug_package %{nil}
%global crate mock_instant
Name:           rust-mock_instant
Version:        0.6.1
Release:        1%{?dist}
Summary:        Simple way to mock an std::time::Instant
License:        0BSD
URL:            https://crates.io/crates/mock_instant
Source0:        https://static.crates.io/crates/mock_instant/mock_instant-%{version}.crate
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
Summary:        Simple way to mock an std::time::Instant
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
%files -n rust-mock_instant-devel -f %{oreon_filedir}/rust-mock_instant-devel.list

%changelog

%autochangelog

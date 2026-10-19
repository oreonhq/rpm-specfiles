%global source0_hash 6d8de370f98a6cb8a4606618e53e802f93b094ddec0f96988eaec2c27e6e9ce7
%bcond check 0
%global debug_package %{nil}
%global crate libtest-mimic
Name:           rust-libtest-mimic
Version:        0.6.1
Release:        1%{?dist}
Summary:        Write your own test harness that looks and behaves like the built-in...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/libtest-mimic
Source0:        https://static.crates.io/crates/libtest-mimic/libtest-mimic-%{version}.crate
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
Summary:        Write your own test harness that looks and behaves like the built-in...
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
%files -n rust-libtest-mimic-devel -f %{oreon_filedir}/rust-libtest-mimic-devel.list

%changelog

%autochangelog
